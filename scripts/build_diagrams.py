#!/usr/bin/env python3
"""
Buduje diagramy podręcznika: podrecznik/diagramy/*.tex (TikZ) -> podrecznik/diagramy/svg/*.svg.

Każdy plik *.tex zawiera jedno środowisko tikzpicture; skrypt dokleja do niego wspólną
preambułę (podrecznik/diagramy/preambula.tex), kompiluje go `latex`-em do DVI i zamienia
`dvisvgm --no-fonts` na SVG (litery jako krzywe — plik wygląda wszędzie tak samo: w PDF-ie,
na GitHubie, w przeglądarce).

Pliki SVG są commitowane, więc do złożenia PDF-u ani do CI nie potrzeba TeX-a. W każdym SVG
jest skrót źródła (<!-- zrodlo:... -->); `--check` porównuje go ze źródłem bez kompilacji.

Użycie:
    python3 scripts/build_diagrams.py              # zbuduj nowe i zmienione diagramy
    python3 scripts/build_diagrams.py 04_petla     # tylko pliki zaczynające się od prefiksu
    python3 scripts/build_diagrams.py --force      # zbuduj wszystko od nowa
    python3 scripts/build_diagrams.py --check      # CI: czy każde SVG jest aktualne (bez TeX-a)

Wymagania (tylko do budowania): latex (TeX Live: texlive-latex-extra, texlive-pictures,
texlive-fonts-extra dla pakietu arev) i dvisvgm.
"""

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
DIAGRAMS_DIR = REPO_ROOT / "podrecznik" / "diagramy"
SVG_DIR = DIAGRAMS_DIR / "svg"
PREAMBLE = DIAGRAMS_DIR / "preambula.tex"
STAMP = re.compile(r"<!-- zrodlo:([0-9a-f]{16})\b")


def sources(prefixes: List[str]) -> List[Path]:
    files = sorted(p for p in DIAGRAMS_DIR.glob("*.tex") if p != PREAMBLE)
    if prefixes:
        files = [p for p in files if any(p.stem.startswith(x) for x in prefixes)]
    return files


def document(body: str) -> str:
    return (
        "\\documentclass[tikz,border=3pt]{standalone}\n"
        + PREAMBLE.read_text(encoding="utf-8")
        + "\n\\begin{document}\n"
        + body.strip()
        + "\n\\end{document}\n"
    )


def digest(tex: Path) -> str:
    return hashlib.sha256(
        document(tex.read_text(encoding="utf-8")).encode()
    ).hexdigest()[:16]


def svg_path(tex: Path) -> Path:
    return SVG_DIR / f"{tex.stem}.svg"


def is_current(tex: Path) -> bool:
    svg = svg_path(tex)
    if not svg.exists():
        return False
    match = STAMP.search(svg.read_text(encoding="utf-8")[:2000])
    return bool(match) and match.group(1) == digest(tex)


def latex_error(log: str) -> str:
    lines = log.splitlines()
    for n, line in enumerate(lines):
        if line.startswith("!"):
            return "\n".join(lines[n : n + 6])
    return "\n".join(lines[-15:])


def build(tex: Path) -> Tuple[Path, Optional[str]]:
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        (work / "d.tex").write_text(
            document(tex.read_text(encoding="utf-8")), encoding="utf-8"
        )
        run = subprocess.run(
            ["latex", "-interaction=nonstopmode", "-halt-on-error", "d.tex"],
            cwd=work,
            capture_output=True,
            text=True,
            errors="replace",
        )
        if run.returncode != 0 or not (work / "d.dvi").exists():
            log = (
                (work / "d.log").read_text(errors="replace")
                if (work / "d.log").exists()
                else run.stdout
            )
            return tex, latex_error(log)
        run = subprocess.run(
            [
                "dvisvgm",
                "--no-fonts",
                "--exact-bbox",
                "--optimize",
                "-o",
                "d.svg",
                "d.dvi",
            ],
            cwd=work,
            capture_output=True,
            text=True,
            errors="replace",
        )
        if run.returncode != 0 or not (work / "d.svg").exists():
            return tex, run.stderr.strip()[-800:]
        svg = (work / "d.svg").read_text(encoding="utf-8")
        stamp = f"<!-- zrodlo:{digest(tex)} (wygenerowane z {tex.name}, nie edytuj ręcznie) -->"
        svg = re.sub(r"(<svg\b)", stamp + "\n\\1", svg, count=1)
        svg_path(tex).write_text(svg, encoding="utf-8")
    return tex, None


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "prefixes", nargs="*", help="tylko diagramy o nazwach z tym prefiksem"
    )
    parser.add_argument(
        "--check", action="store_true", help="sprawdź aktualność SVG (bez kompilacji)"
    )
    parser.add_argument(
        "--force", action="store_true", help="buduj także aktualne diagramy"
    )
    args = parser.parse_args()

    texs = sources(args.prefixes)
    known = {svg_path(t).name for t in sources([])}
    orphans = sorted(p.name for p in SVG_DIR.glob("*.svg") if p.name not in known)

    if args.check:
        stale = [t.name for t in texs if not is_current(t)]
        for name in stale:
            print(
                f"✗ {name}: brak SVG albo SVG nieaktualne — uruchom scripts/build_diagrams.py"
            )
        for name in orphans:
            print(f"✗ svg/{name}: brak pliku źródłowego .tex")
        if stale or orphans:
            return 1
        print(f"✓ {len(texs)} diagramów jest aktualnych.")
        return 0

    for tool in ("latex", "dvisvgm"):
        if not shutil.which(tool):
            print(
                f"Brak programu {tool!r} — zainstaluj TeX Live i dvisvgm.",
                file=sys.stderr,
            )
            return 1
    SVG_DIR.mkdir(parents=True, exist_ok=True)
    todo = [t for t in texs if args.force or not is_current(t)]
    failed = 0
    with ThreadPoolExecutor() as pool:
        for tex, error in pool.map(build, todo):
            if error:
                failed += 1
                print(f"✗ {tex.name}\n{error}\n")
            else:
                print(f"✓ {tex.name}")
    for name in orphans:
        print(
            f"Uwaga: svg/{name} nie ma źródła .tex (usuń je, jeśli jest niepotrzebne)."
        )
    print(
        f"Zbudowano {len(todo) - failed} z {len(todo)} (aktualnych: {len(texs) - len(todo)})."
    )
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
