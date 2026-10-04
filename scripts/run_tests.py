#!/usr/bin/env python3
"""
Sprawdza rozwiązania wzorcowe w Pythonie (src/python) na testach i przykładach.

Każde zadanie z zbior_zadan/*.md musi mieć rozwiązanie w pliku
src/python/<rozdział>/zadNN.py (lub zadNNa.py dla podpunktu ZAD-NNA), które
czyta standardowe wejście i przechodzi wszystkie testy z zbior_zadan_tests/
oraz wszystkie przykłady z treści. Porównanie wyników wykonuje
scripts/judge_harness.py — ten sam kod, który ocenia rozwiązania na stronie kursu.

Użycie:
    python3 scripts/run_tests.py                 # wszystkie rozdziały
    python3 scripts/run_tests.py 03 15           # wybrane rozdziały (prefiks nazwy)
    python3 scripts/run_tests.py 03 --task ZAD-07 -v
"""

import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import md_to_json  # noqa: E402

TIMEOUT = 20
RUNNER = """
import json, sys
sys.path.insert(0, sys.argv[1])
sys.setrecursionlimit(10000)
import judge_harness
code = open(sys.argv[2], encoding="utf-8").read()
cases = json.load(sys.stdin)
print(json.dumps(judge_harness.run(code, cases), ensure_ascii=False))
"""


def solution_path(chapter: str, task_id: str) -> Path:
    number, letter = task_id[4:6], task_id[6:].lower()
    return REPO_ROOT / "src" / "python" / chapter / f"zad{number}{letter}.py"


def cases_for(exercise: Dict[str, Any]) -> List[Tuple[str, Dict[str, Any]]]:
    cases = []
    for n, example in enumerate(exercise["examples"], start=1):
        case = {"input": example["input"], "expected": example["output"]}
        for key in ("files", "expected_files"):
            if key in example:
                case[key] = example[key]
        cases.append((f"przykład {n}", case))
    for n, test in enumerate(exercise["testcases"], start=1):
        case = {"input": test["input"], "expected": test["output"]}
        for key in ("files", "expected_files"):
            if key in test:
                case[key] = test[key]
        cases.append((f"test {n}", case))
    return cases


def run_solution(path: Path, cases: List[Dict[str, Any]]) -> Dict[str, Any]:
    try:
        proc = subprocess.run(
            [sys.executable, "-c", RUNNER, str(SCRIPTS), str(path)],
            input=json.dumps(cases),
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            cwd=REPO_ROOT,
        )
    except subprocess.TimeoutExpired:
        return {"fatal": f"przekroczono limit czasu ({TIMEOUT} s)"}
    try:
        return json.loads(proc.stdout.strip().splitlines()[-1])
    except (IndexError, json.JSONDecodeError):
        return {"fatal": (proc.stderr or proc.stdout).strip()[-500:] or "brak wyniku"}


def indent(text: str) -> str:
    return "\n".join("        " + line for line in str(text).split("\n"))


def check_task(
    chapter: str, exercise: Dict[str, Any], verbose: bool
) -> Tuple[str, List[str]]:
    task_id = exercise["id"]
    path = solution_path(chapter, task_id)
    rel = path.relative_to(REPO_ROOT)
    if not path.exists():
        return "MISSING", [f"brak pliku {rel}"]
    labelled = cases_for(exercise)
    if not exercise["testcases"]:
        labelled = [
            (label, case) for label, case in labelled if label.startswith("przykład")
        ]
        for _, case in labelled:
            case["expected"] = (
                None  # zadanie interaktywne: tylko sprawdź, że się uruchamia
            )
    result = run_solution(path, [case for _, case in labelled])
    if "fatal" in result:
        return "FAIL", [f"{rel}: {result['fatal']}"]
    if "compile_error" in result:
        err = result["compile_error"]
        return "FAIL", [f"{rel}:{err['line']}: {err['type']}: {err['message']}"]

    messages = []
    for (label, case), outcome in zip(labelled, result["results"]):
        if outcome.get("ok", outcome["error"] is None):
            continue
        lines = [f"{rel} — {label} niezaliczony"]
        if outcome["error"]:
            lines.append(indent(outcome["error"]["traceback"]))
        if verbose or not outcome["error"]:
            lines.append("      wejście:")
            lines.append(indent(case["input"]))
            if case.get("expected") is not None:
                lines.append("      oczekiwane:")
                lines.append(indent(case["expected"]))
            lines.append("      otrzymane:")
            lines.append(indent(outcome["output"]))
        for item in outcome.get("files") or []:
            if not item["ok"]:
                lines.append(
                    f"      plik {item['path']}: oczekiwano {item['expected']!r}, jest {item['got']!r}"
                )
        messages.append("\n".join(lines))
    return ("FAIL" if messages else "PASS"), messages


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "chapters", nargs="*", help="prefiksy rozdziałów, np. 03 albo 15_funkcje"
    )
    parser.add_argument(
        "--task", help="tylko zadanie o tym identyfikatorze, np. ZAD-05A"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="pokaż wejście/wyjście także przy błędach wykonania",
    )
    parser.add_argument("-j", "--jobs", type=int, default=8)
    args = parser.parse_args()

    problems = md_to_json.Problems()
    chapters = md_to_json.load_chapters(
        REPO_ROOT / "zbior_zadan",
        REPO_ROOT / "zbior_zadan_tests",
        ["szablon.md"],
        problems,
    )
    selected = {
        stem: data
        for stem, data in chapters.items()
        if not args.chapters or any(stem.startswith(prefix) for prefix in args.chapters)
    }
    jobs = [
        (stem, exercise)
        for stem, data in selected.items()
        for exercise in data["exercises"]
        if not args.task or exercise["id"] == args.task
    ]
    if not jobs:
        print("Nie znaleziono zadań do sprawdzenia.", file=sys.stderr)
        return 2

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        outcomes = list(
            pool.map(lambda job: check_task(job[0], job[1], args.verbose), jobs)
        )

    counts: Dict[str, int] = {}
    current: Optional[str] = None
    for (stem, exercise), (status, messages) in zip(jobs, outcomes):
        counts[status] = counts.get(status, 0) + 1
        if stem != current:
            current = stem
            print(f"\n{stem}")
        mark = {"PASS": "✓", "FAIL": "✗", "MISSING": "?"}[status]
        interactive = " (interaktywne)" if not exercise["testcases"] else ""
        print(f"  {mark} {exercise['id']} {exercise['title']}{interactive}")
        for message in messages:
            print("    " + message.replace("\n", "\n    "))

    total = len(jobs)
    print(f"\nZaliczone: {counts.get('PASS', 0)}/{total}", end="")
    if counts.get("FAIL"):
        print(f", niezaliczone: {counts['FAIL']}", end="")
    if counts.get("MISSING"):
        print(f", brak rozwiązania: {counts['MISSING']}", end="")
    print()
    return 0 if counts.get("PASS", 0) == total else 1


if __name__ == "__main__":
    sys.exit(main())
