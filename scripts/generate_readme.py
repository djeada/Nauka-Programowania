#!/usr/bin/env python3
"""
Generuje indeks zadań i statystyki w README.md na podstawie zbior_zadan_json/.

Fragmenty README pomiędzy znacznikami
    <!-- ZADANIA:START --> … <!-- ZADANIA:END -->
    <!-- STATYSTYKI:START --> … <!-- STATYSTYKI:END -->
są w całości nadpisywane. Linki do rozwiązań powstają tylko dla plików, które
istnieją, więc README nie może zawierać martwych linków do kodu.

Użycie:
    python3 scripts/generate_readme.py           # zaktualizuj README.md
    python3 scripts/generate_readme.py --check   # zakończ błędem, jeśli README jest nieaktualne (CI)
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"
JSON_DIR = REPO_ROOT / "zbior_zadan_json"
COURSE_URL = "https://adamdjellouli.com/courses/kurs_podstaw_pythona/"

LANGUAGES = [
    ("Python", "python", "py"),
    ("C++", "cpp", "cpp"),
    ("Java", "java", "java"),
    ("JavaScript", "js", "js"),
    ("Bash", "bash", "sh"),
    ("Haskell", "haskell", "hs"),
    ("Rust", "rust", "rs"),
]


def chapter_name(title: str) -> str:
    return re.sub(r"^Rozdział(\s+\d+)?\s*:\s*", "", title.strip()) or title.strip()


def github_anchor(heading: str) -> str:
    slug = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return slug.replace(" ", "-")


def course_slug(slug: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", slug.lower()).strip("_")


def solution_path(chapter: str, task_id: str, folder: str, ext: str) -> Optional[str]:
    number, letter = task_id[4:6], task_id[6:].lower()
    base = REPO_ROOT / "src" / folder / chapter
    if folder == "java":
        candidates = [base / f"zad{int(number)}" / "Main.java"]
    elif folder == "python":
        candidates = [base / f"zad{number}{letter}.py", base / f"zad{number}.py"]
    else:
        candidates = [base / f"zad{number}{letter}.{ext}", base / f"zad{number}.{ext}"]
    for path in candidates:
        if path.exists():
            return path.relative_to(REPO_ROOT).as_posix()
    return None


def plural(n: int) -> str:
    if n == 1:
        return "zadanie"
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return "zadania"
    return "zadań"


def load() -> List[Dict]:
    return [
        json.loads(p.read_text(encoding="utf-8"))
        for p in sorted(JSON_DIR.glob("*.json"))
    ]


def render_index(chapters: List[Dict]) -> str:
    out = [
        "<!-- Sekcja generowana przez scripts/generate_readme.py — nie edytuj jej ręcznie. -->",
        "",
        f"Każde zadanie możesz też **rozwiązać online w przeglądarce** z automatyczną sprawdzarką: "
        f"[Kurs Podstaw Pythona]({COURSE_URL}).",
        "",
    ]
    headings = []
    for number, chapter in enumerate(chapters, start=1):
        heading = f"Rozdział {number}: {chapter_name(chapter['chapter_title'])}"
        headings.append(heading)
        count = len(chapter["exercises"])
        out.append(
            f"{number}. [{chapter_name(chapter['chapter_title'])}](#{github_anchor(heading)}) — {count} {plural(count)}"
        )
    out.append("")

    for number, (chapter, heading) in enumerate(zip(chapters, headings), start=1):
        stem = chapter["file"][:-3]
        out += [
            f"### {heading}",
            "",
            f"📄 [Treści zadań](zbior_zadan/{chapter['file']}) · "
            f"🧪 [Testy](zbior_zadan_tests/{stem}.json) · "
            f"▶️ [Rozwiąż online]({COURSE_URL}#rozdzial-{number})",
            "",
            "<table>",
            "    <thead>",
            "        <tr><th>Nr</th><th>Zadanie</th><th>Rozwiązania</th><th>Poziom</th></tr>",
            "    </thead>",
            "    <tbody>",
        ]
        for exercise in chapter["exercises"]:
            links = []
            for label, folder, ext in LANGUAGES:
                path = solution_path(stem, exercise["id"], folder, ext)
                if path:
                    links.append(f'<a href="{path}">{label}</a>')
            task_url = f"{COURSE_URL}tasks/{course_slug(exercise['slug'])}.html"
            title = exercise["title"].replace("<", "&lt;")
            out.append(
                f"        <tr><td>{exercise['id'][4:]}</td>"
                f'<td><a href="{task_url}">{title}</a></td>'
                f"<td>{' · '.join(links) or '—'}</td>"
                f"<td>{exercise['difficulty_display']}</td></tr>"
            )
        out += ["    </tbody>", "</table>", ""]
    return "\n".join(out)


def render_stats(chapters: List[Dict]) -> str:
    tasks = sum(len(c["exercises"]) for c in chapters)
    tests = sum(len(e["testcases"]) for c in chapters for e in c["exercises"])
    return "\n".join(
        [
            "| 📚 Rozdziały | 📝 Zadania | 🧪 Testy automatyczne | 💻 Języki | ⭐ Poziomy trudności |",
            "|:------------:|:----------:|:---------------------:|:---------:|:--------------------:|",
            f"| **{len(chapters)}** | **{tasks}** | **{tests}** | **{len(LANGUAGES)}** | **3** |",
        ]
    )


def replace_block(text: str, name: str, content: str) -> str:
    pattern = re.compile(rf"<!-- {name}:START -->.*?<!-- {name}:END -->", re.S)
    if not pattern.search(text):
        raise SystemExit(
            f"README.md nie zawiera znaczników <!-- {name}:START --> / <!-- {name}:END -->"
        )
    block = f"<!-- {name}:START -->\n{content}\n<!-- {name}:END -->"
    return pattern.sub(lambda _: block, text, count=1)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    chapters = load()
    current = README.read_text(encoding="utf-8")
    updated = replace_block(current, "ZADANIA", render_index(chapters))
    updated = replace_block(updated, "STATYSTYKI", render_stats(chapters))

    if args.check:
        if updated != current:
            print(
                "✗ README.md jest nieaktualne. Uruchom: python3 scripts/generate_readme.py",
                file=sys.stderr,
            )
            return 1
        print("✓ README.md jest aktualne.")
        return 0
    README.write_text(updated, encoding="utf-8")
    print(
        f"✓ Zaktualizowano README.md ({sum(len(c['exercises']) for c in chapters)} zadań)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
