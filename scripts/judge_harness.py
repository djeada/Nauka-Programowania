"""
Sędzia zadań: uruchamia program na przypadkach testowych i porównuje wyniki.

Ten plik jest jedynym źródłem prawdy o tym, kiedy rozwiązanie jest poprawne.
Korzystają z niego:

* ``scripts/run_tests.py`` — CI tego repozytorium (CPython),
* kurs na stronie https://adamdjellouli.com/courses/kurs_podstaw_pythona/
  (Pyodide w przeglądarce; plik jest kopiowany do strony bez zmian).

Dlatego moduł używa wyłącznie biblioteki standardowej i musi działać zarówno
w CPythonie, jak i w Pyodide.

Przypadek testowy (``case``) to słownik:

* ``input`` — tekst podawany na standardowe wejście,
* ``expected`` — oczekiwane wyjście (``None`` = tylko uruchom, nie oceniaj),
* ``files`` — opcjonalnie: pliki tworzone w pustym katalogu roboczym przed
  uruchomieniem; ``{"ścieżka": "treść"}``; ścieżka zakończona ``/`` tworzy pusty
  katalog; treść może też mieć postać ``{"repeat": "x", "times": 12000}``,
* ``expected_files`` — opcjonalnie: stan plików po uruchomieniu;
  ``{"ścieżka": "treść"}`` albo ``{"ścieżka": None}`` (plik ma nie istnieć).

Zasady porównywania wyjścia:

* końcowe spacje w liniach i puste linie na końcu są ignorowane,
* liczba linii musi się zgadzać,
* tekst w linii musi być identyczny, a liczby zmiennoprzecinkowe mogą różnić się
  o 0.01 (lub względnie o 1e-9), więc ``3`` == ``3.0`` i ``0.333`` == ``0.3333``;
  dwie liczby całkowite muszą być zapisane identycznie (``010`` != ``10``),
* tekst przekazany do ``input("…")`` nie jest wypisywany ani sprawdzany.
"""

import builtins
import io
import json
import linecache
import os
import re
import shutil
import sys
import tempfile
import traceback

MAX_OUTPUT = 20000
ABS_TOL = 0.01
REL_TOL = 1e-9
FILENAME = "main.py"

_NUMBER = re.compile(r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?")


def normalize(text):
    """Ujednolica końce linii, usuwa końcowe spacje i puste linie na końcu."""
    text = str(text if text is not None else "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    return lines


def _close(a, b):
    diff = abs(a - b)
    return diff <= ABS_TOL or diff <= REL_TOL * max(abs(a), abs(b))


def same_line(got, want):
    if got == want:
        return True
    if _NUMBER.sub("#", got) != _NUMBER.sub("#", want):
        return False
    for a, b in zip(_NUMBER.findall(got), _NUMBER.findall(want)):
        if a == b:
            continue
        if not (_is_float(a) or _is_float(b)):
            return False  # liczby całkowite muszą być identyczne: "010" != "10"
        try:
            if not _close(float(a), float(b)):
                return False
        except (ValueError, OverflowError):
            return False
    return True


def _is_float(token):
    return any(char in token for char in ".eE")


def same_output(output, expected):
    got, want = normalize(output), normalize(expected)
    return len(got) == len(want) and all(same_line(a, b) for a, b in zip(got, want))


def _error(exc):
    frames = [
        frame
        for frame in traceback.extract_tb(exc.__traceback__)
        if frame.filename == FILENAME
    ]
    line = frames[-1].lineno if frames else None
    if isinstance(exc, SyntaxError) and exc.filename == FILENAME:
        line = exc.lineno
    text = "".join(traceback.format_list(frames))
    if text:
        text = "Traceback (most recent call last):\n" + text
    text += "".join(traceback.format_exception_only(type(exc), exc))
    return {
        "type": type(exc).__name__,
        "message": exc.msg if isinstance(exc, SyntaxError) else str(exc),
        "line": line,
        "traceback": text.rstrip(),
    }


def _file_content(spec):
    if isinstance(spec, dict):
        return str(spec.get("repeat", "")) * int(spec.get("times", 1))
    return str(spec)


def _prepare_files(root, files):
    for rel, spec in sorted((files or {}).items()):
        path = os.path.join(root, rel)
        if rel.endswith("/"):
            os.makedirs(path, exist_ok=True)
            continue
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(_file_content(spec))


def _read_file(path):
    if not os.path.isfile(path):
        return None
    try:
        with open(path, "r", encoding="utf-8", newline="") as handle:
            return handle.read()
    except (OSError, UnicodeDecodeError):
        return None


def _check_files(root, expected_files):
    report = []
    for rel, want in sorted((expected_files or {}).items()):
        got = _read_file(os.path.join(root, rel))
        if want is None:
            ok = not os.path.exists(os.path.join(root, rel))
        else:
            ok = got is not None and same_output(got, _file_content(want))
        report.append({"path": rel, "expected": want, "got": got, "ok": ok})
    return report


def run_case(compiled, case):
    stdin = io.StringIO(case.get("input") or "")
    stdout = io.StringIO()
    stderr = io.StringIO()

    def _input(prompt=""):
        line = stdin.readline()
        if not line:
            raise EOFError("EOF when reading a line")
        return line.rstrip("\r\n")

    uses_files = "files" in case or "expected_files" in case
    previous_dir = os.getcwd()
    workdir = tempfile.mkdtemp(prefix="zadanie-") if uses_files else None

    saved = (sys.stdin, sys.stdout, sys.stderr, builtins.input)
    error = None
    try:
        if workdir:
            _prepare_files(workdir, case.get("files"))
            os.chdir(workdir)
        sys.stdin, sys.stdout, sys.stderr, builtins.input = (
            stdin,
            stdout,
            stderr,
            _input,
        )
        exec(compiled, {"__name__": "__main__", "__builtins__": builtins})
    except SystemExit:
        pass
    except BaseException as exc:  # noqa: B902 - błąd ucznia ma trafić do raportu
        error = _error(exc)
    finally:
        sys.stdin, sys.stdout, sys.stderr, builtins.input = saved

    files = None
    try:
        if workdir and "expected_files" in case:
            files = _check_files(workdir, case["expected_files"])
    finally:
        os.chdir(previous_dir)
        if workdir:
            shutil.rmtree(workdir, ignore_errors=True)

    output = stdout.getvalue()
    result = {
        "output": output[:MAX_OUTPUT],
        "truncated": len(output) > MAX_OUTPUT,
        "stderr": stderr.getvalue()[:MAX_OUTPUT],
        "error": error,
    }
    if files is not None:
        result["files"] = files
    if case.get("expected") is not None or files is not None:
        ok = error is None
        if case.get("expected") is not None:
            ok = ok and same_output(output, case["expected"])
        if files is not None:
            ok = ok and all(item["ok"] for item in files)
        result["ok"] = ok
    return result


def run(code, cases):
    """Kompiluje ``code`` i uruchamia go na liście przypadków ``cases``."""
    linecache.cache[FILENAME] = (len(code), None, code.splitlines(True), FILENAME)
    try:
        compiled = compile(code, FILENAME, "exec")
    except SyntaxError as exc:
        return {"compile_error": _error(exc)}
    return {"results": [run_case(compiled, case) for case in cases]}


def _pyk_run(code, cases_json):
    """Punkt wejścia dla przeglądarki (judge-worker.js): JSON na wejściu i wyjściu."""
    return json.dumps(run(code, json.loads(cases_json)), ensure_ascii=False)
