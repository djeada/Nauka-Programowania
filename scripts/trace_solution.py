#!/usr/bin/env python3
"""
Śledzi wykonanie rozwiązania w Pythonie — na potrzeby wizualizacji w PDF-ie (generate_pdf.py).

Program jest uruchamiany w osobnym procesie z podanym wejściem. sys.settrace zapisuje każdą
wykonaną linię (ze stanem zmiennych po jej wykonaniu i tym, co wypisała) oraz wywołania
i powroty funkcji. Z tego powstaje:

* tabela przebiegu — kolejne linie i wartości zmiennych (zmienione wartości wyróżnione),
* drzewo wywołań — dla funkcji rekurencyjnych (argumenty i zwracane wartości).

Użycie z linii poleceń (podgląd):
    python3 scripts/trace_solution.py src/python/04_petla_wprowadzenie/zad04.py < wejscie.txt
"""

import ast
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

MAX_EVENTS = 4000
VALUE_WIDTH = 22
SKIP_LINES = re.compile(r"^\s*(def |class |import |from |@|if __name__ ==|$|#)")

# --------------------------------------------------------------------------- proces śledzący


def _runner(path: str) -> None:  # uruchamiane w procesie potomnym
    import io
    import types

    real_stdout = sys.stdout
    captured = io.StringIO()
    sys.stdout = captured
    events: List[Dict[str, Any]] = []
    hidden = (
        types.ModuleType,
        types.FunctionType,
        types.BuiltinFunctionType,
        type,
        types.MethodType,
    )

    def short(value: Any, depth: int = 0) -> str:
        try:
            if isinstance(value, float):
                text = repr(round(value, 6))
            elif (
                hasattr(value, "__dict__")
                and not isinstance(value, hidden)
                and depth == 0
                and type(value).__repr__ is object.__repr__
            ):
                attrs = ", ".join(
                    f"{k}={short(v, 1)}"
                    for k, v in vars(value).items()
                    if not k.startswith("__")
                )
                text = f"{type(value).__name__}({attrs})"
            else:
                text = repr(value)
        except (
            Exception
        ):  # noqa: BLE001 — repr zdefiniowany przez ucznia może rzucić wyjątek
            text = f"<{type(value).__name__}>"
        return text if len(text) <= VALUE_WIDTH else text[: VALUE_WIDTH - 1] + "…"

    def snapshot(frame: Any) -> Dict[str, str]:
        result = {}
        for name, value in frame.f_locals.items():
            if name.startswith("__") or isinstance(value, hidden):
                continue
            result[name] = short(value)
        return result

    def is_class_body(frame: Any) -> bool:
        return (
            frame.f_code.co_name != "<module>"
            and "__qualname__" in frame.f_locals
            and "__module__" in frame.f_locals
        )

    def tracer(frame: Any, event: str, arg: Any) -> Any:
        if frame.f_code.co_filename != path or is_class_body(frame):
            return None
        if len(events) >= MAX_EVENTS:
            sys.settrace(None)
            return None
        record = {
            "e": event,
            "f": id(frame),
            "fn": frame.f_code.co_name,
            "ln": frame.f_lineno,
            "out": len(captured.getvalue()),
        }
        if event == "call":
            record["args"] = snapshot(frame)
        elif event in ("line", "return"):
            record["vars"] = snapshot(frame)
            if event == "return":
                record["ret"] = short(arg)
        events.append(record)
        return tracer

    source = Path(path).read_text(encoding="utf-8")
    code = compile(source, path, "exec")
    error = None
    sys.settrace(tracer)
    try:
        exec(code, {"__name__": "__main__", "__file__": path})
    except SystemExit:
        pass
    except BaseException as exc:  # noqa: BLE001
        error = f"{type(exc).__name__}: {exc}"
    finally:
        sys.settrace(None)
        sys.stdout = real_stdout
    json.dump(
        {
            "events": events,
            "output": captured.getvalue(),
            "error": error,
            "truncated": len(events) >= MAX_EVENTS,
        },
        real_stdout,
    )


def run_trace(
    code: str, stdin: str, files: Optional[Dict[str, Any]] = None, timeout: float = 10
) -> Optional[Dict[str, Any]]:
    """Uruchamia `code` z wejściem `stdin` (i plikami z przykładu) i zwraca zapis przebiegu."""
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "katalog"
        work.mkdir()
        for name, content in (files or {}).items():
            target = work / name
            if name.endswith("/"):
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(content, dict):
                content = content.get("repeat", "x") * int(content.get("times", 0))
            target.write_text(content or "", encoding="utf-8")
        script = Path(tmp) / "rozwiazanie.py"
        script.write_text(code, encoding="utf-8")
        try:
            run = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    str(Path(__file__).resolve()),
                    "--run",
                    str(script),
                ],
                input=stdin if stdin.endswith("\n") or not stdin else stdin + "\n",
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=work,
                env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            )
        except subprocess.TimeoutExpired:
            return None
        if run.returncode != 0 or not run.stdout.strip():
            return None
        try:
            return json.loads(run.stdout)
        except json.JSONDecodeError:
            return None


# ------------------------------------------------------------------------------- analiza


def call_tree(trace: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Drzewo wywołań, jeśli któraś funkcja wywołuje samą siebie (inaczej None)."""
    root: Dict[str, Any] = {"children": []}
    stack = [root]
    recursive = set()
    for event in trace["events"]:
        if event["fn"] == "<module>":
            continue
        if event["e"] == "call":
            if any(node.get("fn") == event["fn"] for node in stack[1:]):
                recursive.add(event["fn"])
            node = {
                "fn": event["fn"],
                "args": event.get("args", {}),
                "ret": None,
                "children": [],
            }
            stack[-1]["children"].append(node)
            stack.append(node)
        elif event["e"] == "return" and len(stack) > 1:
            stack[-1]["ret"] = event.get("ret")
            stack.pop()
    if not recursive:
        return None

    def keep(node: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Zostawia tylko wywołania funkcji rekurencyjnych (pomocnicze są zwijane)."""
        result = []
        for child in node["children"]:
            if child["fn"] in recursive:
                child["children"] = keep(child)
                result.append(child)
            else:
                result.extend(keep(child))
        return result

    roots = keep(root)
    return {"fn": None, "children": roots} if len(roots) != 1 else roots[0]


def imported_names(code: str) -> set:
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return set()
    names = set()
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names.update(
                (alias.asname or alias.name).split(".")[0] for alias in node.names
            )
    return names


def state_table(
    trace: Dict[str, Any], code: str, max_columns: int = 6
) -> Optional[Dict[str, Any]]:
    """Wiersze „linia → stan zmiennych po jej wykonaniu → wypisany tekst”."""
    lines = code.split("\n")
    events = trace["events"]
    output = trace["output"]
    pending: Dict[int, Tuple[int, Dict[str, Any]]] = {}
    rows: List[Dict[str, Any]] = []
    for index, event in enumerate(events):
        frame = event["f"]
        if event["e"] in ("line", "return") and frame in pending:
            start, opened = pending.pop(frame)
            rows.append(
                {
                    "ln": opened["ln"],
                    "fn": opened["fn"],
                    "vars": event["vars"],
                    "out": output[opened["out"] : event["out"]],
                }
            )
        if event["e"] == "line":
            pending[frame] = (index, event)
    for start, opened in pending.values():  # ostatnia linia programu
        rows.append(
            {
                "ln": opened["ln"],
                "fn": opened["fn"],
                "vars": {},
                "out": output[opened["out"] :],
            }
        )

    rows = [
        r
        for r in rows
        if 0 < r["ln"] <= len(lines) and not SKIP_LINES.match(lines[r["ln"] - 1])
    ]
    if len(rows) < 2:
        return None

    # Kolumny: (funkcja, zmienna); „self” ze wszystkich metod to jedna kolumna (ten sam obiekt).
    # Przy nadmiarze kolumn zostają najczęściej zmieniane zmienne.
    def key_of(fn: str, name: str) -> Tuple[str, str]:
        return ("", name) if name == "self" else (fn, name)

    order: List[Tuple[str, str]] = []
    changes: Dict[Tuple[str, str], int] = {}
    previous: Dict[Tuple[str, str], Optional[str]] = {}
    for row in rows:
        for name, value in row["vars"].items():
            key = key_of(row["fn"], name)
            if key not in changes:
                order.append(key)
                changes[key] = 0
            if previous.get(key) != value:
                changes[key] += 1
                previous[key] = value
    # Pomijamy nazwy z importów (np. pi z modułu math) i parametry funkcji, które tylko
    # powtarzają zmienną o tej samej nazwie z programu głównego (n w main → n w funkcji).
    imported = imported_names(code)
    order = [k for k in order if not (k[0] == "<module>" and k[1] in imported)]
    module_values = {}
    redundant = set(
        k
        for k in order
        if k[0] not in ("", "<module>") and ("<module>", k[1]) in changes
    )
    for row in rows:
        if row["fn"] == "<module>":
            module_values.update(row["vars"])
            continue
        for name, value in row["vars"].items():
            key = key_of(row["fn"], name)
            if key in redundant and module_values.get(name) != value:
                redundant.discard(key)
    order = [k for k in order if k not in redundant]
    if len(order) > max_columns:
        top = sorted(order, key=lambda k: (-changes[k], order.index(k)))[:max_columns]
        order = [k for k in order if k in top]

    table_rows = []
    previous = {}
    for row in rows:
        cells = []
        for key in order:
            provided = key[1] in row["vars"] and key_of(row["fn"], key[1]) == key
            value = row["vars"][key[1]] if provided else previous.get(key)
            changed = provided and previous.get(key) != value
            if provided:
                previous[key] = value
            cells.append({"value": value, "changed": changed})
        table_rows.append(
            {
                "ln": row["ln"],
                "fn": row["fn"],
                "code": lines[row["ln"] - 1].strip(),
                "cells": cells,
                "out": row["out"],
            }
        )
    show_fn = len({key[0] for key in order if key[0]} | {r["fn"] for r in rows}) > 1
    return {
        "columns": order,
        "rows": table_rows,
        "show_fn": show_fn,
        "truncated": trace.get("truncated"),
    }


def main() -> int:
    if len(sys.argv) == 3 and sys.argv[1] == "--run":
        _runner(sys.argv[2])
        return 0
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    code = Path(sys.argv[1]).read_text(encoding="utf-8")
    trace = run_trace(code, sys.stdin.read())
    if trace is None:
        print("Nie udało się prześledzić programu.")
        return 1
    tree = call_tree(trace)
    if tree:
        print(json.dumps(tree, ensure_ascii=False, indent=1))
        return 0
    table = state_table(trace, code)
    if not table:
        print("(za mało kroków do pokazania)")
        return 0
    print(" | ".join(["linia"] + [name for _, name in table["columns"]] + ["wypisano"]))
    for row in table["rows"]:
        values = [
            ("*" if c["changed"] else "") + (c["value"] or "") for c in row["cells"]
        ]
        print(
            " | ".join(
                [f"{row['ln']}: {row['code'][:30]}"]
                + values
                + [row["out"].replace(chr(10), "⏎")]
            )
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
