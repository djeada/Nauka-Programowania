#!/usr/bin/env python3
"""
Konwertuje zbior_zadan/*.md (+ testy z zbior_zadan_tests/*.json) do zbior_zadan_json/*.json.

Pliki JSON są publicznym API zbioru zadań (korzysta z nich m.in. kurs na stronie
adamdjellouli.com), dlatego skrypt jest rygorystyczny: każda nierozpoznana sekcja,
zgubiony przykład albo brakujące testy kończą się błędem, zamiast cicho
produkować niepełne dane.

Użycie:
    python3 scripts/md_to_json.py            # wygeneruj pliki JSON
    python3 scripts/md_to_json.py --check    # sprawdź, czy commitowane JSON-y są aktualne (CI)

Schemat pliku JSON:
{
  "file": "02_instrukcja_warunkowa.md",
  "chapter_title": "Rozdział 2: Instrukcja warunkowa",
  "chapter_description": "markdown",
  "exercises": [
    {
      "id": "ZAD-02",                       # ^ZAD-\\d{2}[A-Z]?$
      "slug": "02_instrukcja_warunkowa/ZAD-02",
      "title": "Porównanie dwóch liczb",
      "difficulty": 1,                      # 1..3
      "difficulty_display": "★☆☆",
      "tags": ["if"],
      "description": "markdown, wzory w $...$",
      "input": "markdown",
      "output": "markdown",
      "examples": [{"input": "7\\n4", "output": "Liczby są różne.", "explanation": ""}],
      "testcases": [{"input": "9\\n9", "output": "Liczby są identyczne."}],
      "constraints": "markdown",
      "notes": "markdown",
      "starter_code": "kod startowy w Pythonie lub pusty napis"
    }
  ]
}

Przypadek testowy może dodatkowo zawierać "files" i "expected_files"
(zob. scripts/judge_harness.py). Pusta lista testów oznacza zadanie interaktywne
(bez automatycznej oceny).
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent

EXERCISE_HEADER = re.compile(r"^##\s+(ZAD-\d{2}[A-Z]?)\s+[—-]\s+(.+?)\s*$")
TASK_ID = re.compile(r"^ZAD-\d{2}[A-Z]?$")
DIFFICULTY = re.compile(r"[★☆]+")
TAG = re.compile(r"`([^`]+)`")
INPUT_MARKER = re.compile(r"^\*\*(Wejście|Dane wejściowe)[^*]*:\*\*\s*(.*)$")
OUTPUT_MARKER = re.compile(
    r"^\*\*(Wyjście|Oczekiwane wyjście|Dane wyjściowe)[^*]*:\*\*\s*(.*)$"
)
FILES_BEFORE_MARKER = re.compile(r"^\*\*Pliki przed:\*\*\s*(.*)$")
FILES_AFTER_MARKER = re.compile(r"^\*\*Pliki po:\*\*\s*(.*)$")
FILE_SIZE = re.compile(r"^(.*?)\s+\(rozmiar:\s*(\d+)\s*B\)$")
FORBIDDEN_MARKER = re.compile(r"^\*\*(Wywołanie funkcji|Wywołanie)[^*]*:\*\*")
EMPTY_MARKER = re.compile(r"^\*?\(?\s*brak\s*\)?\*?\.?$", re.IGNORECASE)

# Nagłówek sekcji (### ...) -> pole JSON. Dopasowanie po prefiksie, więc
# "Uwagi o formatowaniu" trafia do notes, a "Przykład 2" do examples.
SECTION_PREFIXES: List[Tuple[str, str]] = [
    ("Treść", "description"),
    ("Wejście", "input"),
    ("Wyjście", "output"),
    ("Ograniczenia", "constraints"),
    ("Gwarancje", "constraints"),
    ("Przykład", "examples"),
    ("Uwagi", "notes"),
    ("Wskazówki", "notes"),
    ("Kod startowy", "starter_code"),
]
MULTI_SECTION_FIELDS = {"notes", "constraints"}


class Problems:
    def __init__(self) -> None:
        self.items: List[str] = []

    def add(self, where: str, message: str) -> None:
        self.items.append(f"{where}: {message}")


def section_field(heading: str) -> Optional[str]:
    for prefix, field in SECTION_PREFIXES:
        if heading.startswith(prefix):
            return field
    return None


def clean_text(lines: List[str]) -> str:
    text = "\n".join(line.rstrip() for line in lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def read_code_block(lines: List[str], i: int) -> Tuple[str, int]:
    """Zwraca zawartość bloku ``` zaczynającego się w linii i oraz indeks za blokiem."""
    body = []
    i += 1
    while i < len(lines) and not lines[i].strip().startswith("```"):
        body.append(lines[i].rstrip())
        i += 1
    return "\n".join(body), i + 1


def parse_file_tree(
    code: str, expected: bool, where: str, problems: Problems
) -> Dict[str, Any]:
    """
    Czyta opis plików z przykładu:

        dane/notatki.txt        <- ścieżka pliku
        | Ala ma kota           <- kolejne linie treści (prefiks "| ")
        dane/pusty.txt          <- pusty plik
        archiwum/               <- pusty katalog
        duzy.bin (rozmiar: 12000 B)
        stary.txt (usunięty)    <- tylko w "Pliki po:": plik ma nie istnieć
    """
    files: Dict[str, Any] = {}
    current: Optional[str] = None
    for raw in code.split("\n"):
        if raw.startswith("|"):
            if current is None or not isinstance(files[current], str):
                problems.add(where, f"linia treści pliku bez ścieżki: {raw!r}")
                continue
            files[current] += raw[2:] + "\n" if raw.startswith("| ") else "\n"
            continue
        line = raw.strip()
        if not line:
            continue
        size = FILE_SIZE.match(line)
        if expected and line.endswith("(usunięty)"):
            files[line[: -len("(usunięty)")].strip()] = None
            current = None
        elif size:
            files[size.group(1).strip()] = {"repeat": "x", "times": int(size.group(2))}
            current = None
        elif line.endswith("/"):
            if expected:
                problems.add(where, "w 'Pliki po:' podawaj pliki, nie katalogi")
            files[line] = ""
            current = None
        else:
            files[line] = ""
            current = line
    return files


def parse_examples(
    lines: List[str], where: str, problems: Problems
) -> List[Dict[str, str]]:
    examples: List[Dict[str, str]] = []
    current: Dict[str, Any] = {}
    state: Optional[str] = None
    prose: List[str] = []

    def flush() -> None:
        nonlocal current, prose
        if "output" in current:
            example = {
                "input": current.get("input", ""),
                "output": current["output"],
                "explanation": clean_text(prose),
            }
            for key in ("files", "expected_files"):
                if key in current:
                    example[key] = current[key]
            examples.append(example)
        elif current:
            problems.add(where, "przykład ma wejście, ale nie ma wyjścia")
        current, prose = {}, []

    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if FORBIDDEN_MARKER.match(stripped):
            problems.add(
                where,
                f"niedozwolony znacznik {stripped!r} — przykład musi pokazywać "
                "**Wejście:** i **Wyjście:** programu (stdin/stdout)",
            )
            state = None
            i += 1
            continue
        match_in = INPUT_MARKER.match(stripped)
        match_out = OUTPUT_MARKER.match(stripped)
        match_before = FILES_BEFORE_MARKER.match(stripped)
        match_after = FILES_AFTER_MARKER.match(stripped)
        if match_before or match_after:
            if match_before and current:
                flush()
            state = "files" if match_before else "expected_files"
            if EMPTY_MARKER.match(
                (match_before or match_after).group(1).strip() or "x"
            ):
                current[state] = {}
                state = None
            i += 1
            continue
        if match_in:
            if "input" in current or "output" in current:
                flush()
            state = "input"
            if EMPTY_MARKER.match(match_in.group(2).strip()):
                current["input"] = ""
                state = None
            i += 1
            continue
        if match_out:
            if "output" in current:
                flush()
            state = "output"
            rest = match_out.group(2).strip()
            if rest and EMPTY_MARKER.match(rest):
                current["output"] = ""
                state = None
            i += 1
            continue
        if stripped.startswith("```"):
            code, i = read_code_block(lines, i)
            if state == "input":
                current["input"] = code
            elif state == "output":
                current["output"] = code
            elif state in ("files", "expected_files"):
                current[state] = parse_file_tree(
                    code, state == "expected_files", where, problems
                )
            else:
                problems.add(
                    where,
                    "blok kodu w przykładzie bez znacznika **Wejście:**/**Wyjście:**",
                )
            state = None
            continue
        if stripped and stripped != "---":
            prose.append(lines[i])
        i += 1
    flush()
    return examples


def parse_exercise(
    lines: List[str], start: int, stem: str, problems: Problems
) -> Tuple[Dict[str, Any], int]:
    header = EXERCISE_HEADER.match(lines[start])
    task_id, title = header.group(1), header.group(2)
    where = f"{stem}/{task_id}"
    exercise: Dict[str, Any] = {
        "id": task_id,
        "slug": f"{stem}/{task_id}",
        "title": title,
        "difficulty": 0,
        "difficulty_display": "",
        "tags": [],
        "description": "",
        "input": "",
        "output": "",
        "examples": [],
        "testcases": [],
        "constraints": "",
        "notes": "",
        "starter_code": "",
    }

    i = start + 1
    sections: List[Tuple[str, List[str]]] = []
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if EXERCISE_HEADER.match(line) or re.match(r"^#{1,2}\s", line):
            break
        if stripped.startswith("**Poziom:**"):
            stars = DIFFICULTY.search(stripped)
            display = stars.group(0) if stars else ""
            exercise["difficulty_display"] = display
            exercise["difficulty"] = display.count("★")
        elif stripped.startswith("**Tagi:**"):
            exercise["tags"] = TAG.findall(stripped)
        elif stripped.startswith("### "):
            sections.append((stripped[4:].strip(), []))
        elif sections:
            if stripped.startswith("```"):
                block_end = i + 1
                while block_end < len(lines) and not lines[
                    block_end
                ].strip().startswith("```"):
                    block_end += 1
                sections[-1][1].extend(lines[i : block_end + 1])
                i = block_end + 1
                continue
            if stripped != "---":
                sections[-1][1].append(line)
        elif stripped and stripped != "---":
            problems.add(where, f"tekst poza sekcją: {stripped[:60]!r}")
        i += 1

    for heading, body in sections:
        field = section_field(heading)
        if field is None:
            problems.add(where, f"nieznana sekcja '### {heading}'")
            continue
        if field == "examples":
            exercise["examples"].extend(parse_examples(body, where, problems))
        elif field == "starter_code":
            code_start = next(
                (n for n, l in enumerate(body) if l.strip().startswith("```")), None
            )
            if code_start is None:
                problems.add(
                    where, "sekcja 'Kod startowy' musi zawierać blok ```python"
                )
            else:
                exercise["starter_code"] = read_code_block(body, code_start)[0] + "\n"
        else:
            text = clean_text(body)
            label_needed = field in MULTI_SECTION_FIELDS and heading not in (
                "Uwagi",
                "Ograniczenia",
            )
            if label_needed and text:
                text = f"**{heading}:**\n\n{text}"
            if exercise[field] and field in MULTI_SECTION_FIELDS:
                exercise[field] += "\n\n" + text
            elif exercise[field]:
                problems.add(where, f"sekcja '{heading}' powtórzona")
            else:
                exercise[field] = text

    for field in ("description", "input", "output"):
        if not exercise[field]:
            problems.add(where, f"brak sekcji {field!r}")
    if not exercise["examples"]:
        problems.add(where, "brak przykładu")
    if exercise["difficulty_display"] and len(exercise["difficulty_display"]) != 3:
        problems.add(
            where,
            f"poziom trudności musi mieć 3 znaki: {exercise['difficulty_display']!r}",
        )
    if not 1 <= exercise["difficulty"] <= 3:
        problems.add(where, "brak lub zły **Poziom:** (★☆☆ … ★★★)")
    if not exercise["tags"]:
        problems.add(where, "brak **Tagi:**")
    return exercise, i


def validate_testcases(
    where: str, cases: Any, problems: Problems
) -> List[Dict[str, Any]]:
    if not isinstance(cases, list):
        problems.add(where, "testy muszą być listą")
        return []
    seen = set()
    for n, case in enumerate(cases, start=1):
        if not isinstance(case, dict) or "input" not in case or "output" not in case:
            problems.add(where, f"test {n}: wymagane pola 'input' i 'output'")
            continue
        extra = set(case) - {"input", "output", "files", "expected_files"}
        if extra:
            problems.add(where, f"test {n}: nieznane pola {sorted(extra)}")
        key = json.dumps(case, sort_keys=True, ensure_ascii=False)
        if key in seen:
            problems.add(where, f"test {n} jest duplikatem wcześniejszego testu")
        seen.add(key)
    return cases


MIN_TESTS = 4


def check_test_strength(
    where: str, exercise: Dict[str, Any], problems: Problems
) -> None:
    cases = [c for c in exercise["testcases"] if isinstance(c, dict) and "input" in c]
    if not cases:
        return  # zadanie interaktywne
    no_input = all(
        not (c.get("input") or "").strip() and "files" not in c for c in cases
    )
    minimum = 1 if no_input else MIN_TESTS
    if len(cases) < minimum:
        problems.add(where, f"za mało testów: {len(cases)} (minimum {minimum})")
    if any("files" in c for c in cases):
        for n, example in enumerate(exercise["examples"], start=1):
            if "files" not in example:
                problems.add(
                    where,
                    f"przykład {n}: zadanie na plikach — dodaj **Pliki przed:** (i ewentualnie **Pliki po:**)",
                )
    example_inputs = {
        ex["input"].strip() for ex in exercise["examples"] if ex["input"].strip()
    }
    for n, case in enumerate(cases, start=1):
        if "files" not in case and (case.get("input") or "").strip() in example_inputs:
            problems.add(where, f"test {n} powtarza wejście z przykładu")


def parse_markdown_file(
    path: Path, tests_map: Optional[Dict[str, Any]], problems: Problems
) -> Dict[str, Any]:
    lines = path.read_text(encoding="utf-8").split("\n")
    stem = path.stem
    result: Dict[str, Any] = {
        "file": path.name,
        "chapter_title": "",
        "chapter_description": "",
        "exercises": [],
    }

    i = 0
    while i < len(lines) and not re.match(r"^#\s", lines[i]):
        i += 1
    if i == len(lines):
        problems.add(stem, "brak tytułu rozdziału (# ...)")
        return result
    result["chapter_title"] = lines[i][2:].strip()
    i += 1
    description = []
    while i < len(lines) and not EXERCISE_HEADER.match(lines[i]):
        if re.match(r"^#{1,2}\s", lines[i]):
            problems.add(
                stem, f"nieoczekiwany nagłówek przed pierwszym zadaniem: {lines[i]!r}"
            )
        elif lines[i].strip() != "---":
            description.append(lines[i])
        i += 1
    result["chapter_description"] = clean_text(description)

    while i < len(lines):
        if EXERCISE_HEADER.match(lines[i]):
            exercise, i = parse_exercise(lines, i, stem, problems)
            result["exercises"].append(exercise)
        else:
            if re.match(r"^#{1,2}\s", lines[i]):
                problems.add(stem, f"nieoczekiwany nagłówek: {lines[i]!r}")
            i += 1

    ids = [ex["id"] for ex in result["exercises"]]
    duplicates = sorted({x for x in ids if ids.count(x) > 1})
    if duplicates:
        problems.add(stem, f"powtórzone identyfikatory zadań: {duplicates}")

    tests_map = tests_map or {}
    for exercise in result["exercises"]:
        where = f"{stem}/{exercise['id']}"
        if exercise["id"] not in tests_map:
            problems.add(
                where,
                "brak wpisu w zbior_zadan_tests (pusta lista = zadanie interaktywne)",
            )
            continue
        cases = validate_testcases(where, tests_map[exercise["id"]], problems)
        exercise["testcases"] = cases
        check_test_strength(where, exercise, problems)
    for key in sorted(set(tests_map) - set(ids)):
        problems.add(stem, f"testy dla nieistniejącego zadania {key}")
    return result


def load_chapters(
    input_dir: Path,
    tests_dir: Path,
    exclude: List[str],
    problems: Problems,
    prefixes: Optional[List[str]] = None,
) -> Dict[str, Dict[str, Any]]:
    chapters = {}
    for md_file in sorted(input_dir.glob("*.md")):
        if md_file.name in exclude:
            continue
        if prefixes and not any(md_file.stem.startswith(prefix) for prefix in prefixes):
            continue
        tests_file = tests_dir / f"{md_file.stem}.json"
        tests_map = None
        if tests_file.exists():
            tests_map = json.loads(tests_file.read_text(encoding="utf-8"))
        else:
            problems.add(
                md_file.stem,
                f"brak pliku z testami {tests_file.relative_to(REPO_ROOT)}",
            )
        chapters[md_file.stem] = parse_markdown_file(md_file, tests_map, problems)
    return chapters


def render(chapter: Dict[str, Any]) -> str:
    return json.dumps(chapter, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--input-dir", default="zbior_zadan")
    parser.add_argument("--output-dir", default="zbior_zadan_json")
    parser.add_argument("--tests-dir", default="zbior_zadan_tests")
    parser.add_argument("--exclude", nargs="*", default=["szablon.md"])
    parser.add_argument(
        "--check",
        action="store_true",
        help="nie zapisuj; zakończ błędem, jeśli JSON-y są nieaktualne",
    )
    parser.add_argument(
        "--lenient", action="store_true", help="wypisz problemy, ale nie kończ błędem"
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="tylko walidacja treści i testów, bez zapisu",
    )
    parser.add_argument(
        "--chapters",
        nargs="*",
        help="ogranicz do rozdziałów o tych prefiksach (np. 03 15)",
    )
    args = parser.parse_args()

    input_dir = REPO_ROOT / args.input_dir
    output_dir = REPO_ROOT / args.output_dir
    tests_dir = REPO_ROOT / args.tests_dir
    problems = Problems()
    chapters = load_chapters(
        input_dir, tests_dir, args.exclude, problems, args.chapters
    )
    if args.chapters and not args.validate:
        parser.error(
            "--chapters działa tylko z --validate (JSON generujemy zawsze w całości)"
        )

    for item in problems.items:
        print(f"✗ {item}", file=sys.stderr)
    if problems.items and not args.lenient:
        print(f"\n{len(problems.items)} problem(ów) w zbiorze zadań.", file=sys.stderr)
        return 1

    if args.validate:
        total = sum(len(ch["exercises"]) for ch in chapters.values())
        print(f"✓ {len(chapters)} rozdziałów, {total} zadań — bez problemów.")
        return 0

    expected = {f"{stem}.json": render(chapter) for stem, chapter in chapters.items()}
    if args.check:
        stale = [
            name
            for name, text in expected.items()
            if not (output_dir / name).exists()
            or (output_dir / name).read_text(encoding="utf-8") != text
        ]
        extra = sorted(
            p.name for p in output_dir.glob("*.json") if p.name not in expected
        )
        for name in stale:
            print(f"✗ {args.output_dir}/{name} jest nieaktualny", file=sys.stderr)
        for name in extra:
            print(
                f"✗ {args.output_dir}/{name} nie ma odpowiednika w {args.input_dir}/",
                file=sys.stderr,
            )
        if stale or extra:
            print("\nUruchom: python3 scripts/md_to_json.py", file=sys.stderr)
            return 1
        print(f"✓ {len(expected)} plików JSON jest aktualnych.")
        return 0

    output_dir.mkdir(exist_ok=True)
    for name, text in expected.items():
        (output_dir / name).write_text(text, encoding="utf-8")
    total = sum(len(ch["exercises"]) for ch in chapters.values())
    print(
        f"✓ Zapisano {len(expected)} plików JSON ({total} zadań) w {args.output_dir}/"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
