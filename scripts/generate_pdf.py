#!/usr/bin/env python3
"""
Składa zbiór zadań (zbior_zadan/*.md) w jeden PDF gotowy do druku i do czytania na ekranie.

Treści są czytane tym samym parserem co w md_to_json.py, więc PDF pokazuje dokładnie
to, co trafia do JSON-ów i na stronę kursu. Dokument zawiera:

* okładkę i stronę „Jak korzystać z tego zbioru”,
* spis treści z numerami stron (klikalny) i zakładki PDF (rozdział → zadanie),
* wprowadzenia do rozdziałów (podrecznik/*.md): teoria, wzory, diagramy TikZ (SVG),
* rozdziały z listą zadań, a w nich karty zadań: poziom, tagi, wejście/wyjście,
  przykłady w układzie Wejście | Wyjście, wzory ($...$) złożone jak w podręczniku,
  kod startowy z kolorowaniem składni,
* opcjonalnie (--rozwiazania) dodatek z rozwiązaniami wzorcowymi w Pythonie,
  odnośnikami „rozwiązanie → s. N” i wizualizacją przebiegu każdego rozwiązania
  (tabela stanu zmiennych albo drzewo wywołań — zob. trace_solution.py).

Użycie:
    pip install -r scripts/requirements-pdf.txt
    python3 scripts/generate_pdf.py                       # Nauka_Programowania_Zbior_Zadan.pdf
    python3 scripts/generate_pdf.py --rozwiazania         # ... z dodatkiem z rozwiązaniami
    python3 scripts/generate_pdf.py --rozdzialy 02 15 -o próbka.pdf
    python3 scripts/generate_pdf.py --html podglad.html   # sam HTML (bez WeasyPrint)
"""

import argparse
import base64
import html
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
import md_to_json  # noqa: E402
import trace_solution  # noqa: E402

REPO_ROOT = md_to_json.REPO_ROOT
TASKS_DIR = REPO_ROOT / "zbior_zadan"
TESTS_DIR = REPO_ROOT / "zbior_zadan_tests"
SOLUTIONS_DIR = REPO_ROOT / "src" / "python"
PRIMER_DIR = REPO_ROOT / "podrecznik"
MISSING_FIGURES: List[str] = []
DEFAULT_OUTPUT = "Nauka_Programowania_Zbior_Zadan.pdf"
DEFAULT_OUTPUT_SOLUTIONS = "Nauka_Programowania_Zbior_Zadan_z_rozwiazaniami.pdf"

REPO_URL = "https://github.com/djeada/Nauka-Programowania"
COURSE_URL = "https://adamdjellouli.com/courses/kurs_podstaw_pythona/"
AUTHOR = "Adam Djellouli"

CHAPTER_TITLE = re.compile(r"^Rozdział\s+(\d+)\s*[:.]\s*(.+)$")
LEVEL_NAMES = {1: "podstawowy", 2: "średni", 3: "wymagający"}

# Przykład w dwóch kolumnach (Wejście | Wyjście), jeśli każda linia mieści się w połowie strony.
SIDE_BY_SIDE_MAX_CHARS = 36

try:
    from pygments import highlight
    from pygments.formatters import HtmlFormatter
    from pygments.lexers import PythonLexer

    _FORMATTER = HtmlFormatter(nowrap=True, style="friendly")
except ImportError:  # kolorowanie składni jest opcjonalne
    highlight = None


def plural(n: int, one: str, few: str, many: str) -> str:
    """Polska odmiana rzeczownika po liczbie: 1 zadanie, 2–4 zadania, 5–21 zadań, 22–24 zadania…"""
    if n == 1:
        return one
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return few
    return many


def esc(text: str) -> str:
    return html.escape(text, quote=True)


# --------------------------------------------------------------------------- wzory


class LatexToHtml:
    """
    Zamienia podzbiór LaTeX-a używany w treściach zadań na HTML z CSS.

    WeasyPrint nie wykonuje JavaScriptu (KaTeX/MathJax) ani nie zna MathML, więc wzory
    składamy sami: indeksy jako <sup>/<sub>, ułamki jako dwa wiersze, pierwiastek
    z kreską nad wyrażeniem. Nieznane polecenia trafiają do `unknown`.
    """

    # fmt: off
    SYMBOLS = {
        "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "ne": "≠", "neq": "≠",
        "cdot": "·", "times": "×", "pm": "±", "approx": "≈", "to": "→",
        "ldots": "…", "dots": "…", "cdots": "⋯", "pi": "π", "Delta": "Δ",
        "oplus": "⊕", "setminus": "\\", "cup": "∪", "cap": "∩", "in": "∈",
        "lfloor": "⌊", "rfloor": "⌋", "lceil": "⌈", "rceil": "⌉", "infty": "∞",
        "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε",
        "varepsilon": "ε", "theta": "θ", "lambda": "λ", "mu": "μ", "sigma": "σ",
        "phi": "φ", "omega": "ω", "Sigma": "Σ", "Omega": "Ω", "Theta": "Θ",
        "sum": "∑", "prod": "∏", "land": "∧", "lor": "∨", "neg": "¬", "lnot": "¬",
        "wedge": "∧", "vee": "∨", "Rightarrow": "⇒", "Leftrightarrow": "⇔",
        "implies": "⇒", "iff": "⇔", "rightarrow": "→", "leftarrow": "←",
        "mapsto": "↦", "equiv": "≡", "circ": "∘", "div": "÷", "mid": "∣",
        "notin": "∉", "subset": "⊂", "subseteq": "⊆", "emptyset": "∅",
        "forall": "∀", "exists": "∃", "lvert": "|", "rvert": "|", "vert": "|",
        "langle": "⟨", "rangle": "⟩", "ll": "≪", "gg": "≫", "sim": "∼",
        "propto": "∝", "partial": "∂", "nabla": "∇", "prime": "′", "star": "⋆",
        "{": "{", "}": "}", "%": "%", "$": "$", "_": "_", "#": "#", "&": "&amp;",
        "|": "‖",
    }
    SPACES = {" ": " ", ",": "\u2009", ";": " ", ":": "\u2005", "!": "", "quad": "\u2003",
              "qquad": "\u2003\u2003"}
    FUNCTIONS = {"log", "ln", "sin", "cos", "tan", "min", "max", "exp", "gcd", "lcm",
                 "lim", "deg", "det", "mod"}
    OPERATORS = {"bmod": "mod"}
    TEXT_COMMANDS = {"text", "mathrm", "textrm", "operatorname"}
    # fmt: on

    # Klasy znaków jak w TeX-u: relacje i działania dostają odstępy, reszta nie.
    RELATIONS = set("=<>:") | set("≤≥≠≈→←⇒⇔≡∈∉⊂⊆∼∝↦≪≫∣")
    BINARY = set("+−∗·×±∧∨⊕∪∩∖÷∘")
    OPENING = set("([⌊⌈⟨{")
    CLOSING = set(")]⌋⌉⟩}!")
    PUNCTUATION = set(",;")
    REL_SPACE, BIN_SPACE, THIN = " ", " ", " "

    def __init__(self) -> None:
        self.unknown: set = set()

    def render(self, source: str, display: bool = False) -> str:
        self.s, self.i, self.display = source, 0, display
        return f'<span class="math">{self.sequence()}</span>'

    # -- parser ---------------------------------------------------------------
    # Atomy to pary (klasa, html); klasy: ord, bin, rel, open, close, punct, fn, space.

    def sequence(self, until_right: bool = False, script: bool = False) -> str:
        atoms: List[Tuple[str, str]] = []
        while self.i < len(self.s):
            c = self.s[self.i]
            if c == "}":
                break
            if until_right and self.s.startswith("\\right", self.i):
                break
            if c in "^_":
                self.i += 1
                tag = "sup" if c == "^" else "sub"
                script_html = self.group(script=True)
                kind, base = atoms.pop() if atoms else ("ord", "")
                atoms.append((kind, f"{base}<{tag}>{script_html}</{tag}>"))
            elif c.isspace():
                self.i += 1  # jak w TeX-u: odstępy w źródle wzoru nie mają znaczenia
            else:
                atoms.append(self.atom())
        return self.join(atoms, script)

    def join(self, atoms: List[Tuple[str, str]], script: bool) -> str:
        out: List[str] = []
        previous = None
        for n, (kind, text) in enumerate(atoms):
            if kind == "bin" and previous in (
                None,
                "bin",
                "rel",
                "open",
                "punct",
                "fn",
            ):
                kind = "ord"  # minus jednoargumentowy: −5, (−x), a = −b
            following = atoms[n + 1][0] if n + 1 < len(atoms) else None
            if kind == "bin" and following in (None, "close", "punct", "rel"):
                kind = "ord"
            if script or kind in ("ord", "open", "close", "space"):
                out.append(text)
            elif kind == "rel":
                out.append(
                    f"{self.REL_SPACE}{text}{self.REL_SPACE}"
                    if out
                    else text + self.REL_SPACE
                )
            elif kind == "bin":
                out.append(f"{self.BIN_SPACE}{text}{self.BIN_SPACE}")
            elif kind == "punct":
                out.append(text + self.THIN)
            elif kind == "fn":
                before = self.THIN if previous in ("ord", "close") else ""
                out.append(
                    before + (text if following in ("open", None) else text + self.THIN)
                )
            previous = kind
        return "".join(out).strip(self.REL_SPACE + self.BIN_SPACE + self.THIN)

    def classify(self, symbol: str) -> str:
        if symbol in self.RELATIONS:
            return "rel"
        if symbol in self.BINARY:
            return "bin"
        if symbol in self.OPENING:
            return "open"
        if symbol in self.CLOSING:
            return "close"
        if symbol in self.PUNCTUATION:
            return "punct"
        return "ord"

    def group(self, script: bool = False) -> str:
        """Treść {…} (wskaźnik stoi na „{”) albo pojedynczy atom."""
        self.skip_spaces()
        if self.i < len(self.s) and self.s[self.i] == "{":
            self.i += 1
            inner = self.sequence(script=script)
            self.i += 1  # „}”
            return inner
        return self.atom()[1]

    def raw_group(self) -> str:
        self.skip_spaces()
        if self.i >= len(self.s) or self.s[self.i] != "{":
            return ""
        depth, start = 0, self.i
        while self.i < len(self.s):
            if self.s[self.i] == "{":
                depth += 1
            elif self.s[self.i] == "}":
                depth -= 1
                if depth == 0:
                    self.i += 1
                    return self.s[start + 1 : self.i - 1]
            self.i += 1
        return self.s[start + 1 :]

    def skip_spaces(self) -> None:
        while self.i < len(self.s) and self.s[self.i].isspace():
            self.i += 1

    def atom(self) -> Tuple[str, str]:
        self.skip_spaces()
        if self.i >= len(self.s):
            return "ord", ""
        c = self.s[self.i]
        if c == "{":
            return "ord", self.group()
        if c == "\\":
            return self.command()
        self.i += 1
        if c.isalpha():
            return "ord", f"<i>{esc(c)}</i>"
        symbol = {"-": "−", "*": "∗", "'": "′"}.get(c, c)
        return self.classify(symbol), esc(symbol)

    def command(self) -> Tuple[str, str]:
        self.i += 1  # „\”
        match = re.match(r"[A-Za-z]+", self.s[self.i :])
        name = match.group(0) if match else self.s[self.i : self.i + 1]
        self.i += len(name)
        if name in self.SPACES:
            return "space", self.SPACES[name]
        if name in self.SYMBOLS:
            symbol = self.SYMBOLS[name]
            if name in ("sum", "prod"):
                return "fn", self.big_operator(symbol)
            if name in ("{", "}"):
                return ("open" if name == "{" else "close"), symbol
            return self.classify(symbol), symbol
        if name in self.FUNCTIONS:
            return "fn", f'<span class="fn">{name}</span>'
        if name in self.OPERATORS:
            return "bin", f'<span class="fn">{self.OPERATORS[name].strip()}</span>'
        if name in self.TEXT_COMMANDS:
            return "ord", f'<span class="mtext">{esc(self.raw_group())}</span>'
        if name in ("mathbf", "textbf", "boldsymbol"):
            return "ord", f"<b>{self.group()}</b>"
        if name in ("texttt", "mathtt"):
            return "ord", f'<span class="mtt">{esc(self.raw_group())}</span>'
        if name == "underbrace":
            body = self.group()
            self.skip_spaces()
            label = ""
            if self.i < len(self.s) and self.s[self.i] in "_^":
                self.i += 1
                label = self.group(script=True)
            return "ord", (
                f'<span class="{name}"><span class="ub-body">{body}</span>'
                f'<span class="ub-label">{label or "&#8203;"}</span></span>'
            )
        if name in ("overline", "bar"):
            return "ord", f'<span class="overline">{self.group()}</span>'
        if name in ("vec", "hat", "tilde"):
            accent = {"vec": "⃗", "hat": "̂", "tilde": "̃"}[name]
            return "ord", f"{self.group()}{accent}"
        if name in ("big", "Big", "bigg", "Bigg", "displaystyle", "limits"):
            return "space", ""
        if name == "frac":
            num, den = self.group(), self.group()
            return "ord", self.stack(num, den, "frac")
        if name == "binom":
            top, bottom = self.group(), self.group()
            return "ord", (
                f'<span class="delim">(</span>{self.stack(top, bottom, "binom")}'
                f'<span class="delim">)</span>'
            )
        if name == "sqrt":
            return (
                "ord",
                f'<span class="sqrt">√<span class="radicand">{self.group()}</span></span>',
            )
        if name == "left":
            opening = self.delimiter()
            inner = self.sequence(until_right=True)
            closing = ""
            if self.s.startswith("\\right", self.i):
                self.i += len("\\right")
                closing = self.delimiter()
            big = " big" if 'class="frac"' in inner else ""
            return "ord", (
                f'<span class="delim{big}">{opening}</span>{inner}'
                f'<span class="delim{big}">{closing}</span>'
            )
        self.unknown.add(name)
        return "ord", f'<span class="fn">{esc(name)}</span>'

    def big_operator(self, symbol: str) -> str:
        """∑/∏; we wzorze blokowym granice stoją nad i pod znakiem (jak w LaTeX-u)."""
        if not getattr(self, "display", False):
            return f'<span class="bigop">{symbol}</span>'
        limits = {"^": "", "_": ""}
        for _ in range(2):
            self.skip_spaces()
            if self.i < len(self.s) and self.s[self.i] in "^_":
                mark = self.s[self.i]
                self.i += 1
                limits[mark] = self.group(script=True)
        return (
            f'<span class="bigop-limits"><span class="lim">{limits["^"] or "&#8203;"}</span>'
            f'<span class="bigop">{symbol}</span>'
            f'<span class="lim">{limits["_"] or "&#8203;"}</span></span>'
        )

    def delimiter(self) -> str:
        self.skip_spaces()
        if self.i >= len(self.s):
            return ""
        if self.s[self.i] == "\\":
            self.i += 1
            match = re.match(r"[A-Za-z]+|.", self.s[self.i :])
            name = match.group(0)
            self.i += len(name)
            return self.SYMBOLS.get(name, "")
        c = self.s[self.i]
        self.i += 1
        return "" if c == "." else esc(c)

    @staticmethod
    def stack(top: str, bottom: str, kind: str) -> str:
        return (
            f'<span class="{kind}"><span class="num">{top}</span>'
            f'<span class="den">{bottom}</span></span>'
        )


LATEX = LatexToHtml()
# Wzór w tekście może przechodzić do następnej linii (ale nie przez pusty wiersz).
INLINE_MATH = re.compile(r"(?<![\\$])\$(?=\S)((?:[^$\n]|\n(?![ \t]*\n))+?)(?<=\S)\$")
NUMBERED_BULLET = re.compile(r"^(\s*[*+-]\s+)(\d+)\.\s", re.M)
CODE_SPANS = re.compile(r"(```.*?```|`[^`\n]*`)", re.S)
DISPLAY_MATH = re.compile(r"\$\$(.+?)\$\$", re.S)
FENCED_CODE = re.compile(
    r"^([ \t]*)```(python|py)?[ \t]*\n(.*?)\n[ \t]*```[ \t]*$", re.S | re.M
)


# ------------------------------------------------------------------------ markdown


def markdown_to_html(text: str, hard_breaks: bool = True) -> str:
    """
    Markdown → HTML. Wzory $...$ i $$...$$ poza kodem są składane przez LatexToHtml,
    a bloki ```python kolorowane tak samo jak kod startowy.

    hard_breaks: w treściach zadań każde przejście do nowej linii jest złamaniem wiersza
    (tak pisane są pliki zbior_zadan); wprowadzenia z podrecznik/ mają zwykłe akapity.
    """
    import markdown2

    if not text.strip():
        return ""
    blocks: List[str] = []

    def keep(html_block: str) -> str:
        blocks.append(html_block)
        return f"BLOCKPLACEHOLDER{len(blocks) - 1}X"

    def display_math(match: "re.Match[str]") -> str:
        formula = LATEX.render(" ".join(match.group(1).split()), display=True)
        return "\n\n" + keep(f'<div class="math-display">{formula}</div>') + "\n\n"

    def code_block(match: "re.Match[str]") -> str:
        indent, language, body = match.group(1), match.group(2), match.group(3)
        body = "\n".join(line[len(indent) :] for line in body.split("\n"))
        return f"\n{indent}" + keep(code_html(body, language or "text")) + "\n"

    # „* 1. linia: …” to punkt listy, a nie zagnieżdżona lista numerowana.
    text = NUMBERED_BULLET.sub(r"\1\2\\. ", text)
    text = FENCED_CODE.sub(code_block, text)
    parts = CODE_SPANS.split(text)
    for n in range(0, len(parts), 2):  # parzyste fragmenty to tekst poza kodem
        parts[n] = DISPLAY_MATH.sub(display_math, parts[n])
        parts[n] = INLINE_MATH.sub(
            lambda m: keep(LATEX.render(" ".join(m.group(1).split()))), parts[n]
        )
    extras = ["fenced-code-blocks", "tables", "code-friendly", "cuddled-lists"]
    if hard_breaks:
        extras.append("break-on-newline")
    rendered = markdown2.markdown("".join(parts), extras=extras)
    rendered = re.sub(r"<p>\s*(BLOCKPLACEHOLDER\d+X)\s*</p>", r"\1", rendered)
    for _ in range(2):  # blok może zawierać kolejne znaczniki (np. wzór w kodzie — nie)
        rendered = re.sub(
            r"BLOCKPLACEHOLDER(\d+)X", lambda m: blocks[int(m.group(1))], rendered
        )
    return rendered


def inline_markdown(text: str) -> str:
    """Jedna linia markdownu bez otaczającego <p> (np. tytuł zadania)."""
    rendered = markdown_to_html(text).strip()
    return re.sub(r"^<p>(.*)</p>$", r"\1", rendered, flags=re.S)


def code_html(code: str, language: str = "python") -> str:
    code = code.rstrip("\n")
    if highlight and language == "python":
        return (
            f'<pre class="code hl">{highlight(code, PythonLexer(), _FORMATTER)}</pre>'
        )
    return f'<pre class="code">{esc(code)}</pre>'


# ----------------------------------------------------------------------- przykłady


def file_tree(files: Dict[str, Any]) -> str:
    """Pliki z przykładu w tej samej notacji, w której są zapisane w treści zadania."""
    if not files:
        return '<div class="io empty">(pusty katalog roboczy)</div>'
    lines = []
    for path, content in files.items():
        if content is None:
            lines.append(
                f'<span class="path">{esc(path)}</span> <span class="muted">(usunięty)</span>'
            )
        elif isinstance(content, dict):
            lines.append(
                f'<span class="path">{esc(path)}</span> '
                f'<span class="muted">(rozmiar: {content.get("times", 0)} B)</span>'
            )
        else:
            lines.append(f'<span class="path">{esc(path)}</span>')
            for line in content.rstrip("\n").split("\n") if content else []:
                lines.append(f'<span class="muted">│</span> {esc(line)}')
    return f'<pre class="io files">{chr(10).join(lines)}</pre>'


def io_block(text: str) -> str:
    if text == "":
        return '<div class="io empty">(brak)</div>'
    return f'<pre class="io">{esc(text)}</pre>'


def example_html(example: Dict[str, Any], label: str) -> str:
    inp, out = example["input"], example["output"]
    widest = max((len(line) for line in (inp + "\n" + out).split("\n")), default=0)
    layout = "side" if widest <= SIDE_BY_SIDE_MAX_CHARS else "stacked"
    parts = [
        f'<div class="example {layout}">',
        f'<div class="example-label">{label}</div>',
    ]
    if "files" in example:
        parts.append(
            f'<div class="io-cell wide"><div class="io-head">Pliki przed</div>{file_tree(example["files"])}</div>'
        )
    parts.append('<div class="io-row">')
    parts.append(
        f'<div class="io-cell"><div class="io-head">Wejście</div>{io_block(inp)}</div>'
    )
    parts.append(
        f'<div class="io-cell"><div class="io-head">Wyjście</div>{io_block(out)}</div>'
    )
    parts.append("</div>")
    if "expected_files" in example:
        parts.append(
            f'<div class="io-cell wide"><div class="io-head">Pliki po</div>'
            f'{file_tree(example["expected_files"])}</div>'
        )
    if example.get("explanation"):
        parts.append(
            f'<div class="explanation">{markdown_to_html(example["explanation"])}</div>'
        )
    parts.append("</div>")
    return "".join(parts)


# -------------------------------------------------------------------------- zadania


def anchor(slug: str, kind: str = "zad") -> str:
    return f"{kind}-" + re.sub(r"[^A-Za-z0-9]+", "-", slug).strip("-")


def section(label: str, body: str, extra_class: str = "") -> str:
    if not body.strip():
        return ""
    return (
        f'<div class="sec {extra_class}"><div class="sec-label">{label}</div>'
        f'<div class="sec-body">{body}</div></div>'
    )


def stars(difficulty: int) -> str:
    filled = "★" * difficulty
    return f'<span class="stars" title="{LEVEL_NAMES.get(difficulty, "")}">{filled}<span class="off">{"★" * (3 - difficulty)}</span></span>'


def exercise_html(ex: Dict[str, Any], with_solutions: bool) -> str:
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in ex["tags"])
    solution_ref = ""
    if with_solutions and solution_file(ex) is not None:
        solution_ref = f'<a class="solution-ref" href="#{anchor(ex["slug"], "roz")}">rozwiązanie</a>'
    parts = [
        f'<article class="exercise level-{ex["difficulty"]}" id="{anchor(ex["slug"])}">',
        '<header class="ex-head">',
        f'<div class="ex-top"><span class="ex-id">{ex["id"]}</span>{stars(ex["difficulty"])}{solution_ref}</div>',
        f'<h2 class="ex-title">{inline_markdown(ex["title"])}</h2>',
        f'<div class="tags">{tags}</div>',
        "</header>",
        f'<div class="ex-desc">{markdown_to_html(ex["description"])}</div>',
        section("Wejście", markdown_to_html(ex["input"])),
        section("Wyjście", markdown_to_html(ex["output"])),
        section("Ograniczenia", markdown_to_html(ex["constraints"])),
    ]
    examples = ex["examples"]
    for n, example in enumerate(examples, start=1):
        label = "Przykład" if len(examples) == 1 else f"Przykład {n}"
        parts.append(example_html(example, label))
    parts.append(section("Uwagi", markdown_to_html(ex["notes"]), "notes"))
    if ex["starter_code"]:
        short = " short" if ex["starter_code"].count("\n") <= 30 else ""
        parts.append(
            f'<div class="starter{short}"><div class="example-label">Kod startowy</div>'
            f'{code_html(ex["starter_code"])}</div>'
        )
    parts.append("</article>")
    return "\n".join(parts)


def split_chapter_title(title: str, fallback_number: int) -> Tuple[int, str]:
    match = CHAPTER_TITLE.match(title)
    if match:
        return int(match.group(1)), match.group(2).strip()
    return fallback_number, title


def chapter_html(stem: str, chapter: Dict[str, Any], with_solutions: bool) -> str:
    number, name = split_chapter_title(chapter["chapter_title"], int(stem[:2]))
    rows = "".join(
        f'<tr><td class="c-id">{ex["id"]}</td>'
        f'<td class="c-title"><a href="#{anchor(ex["slug"])}">{inline_markdown(ex["title"])}</a></td>'
        f'<td class="c-stars">{stars(ex["difficulty"])}</td>'
        f'<td class="c-page"><a class="pageref" href="#{anchor(ex["slug"])}"></a></td></tr>'
        for ex in chapter["exercises"]
    )
    primer = primer_html(stem, number)
    tasks_heading = (
        f'<h2 class="tasks-heading" id="{anchor(stem, "zadania")}">Zadania</h2>'
        if primer
        else ""
    )
    opener = f"""
    <section class="chapter" id="{anchor(stem, 'rozdzial')}">
      <div class="chapter-opener">
        <div class="chapter-number">Rozdział {number}</div>
        <h1 class="chapter-title">{esc(name)}</h1>
        {primer}
        {tasks_heading}
        <div class="chapter-desc">{markdown_to_html(chapter["chapter_description"])}</div>
        <h3 class="chapter-list-title">Zadania w tym rozdziale</h3>
        <table class="chapter-list">{rows}</table>
      </div>
    """
    body = "\n".join(exercise_html(ex, with_solutions) for ex in chapter["exercises"])
    return opener + body + "</section>"


CALLOUTS = {
    "uwaga": "warn",
    "pułapka": "warn",
    "wskazówka": "tip",
    "pamiętaj": "tip",
    "ciekawostka": "info",
    "definicja": "def",
    "zapamiętaj": "def",
}


def primer_html(stem: str, chapter_number: int) -> str:
    """Wprowadzenie do rozdziału z podrecznik/<rozdział>.md (teoria, diagramy, przykład)."""
    path = PRIMER_DIR / f"{stem}.md"
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\A\s*#\s[^\n]*\n", "", text)  # tytuł jest już w nagłówku rozdziału
    rendered = markdown_to_html(text, hard_breaks=False)
    figure = 0

    def make_figure(match: "re.Match[str]") -> str:
        nonlocal figure
        figure += 1
        src, alt = match.group("src"), html.unescape(match.group("alt"))
        if not re.match(r"^[a-z]+:", src):
            src = (PRIMER_DIR / src).relative_to(REPO_ROOT).as_posix()
            if not (REPO_ROOT / src).exists():
                MISSING_FIGURES.append(src)
        caption = (
            f'<span class="fig-no">Rys. {chapter_number}.{figure}.</span> {esc(alt)}'
        )
        return (
            f'<figure><img src="{esc(src)}" alt="{esc(alt)}"/>'
            f"<figcaption>{caption}</figcaption></figure>"
        )

    rendered = re.sub(
        r'<p>\s*<img src="(?P<src>[^"]+)" alt="(?P<alt>[^"]*)"\s*/?>\s*</p>',
        make_figure,
        rendered,
    )

    def callout(match: "re.Match[str]") -> str:
        kind = CALLOUTS.get(match.group(2).strip().lower(), "info")
        return f'<blockquote class="callout {kind}">\n<p><strong>{match.group(2)}'

    rendered = re.sub(r"<blockquote>(\s*)<p><strong>([^<:]+)", callout, rendered)
    return f'<div class="primer">{rendered}</div>'


# --------------------------------------------------------------------- rozwiązania

DOCSTRING = re.compile(r'\A\s*[rRuU]?("""|\'\'\')[\s\S]*?\1[ \t]*\n+')


def solution_file(ex: Dict[str, Any]) -> Optional[Path]:
    chapter, task_id = ex["slug"].split("/")
    path = SOLUTIONS_DIR / chapter / f"zad{task_id[4:6]}{task_id[6:].lower()}.py"
    return path if path.exists() else None


def numbered_code_html(code: str) -> str:
    """Kod z numerami linii — tabela przebiegu odwołuje się do nich."""
    code = code.rstrip("\n")
    if highlight:
        body = highlight(code, PythonLexer(), _FORMATTER).rstrip("\n").split("\n")
    else:
        body = [esc(line) for line in code.split("\n")]
    width = len(str(len(body)))
    lines = [
        f'<span class="cl"><span class="ln">{n:>{width}}</span>{line or " "}</span>'
        for n, line in enumerate(body, 1)
    ]
    return f'<pre class="code hl numbered">{"".join(lines)}</pre>'


TRACE_MAX_ROWS = 16


def trace_table_html(table: Dict[str, Any]) -> str:
    head = ['<th class="t-line">linia</th>']
    for fn, name in table["columns"]:
        scope = (
            f'<span class="t-scope">{esc(fn)}()</span>'
            if table["show_fn"] and fn not in ("", "<module>")
            else ""
        )
        head.append(f'<th class="t-var"><code>{esc(name)}</code>{scope}</th>')
    head.append('<th class="t-out">wypisano</th>')

    def row_html(row: Dict[str, Any]) -> str:
        code = row["code"] if len(row["code"]) <= 34 else row["code"][:33] + "…"
        cells = [
            f'<td class="t-line"><span class="t-ln">{row["ln"]}</span> <code>{esc(code)}</code></td>'
        ]
        for cell in row["cells"]:
            if cell["value"] is None:
                cells.append('<td class="t-val"></td>')
            else:
                css = "t-val chg" if cell["changed"] else "t-val"
                cells.append(f'<td class="{css}">{esc(cell["value"])}</td>')
        out = row["out"].rstrip("\n").replace("\n", " ⏎ ")
        out = out if len(out) <= 28 else out[:27] + "…"
        cells.append(f'<td class="t-out">{esc(out)}</td>')
        return "<tr>" + "".join(cells) + "</tr>"

    rows = table["rows"]
    if len(rows) > TRACE_MAX_ROWS:
        skipped = len(rows) - (TRACE_MAX_ROWS - 4)
        body = [row_html(r) for r in rows[: TRACE_MAX_ROWS - 5]]
        body.append(
            f'<tr class="t-skip"><td colspan="{len(head)}">⋮ pominięto {skipped} '
            f'{plural(skipped, "krok", "kroki", "kroków")} ⋮</td></tr>'
        )
        body += [row_html(r) for r in rows[-4:]]
    else:
        body = [row_html(r) for r in rows]
    return (
        f'<table class="trace"><thead><tr>{"".join(head)}</tr></thead>'
        f'<tbody>{"".join(body)}</tbody></table>'
    )


CALL_TREE_MAX_NODES = 15


def call_tree_svg(tree: Dict[str, Any]) -> str:
    """Drzewo wywołań rekurencyjnych jako SVG (węzeł: wywołanie, pod nim zwrócona wartość)."""
    char_w, font, level_h, gap, pad = 5.2, 8.6, 50.0, 10.0, 6.0
    counter = {"n": 0}

    def prepare(node: Dict[str, Any]) -> Dict[str, Any]:
        counter["n"] += 1
        args = ", ".join(node["args"].values())
        label = f'{node["fn"]}({args})'
        if len(label) > 26:
            label = label[:25] + "…"
        ret = "" if node["ret"] in (None, "None") else f'→ {node["ret"]}'
        out = {"label": label, "ret": ret, "order": counter["n"], "children": []}
        for child in node["children"]:
            if counter["n"] >= CALL_TREE_MAX_NODES:
                out["children"].append(
                    {"label": "…", "ret": "", "order": None, "children": []}
                )
                break
            out["children"].append(prepare(child))
        return out

    roots = tree["children"] if tree.get("fn") is None else [tree]
    nodes = [prepare(r) for r in roots]

    def measure(node: Dict[str, Any]) -> float:
        node["w"] = max(len(node["label"]), len(node["ret"])) * char_w + 2 * pad
        children_w = sum(measure(c) for c in node["children"]) + gap * max(
            0, len(node["children"]) - 1
        )
        node["span"] = max(node["w"], children_w)
        return node["span"]

    total = sum(measure(n) for n in nodes) + gap * (len(nodes) - 1)
    shapes: List[str] = []
    depth = {"max": 0}

    def place(node: Dict[str, Any], left: float, level: int) -> None:
        depth["max"] = max(depth["max"], level)
        cx = left + node["span"] / 2
        y = 8 + level * level_h
        node["cx"], node["y"] = cx, y
        children_w = sum(c["span"] for c in node["children"]) + gap * max(
            0, len(node["children"]) - 1
        )
        x = cx - children_w / 2
        for child in node["children"]:
            place(child, x, level + 1)
            shapes.append(
                f'<line x1="{cx:.1f}" y1="{y + (31 if node["ret"] else 16):.1f}" x2="{child["cx"]:.1f}" y2="{child["y"]:.1f}" '
                f'stroke="#94a3b8" stroke-width="0.8"/>'
            )
            x += child["span"] + gap
        w = node["w"]
        if node["label"] == "…":
            shapes.append(
                f'<text x="{cx:.1f}" y="{y + 11:.1f}" text-anchor="middle" fill="#64748b" font-size="{font}">…</text>'
            )
            return
        shapes.append(
            f'<rect x="{cx - w / 2:.1f}" y="{y:.1f}" width="{w:.1f}" height="16" rx="3" '
            f'fill="#dbeafe" stroke="#2563eb" stroke-width="0.8"/>'
        )
        shapes.append(
            f'<text x="{cx:.1f}" y="{y + 11.2:.1f}" text-anchor="middle" fill="#1e293b" '
            f'font-size="{font}">{esc(node["label"])}</text>'
        )
        if node["ret"]:
            shapes.append(
                f'<text x="{cx:.1f}" y="{y + 27:.1f}" text-anchor="middle" fill="#15803d" '
                f'font-size="{font - 0.6}" font-weight="bold">{esc(node["ret"])}</text>'
            )
        if node["order"] is not None:
            shapes.append(
                f'<text x="{cx - w / 2 - 2:.1f}" y="{y - 2:.1f}" text-anchor="end" fill="#94a3b8" '
                f'font-size="6.5">{node["order"]}</text>'
            )

    x = 0.0
    for node in nodes:
        place(node, x, 0)
        x += node["span"] + gap
    width, height = total + 16, 8 + depth["max"] * level_h + 34
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}pt" height="{height:.0f}pt" '
        f'viewBox="-8 0 {width:.1f} {height:.1f}" font-family="DejaVu Sans Mono, monospace">'
        + "".join(shapes)
        + "</svg>"
    )
    data = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f'<img class="call-tree" src="data:image/svg+xml;base64,{data}" alt="drzewo wywołań"/>'


def visualization_html(
    ex: Dict[str, Any], code: str, trace: Optional[Dict[str, Any]]
) -> str:
    if not trace or trace.get("error"):
        return ""
    example = ex["examples"][0]
    shown_input = example["input"].strip("\n")
    if shown_input.count("\n") > 3 or len(shown_input) > 60:
        lines = shown_input.split("\n")
        shown_input = " ⏎ ".join(lines[:3])[:57] + " …"
    else:
        shown_input = shown_input.replace("\n", " ⏎ ")
    input_note = (
        f"dla wejścia z przykładu: <code>{esc(shown_input)}</code>"
        if shown_input
        else "dla przykładu"
    )
    tree = trace_solution.call_tree(trace)
    if tree:
        return (
            f'<div class="viz"><div class="viz-head">Drzewo wywołań {input_note}</div>'
            f"{call_tree_svg(tree)}"
            '<div class="viz-note">Liczby przy węzłach to kolejność wywołań; '
            "pod wywołaniem — zwrócona wartość.</div></div>"
        )
    table = trace_solution.state_table(trace, code)
    if not table:
        return ""
    note = (
        " (śledzenie przerwane — program wykonuje bardzo wiele kroków)"
        if table["truncated"]
        else ""
    )
    return (
        f'<div class="viz"><div class="viz-head">Przebieg programu {input_note}{note}</div>'
        f"{trace_table_html(table)}"
        '<div class="viz-note">Każdy wiersz to wykonana linia kodu i stan zmiennych po niej; '
        "wyróżnione są wartości, które właśnie się zmieniły.</div></div>"
    )


def solutions_html(chapters: Dict[str, Dict[str, Any]]) -> str:
    parts = [
        '<section class="appendix" id="rozwiazania">',
        '<div class="chapter-opener">',
        '<div class="chapter-number">Dodatek</div>',
        '<h1 class="chapter-title">Rozwiązania wzorcowe (Python)</h1>',
        '<div class="chapter-desc"><p>Każde rozwiązanie przechodzi wszystkie przykłady i testy '
        "zadania (sprawdza to CI repozytorium). To jedna z wielu poprawnych odpowiedzi — "
        "zajrzyj tu dopiero po własnej próbie, a potem porównaj podejścia.</p>"
        "<p>Pod kodem jest <b>przebieg programu</b> dla pierwszego przykładu z treści: kolejne "
        "wykonane linie (numery jak przy kodzie) i wartości zmiennych po każdej z nich. Dla funkcji "
        "rekurencyjnych zamiast tabeli jest <b>drzewo wywołań</b> z argumentami i zwracanymi "
        "wartościami. Przebiegi powstają automatycznie — przez uruchomienie rozwiązania.</p>"
        f"<p>Rozwiązania w C++, Javie, JavaScripcie, Ruście, Haskellu i Bashu znajdziesz w "
        f'<a href="{REPO_URL}">repozytorium</a> (katalog <code>src/</code>).</p></div>',
        "</div>",
    ]
    jobs = []
    for chapter in chapters.values():
        for ex in chapter["exercises"]:
            path = solution_file(ex)
            if path is not None:
                code = DOCSTRING.sub("", path.read_text(encoding="utf-8"), count=1)
                jobs.append((ex, code))

    def trace_job(job: Tuple[Dict[str, Any], str]) -> Optional[Dict[str, Any]]:
        ex, code = job
        example = ex["examples"][0]
        return trace_solution.run_trace(code, example["input"], example.get("files"))

    with ThreadPoolExecutor() as pool:
        traces = dict(zip((ex["slug"] for ex, _ in jobs), pool.map(trace_job, jobs)))
    codes = {ex["slug"]: code for ex, code in jobs}

    for stem, chapter in chapters.items():
        number, name = split_chapter_title(chapter["chapter_title"], int(stem[:2]))
        parts.append(f'<h2 class="sol-chapter">Rozdział {number}. {esc(name)}</h2>')
        for ex in chapter["exercises"]:
            if ex["slug"] not in codes:
                continue
            code = codes[ex["slug"]]
            parts.append(
                f'<div class="solution" id="{anchor(ex["slug"], "roz")}">'
                f'<div class="sol-head"><span class="ex-id">{ex["id"]}</span> '
                f'<span class="sol-title">{inline_markdown(ex["title"])}</span>'
                f'<a class="back-ref" href="#{anchor(ex["slug"])}">treść</a></div>'
                f"{numbered_code_html(code)}"
                f"{visualization_html(ex, code, traces[ex['slug']])}</div>"
            )
    parts.append("</section>")
    return "\n".join(parts)


# ------------------------------------------------------------ strony początkowe


def build_version() -> str:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs %h"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.split()
        return f"wydanie {out[0]} ({out[1]})"
    except (OSError, subprocess.CalledProcessError, IndexError):
        return f"wydanie {date.today().isoformat()}"


def cover_html(chapters: Dict[str, Dict[str, Any]], with_solutions: bool) -> str:
    total = sum(len(c["exercises"]) for c in chapters.values())
    subtitle = "Zbiór zadań z rozwiązaniami" if with_solutions else "Zbiór zadań"
    return f"""
    <section class="cover">
      <div class="cover-code">
        <span class="k">for</span> zadanie <span class="k">in</span> zbior:<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;wejscie = <span class="f">input</span>()<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="f">print</span>(rozwiaz(wejscie))
      </div>
      <div class="cover-main">
        <div class="cover-kicker">Kurs programowania od podstaw</div>
        <div class="cover-title">Nauka<br/>Programowania</div>
        <div class="cover-rule"></div>
        <div class="cover-subtitle">{subtitle}</div>
        <div class="cover-stats">
          <div><b>{len(chapters)}</b><span>{plural(len(chapters), "rozdział", "rozdziały", "rozdziałów")}</span></div>
          <div><b>{total}</b><span>{plural(total, "zadanie", "zadania", "zadań")}</span></div>
          <div><b>7</b><span>języków rozwiązań</span></div>
        </div>
      </div>
      <div class="cover-foot">
        <div>{AUTHOR} i współtwórcy · licencja MIT</div>
        <div>{REPO_URL.replace("https://", "")} · {build_version()}</div>
      </div>
    </section>
    """


def how_to_html(with_solutions: bool) -> str:
    solutions_line = (
        "<li><b>Rozwiązania wzorcowe</b> w Pythonie są w dodatku na końcu książki — przy każdym "
        "zadaniu jest odnośnik <i>rozwiązanie</i>, a przy rozwiązaniu odnośnik <i>treść</i>.</li>"
        if with_solutions
        else f'<li><b>Rozwiązania wzorcowe</b> w 7 językach są w <a href="{REPO_URL}">repozytorium</a> '
        "(katalog <code>src/</code>); wersję PDF z rozwiązaniami w Pythonie tworzy "
        "<code>generate_pdf.py --rozwiazania</code>.</li>"
    )
    example = code_html("a = int(input())\nb = int(input())\nprint(a + b)")
    return f"""
    <section class="front" id="jak-korzystac">
      <h1 class="front-title">Jak korzystać z tego zbioru</h1>
      <p class="lead">Programowania uczy się, pisząc programy. Każde zadanie w tej książce to
      mały, kompletny program o dokładnie opisanym wejściu i wyjściu — dzięki temu sam
      sprawdzisz, czy działa, a automatyczna sprawdzarka oceni go tak samo jak tutaj.</p>

      <div class="front-grid">
        <div class="front-box">
          <h3>1. Program czyta wejście i wypisuje wynik</h3>
          <p>Dane wczytujesz ze <b>standardowego wejścia</b> (w Pythonie <code>input()</code>),
          a wynik wypisujesz na <b>standardowe wyjście</b> (<code>print()</code>). Nie wypisuj
          komunikatów w rodzaju „Podaj liczbę:” — psują porównanie wyniku.</p>
          {example}
        </div>
        <div class="front-box">
          <h3>2. Uruchom i porównaj z przykładem</h3>
          <p>Zapisz program w pliku i uruchom go, wpisując dane z sekcji <i>Wejście</i>:</p>
          <pre class="code">$ python3 zad01.py
3
4
7</pre>
          <p>Dłuższe dane zapisz w pliku i przekaż programowi:
          <code>python3 zad01.py &lt; wejscie.txt</code>.</p>
        </div>
      </div>

      <h3>Jak czytać kartę zadania</h3>
      <div class="legend">
        <div class="legend-card">
          <div class="ex-top"><span class="ex-id">ZAD-03</span>{stars(2)}</div>
          <div class="legend-title">Tytuł zadania</div>
          <div class="tags"><span class="tag">pętle</span><span class="tag">listy</span></div>
        </div>
        <ul>
          <li><b>ZAD-NN</b> — numer zadania w rozdziale; podpunkty (ZAD-05A, ZAD-05B…) to osobne programy.</li>
          <li><b>Poziom:</b> {stars(1)} {LEVEL_NAMES[1]}, {stars(2)} {LEVEL_NAMES[2]}, {stars(3)} {LEVEL_NAMES[3]}.</li>
          <li><b>Tagi</b> mówią, jakie konstrukcje i techniki ćwiczy zadanie.</li>
          <li><b>Wejście / Wyjście</b> — dokładny format danych; <b>Ograniczenia</b> — zakres wartości.</li>
          <li><b>Przykład</b> pokazuje dane wejściowe i oczekiwany wynik obok siebie.</li>
          <li><b>Kod startowy</b> — szkielet do uzupełnienia (tam, gdzie zadanie dotyczy funkcji lub klas).</li>
        </ul>
      </div>

      <h3>Jak sprawdzarka porównuje wynik</h3>
      <ul>
        <li>Spacje na końcach linii i puste linie na końcu wyjścia są ignorowane.</li>
        <li>Liczba linii i ich treść muszą się zgadzać — łącznie z wielkością liter, polskimi znakami i kropkami.</li>
        <li>Liczby mogą różnić się o 0,01 (np. <code>3.14</code> i <code>3.1416</code> uchodzą za równe).</li>
        <li>Tekst podany w <code>input("…")</code> nie jest traktowany jako wyjście.</li>
      </ul>

      <h3>Gdzie dalej</h3>
      <ul>
        <li><b>Rozwiązuj online:</b> <a href="{COURSE_URL}">{COURSE_URL.replace("https://", "")}</a> —
        te same zadania z edytorem w przeglądarce i automatycznymi testami.</li>
        {solutions_line}
        <li>Każdy rozdział zaczyna się od <b>wprowadzenia</b>: teorii z diagramami, wzorami
        i rozwiązanym przykładem. Przeczytaj je przed zadaniami — opisuje wszystko, czego potrzebujesz.</li>
        <li>Zadania w rozdziale są ułożone od najprostszych. Gdy utkniesz, wróć do przykładu,
        rozpisz go na kartce krok po kroku i dopiero wtedy wróć do kodu.</li>
      </ul>
    </section>
    """


def toc_row(number: str, name: str, meta: str, target: str) -> str:
    meta_html = f'<span class="toc-meta">{esc(meta)}</span>' if meta else ""
    return (
        f'<tr><td class="toc-num">{number}</td>'
        f'<td class="toc-name">{meta_html}<a href="#{target}">{esc(name)}</a></td>'
        f'<td class="toc-page"><a class="pageref" href="#{target}"></a></td></tr>'
    )


def toc_html(chapters: Dict[str, Dict[str, Any]], with_solutions: bool) -> str:
    rows = []
    for stem, chapter in chapters.items():
        number, name = split_chapter_title(chapter["chapter_title"], int(stem[:2]))
        levels = [ex["difficulty"] for ex in chapter["exercises"]]
        mix = " · ".join(
            f"{levels.count(d)}× {'★' * d}" for d in (1, 2, 3) if levels.count(d)
        )
        rows.append(
            toc_row(
                f"{number:02d}",
                name,
                f"{len(levels)} {plural(len(levels), 'zadanie', 'zadania', 'zadań')} · {mix}",
                anchor(stem, "rozdzial"),
            )
        )
    if with_solutions:
        rows.append(
            toc_row("A", "Rozwiązania wzorcowe (Python)", "dodatek", "rozwiazania")
        )
    return f"""
    <section class="toc" id="spis-tresci">
      <h1 class="front-title">Spis treści</h1>
      <table class="toc-list">
        {toc_row("", "Jak korzystać z tego zbioru", "", "jak-korzystac")}
        {''.join(rows)}
      </table>
    </section>
    """


# ----------------------------------------------------------------------------- CSS

CSS = r"""
@page {
  size: A4;
  margin: 2.1cm 1.8cm 2cm 1.8cm;
  @top-left { content: "Nauka Programowania"; font: 8pt 'DejaVu Sans', sans-serif; color: #94a3b8; }
  @top-right { content: string(chapter); font: 8pt 'DejaVu Sans', sans-serif; color: #64748b; }
  @bottom-center { content: counter(page); font: 8.5pt 'DejaVu Sans', sans-serif; color: #64748b; }
}
@page cover { margin: 0; @top-left { content: none } @top-right { content: none } @bottom-center { content: none } }
@page front { @top-left { content: none } @top-right { content: none } }

:root { --ink: #1e293b; --muted: #64748b; --line: #e2e8f0; --accent: #2563eb; --accent-2: #f59e0b;
        --soft: #f1f5f9; --code-bg: #f8fafc; }

* { box-sizing: border-box; }
html { font-family: 'DejaVu Sans', 'Noto Sans', Arial, sans-serif; font-size: 9.6pt; line-height: 1.5; color: var(--ink); }
body { margin: 0; }
a { color: var(--accent); text-decoration: none; }
p { margin: 0 0 5pt 0; orphans: 2; widows: 2; hyphens: auto; }
ul, ol { margin: 2pt 0 6pt 0; padding-left: 15pt; }
li { margin: 1.5pt 0; }
li > p { margin: 0; }
h1, h2, h3 { break-after: avoid; }
strong, b { color: #0f172a; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.6pt; background: var(--soft);
       border-radius: 2pt; padding: 0.5pt 2.5pt; color: #0f172a; }
pre { font-family: 'DejaVu Sans Mono', monospace; margin: 0; white-space: pre-wrap; overflow-wrap: anywhere; }
pre code { background: none; padding: 0; font-size: inherit; }
table { border-collapse: collapse; }
.ex-desc table, .sec-body table, .chapter-desc table { margin: 4pt 0 8pt 0; font-size: 9pt; }
.ex-desc th, .ex-desc td, .sec-body th, .sec-body td { border: 0.6pt solid var(--line); padding: 2pt 6pt; text-align: left; }
.ex-desc th, .sec-body th { background: var(--soft); }

/* ---- wzory ---- */
.math { font-family: 'DejaVu Serif', serif; font-size: 1.04em; white-space: nowrap; }
.math i { font-style: italic; }
.math sup, .math sub { font-size: 0.72em; line-height: 0; }
.math .fn, .math .mtext { font-style: normal; }
.math .frac, .math .binom { display: inline-block; vertical-align: middle; text-align: center; margin: 0 1.5pt; font-size: 0.92em; }
.math .frac > span, .math .binom > span { display: block; line-height: 1.2; padding: 0 1.5pt; }
.math .frac > .num { border-bottom: 0.6pt solid currentColor; }
.math .delim.big { font-size: 1.7em; vertical-align: -0.12em; font-weight: 200; line-height: 1; }
.math .sqrt .radicand { border-top: 0.6pt solid currentColor; padding: 0 1pt; }
.math .bigop { font-size: 1.25em; vertical-align: -0.08em; }
.math .bigop-limits { display: inline-block; vertical-align: middle; text-align: center; margin: 0 2pt; line-height: 1; }
.math .bigop-limits > span { display: block; }
.math .bigop-limits .bigop { font-size: 1.6em; vertical-align: 0; line-height: 1.05; }
.math .bigop-limits .lim { font-size: 0.68em; }

/* ---- kolorowanie składni (pygments, styl jasny) ---- */
PYGMENTS_CSS

/* ---- okładka ---- */
.cover { page: cover; width: 210mm; height: 297mm; position: relative; color: #f8fafc;
         background: linear-gradient(160deg, #0f172a 0%, #1e3a8a 58%, #2563eb 100%); overflow: hidden; }
.cover-code { position: absolute; top: 34mm; right: 18mm; font: 11pt 'DejaVu Sans Mono', monospace;
              color: rgba(226, 232, 240, 0.32); line-height: 1.7; text-align: left; }
.cover-code .k { color: rgba(251, 191, 36, 0.55); }
.cover-code .f { color: rgba(147, 197, 253, 0.6); }
.cover-main { position: absolute; left: 22mm; right: 22mm; top: 98mm; }
.cover-kicker { text-transform: uppercase; letter-spacing: 3pt; font-size: 9pt; color: #bfdbfe; margin-bottom: 10pt; }
.cover-title { font-family: 'DejaVu Serif', serif; font-weight: bold; font-size: 44pt; line-height: 1.08; color: #fff; }
.cover-rule { width: 70pt; height: 4pt; background: var(--accent-2); margin: 18pt 0 14pt 0; border-radius: 2pt; }
.cover-subtitle { font-size: 19pt; color: #e0e7ff; margin-bottom: 30pt; }
.cover-stats { display: flex; gap: 26pt; }
.cover-stats div { border-left: 2pt solid rgba(245, 158, 11, 0.8); padding-left: 8pt; }
.cover-stats b { display: block; font-size: 22pt; color: #fff; line-height: 1.1; }
.cover-stats span { font-size: 8.5pt; color: #c7d2fe; text-transform: uppercase; letter-spacing: 1pt; }
.cover-foot { position: absolute; left: 22mm; right: 22mm; bottom: 18mm; font-size: 8.5pt; color: #c7d2fe;
              border-top: 0.6pt solid rgba(199, 210, 254, 0.35); padding-top: 8pt; line-height: 1.7; }

/* ---- strony początkowe ---- */
.front, .toc { page: front; break-before: page; }
.front-title { font-family: 'DejaVu Serif', serif; font-size: 22pt; color: #0f172a; margin: 0 0 10pt 0;
               padding-bottom: 6pt; border-bottom: 2.5pt solid var(--accent-2); bookmark-level: 1; }
.front h3 { font-size: 11pt; color: #1e3a8a; margin: 12pt 0 4pt 0; bookmark-level: none; }
.lead { font-size: 10.5pt; color: #334155; margin-bottom: 10pt; }
.front-grid { display: flex; gap: 12pt; }
.front-box { flex: 1; background: var(--soft); border-radius: 5pt; padding: 8pt 10pt; }
.front-box h3 { margin-top: 0; }
.front-box .code { margin-top: 4pt; }
.legend { display: flex; gap: 14pt; align-items: flex-start; }
.legend ul { flex: 1; margin: 0; }
.legend-card { width: 5.4cm; border: 0.8pt solid var(--line); border-left: 3pt solid var(--accent);
               border-radius: 4pt; padding: 6pt 8pt; }
.legend-title { font-weight: bold; font-size: 11pt; margin: 2pt 0; }

.toc-list { width: 100%; }
.toc-list td { border-bottom: 0.6pt solid var(--line); padding: 3.4pt 0; vertical-align: baseline; }
.toc-list tr { break-inside: avoid; }
.toc-list a { color: var(--ink); }
.toc-num { width: 28pt; font-weight: bold; color: var(--accent); font-size: 11pt; }
.toc-name { font-size: 10.5pt; }
.toc-page { width: 30pt; text-align: right; font-weight: bold; }
.toc-page .pageref::after { color: #0f172a; }
.toc-meta { float: right; font-size: 7.6pt; color: var(--muted); padding: 1.5pt 10pt 0 8pt; }

/* ---- rozdziały ---- */
.chapter, .appendix { break-before: page; }
.chapter-opener { margin-bottom: 8pt; }
.chapter-number { font-size: 9pt; text-transform: uppercase; letter-spacing: 2.5pt; color: var(--accent-2);
                  font-weight: bold; margin-top: 8pt; }
.chapter-title { font-family: 'DejaVu Serif', serif; font-size: 25pt; line-height: 1.15; color: #0f172a;
                 margin: 4pt 0 12pt 0; string-set: chapter content(); bookmark-level: 1; }
.chapter-desc { font-size: 9.8pt; color: #334155; background: var(--soft); border-radius: 5pt; padding: 9pt 12pt; }
.chapter-desc p:last-child, .chapter-desc ul:last-child { margin-bottom: 0; }
.chapter-list-title { font-size: 10pt; color: #1e3a8a; margin: 14pt 0 4pt 0; text-transform: uppercase;
                      letter-spacing: 1pt; bookmark-level: none; }
.chapter-list { width: 100%; font-size: 9.2pt; }
.chapter-list td { padding: 2.6pt 4pt; border-bottom: 0.5pt solid var(--line); vertical-align: baseline; }
.chapter-list a { color: var(--ink); }
.c-id { width: 52pt; font-family: 'DejaVu Sans Mono', monospace; font-size: 8pt; color: var(--muted); }
.c-stars { width: 40pt; text-align: right; }
.c-page { width: 26pt; text-align: right; }
.pageref::after { content: target-counter(attr(href url), page); color: var(--muted); }

/* ---- karta zadania ---- */
.exercise { margin: 16pt 0 6pt 0; padding-top: 10pt; border-top: 1.2pt solid #cbd5e1; }
.ex-head { break-inside: avoid; break-after: avoid; margin-bottom: 6pt; }
.ex-top { display: flex; align-items: center; gap: 7pt; }
.ex-id { font-family: 'DejaVu Sans Mono', monospace; font-weight: bold; font-size: 8pt; color: #fff;
         background: var(--accent); border-radius: 3pt; padding: 1.2pt 5pt; }
.level-2 .ex-head .ex-id { background: #7c3aed; }
.level-3 .ex-head .ex-id { background: #dc2626; }
.stars { color: var(--accent-2); font-size: 9pt; letter-spacing: 0.5pt; }
.stars .off { color: #cbd5e1; }
.solution-ref { margin-left: auto; font-size: 7.8pt; color: var(--muted); }
.solution-ref::after { content: " → s. " target-counter(attr(href url), page); }
.ex-title { font-size: 13pt; line-height: 1.25; margin: 3pt 0 2pt 0; color: #0f172a; bookmark-level: 2;
            bookmark-label: content(); }
.tags { margin-top: 1pt; }
.tag { display: inline-block; font-size: 7.3pt; color: #475569; background: var(--soft);
       border: 0.5pt solid var(--line); border-radius: 7pt; padding: 0 5pt; margin: 0 3pt 2pt 0; }
.ex-desc { margin: 4pt 0 6pt 0; }
.sec { margin: 5pt 0; break-inside: avoid; }
.sec::after { content: ""; display: block; clear: both; }
.sec-label { float: left; width: 2.6cm; font-size: 7.2pt; font-weight: bold; text-transform: uppercase;
             letter-spacing: 0.6pt; color: #1e3a8a; padding-top: 1.6pt; }
.sec-body { margin-left: 2.75cm; }
.sec-body > p:last-child, .sec-body > ul:last-child { margin-bottom: 0; }
.sec-body ul { padding-left: 12pt; }
.notes .sec-body { color: #334155; }

/* ---- przykłady ---- */
.example { margin: 7pt 0; break-inside: avoid; }
.example-label { font-size: 7.6pt; font-weight: bold; text-transform: uppercase; letter-spacing: 0.6pt;
                 color: #1e3a8a; margin-bottom: 2pt; }
.io-row { display: flex; gap: 8pt; }
.stacked .io-row { display: block; }
.stacked .io-row .io-cell + .io-cell { margin-top: 4pt; }
.io-cell { flex: 1; min-width: 0; }
.io-cell.wide { margin-bottom: 4pt; }
.io-head { font-size: 7pt; color: var(--muted); text-transform: uppercase; letter-spacing: 0.8pt; margin-bottom: 1pt; }
.io { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.4pt; line-height: 1.38; background: var(--code-bg);
      border: 0.6pt solid var(--line); border-radius: 3pt; padding: 4pt 6pt; color: #0f172a; }
.io.empty { color: #94a3b8; font-style: italic; font-family: 'DejaVu Sans', sans-serif; }
.io.files .path { color: #1d4ed8; font-weight: bold; }
.muted { color: #94a3b8; }
.explanation { font-size: 9pt; color: #475569; margin-top: 3pt; padding-left: 8pt; border-left: 2pt solid var(--line); }
.explanation p:last-child { margin-bottom: 0; }

/* ---- kod ---- */
.code { font-size: 8.3pt; line-height: 1.4; background: var(--code-bg); border: 0.6pt solid var(--line);
        border-left: 2.5pt solid var(--accent); border-radius: 3pt; padding: 5pt 7pt; color: #0f172a; }
.ex-desc pre, .sec-body > pre, .notes pre, .chapter-desc pre {
        font-size: 8.3pt; line-height: 1.4; background: var(--code-bg); border: 0.6pt solid var(--line);
        border-radius: 3pt; padding: 4pt 6pt; margin: 3pt 0 6pt 0; }
.starter { margin: 7pt 0; }
.starter .example-label { break-after: avoid; }
.starter.short .code { break-inside: avoid; }
.starter .code { break-inside: auto; }

/* ---- wprowadzenie do rozdziału (podrecznik/) ---- */
.primer { font-size: 9.8pt; line-height: 1.55; margin: 4pt 0 10pt 0; }
.primer p { margin: 0 0 6pt 0; text-align: justify; }
.primer h2 { font-family: 'DejaVu Serif', serif; font-size: 14pt; color: #0f172a; margin: 16pt 0 6pt 0;
             padding-bottom: 2pt; border-bottom: 1pt solid var(--line); bookmark-level: none; }
.primer h2:first-child { margin-top: 6pt; }
.primer h3 { font-size: 11pt; color: #1e3a8a; margin: 10pt 0 4pt 0; bookmark-level: none; }
.primer ul, .primer ol { margin: 2pt 0 7pt 0; }
.primer table { margin: 6pt auto 9pt auto; font-size: 9pt; break-inside: avoid; }
.primer th { background: #1e3a8a; color: #fff; font-weight: bold; padding: 3pt 8pt; text-align: left; }
.primer th code { background: rgba(255, 255, 255, 0.16); color: #fff; }
.primer td { border-bottom: 0.6pt solid var(--line); padding: 2.5pt 8pt; }
.primer tr:nth-child(even) td { background: #f8fafc; }
.primer .code { margin: 4pt 0 8pt 0; break-inside: avoid; }
.primer pre:not(.code) { font-size: 8.3pt; background: var(--code-bg); border: 0.6pt solid var(--line);
                         border-radius: 3pt; padding: 4pt 6pt; margin: 4pt 0 8pt 0; }
figure { margin: 8pt 0 10pt 0; text-align: center; break-inside: avoid; }
figure img { max-width: 100%; }
figcaption { font-size: 8.4pt; color: var(--muted); margin-top: 4pt; }
.fig-no { font-weight: bold; color: #1e3a8a; }
.math-display { text-align: center; margin: 6pt 0 9pt 0; font-size: 1.12em; }
.math .mtt { font-family: 'DejaVu Sans Mono', monospace; font-style: normal; font-size: 0.9em; }
.math .overline { border-top: 0.6pt solid currentColor; }
.math .underbrace { display: inline-block; vertical-align: top; text-align: center; }
.math .underbrace > span { display: block; }
.math .underbrace .ub-body { border-bottom: 0.7pt solid currentColor; border-radius: 0 0 4pt 4pt; padding: 0 2pt 1pt 2pt; }
.math .ub-label { font-size: 0.72em; margin-top: 1pt; }
blockquote { margin: 6pt 0 9pt 0; padding: 5pt 10pt; border-left: 3pt solid var(--accent);
             background: #eff6ff; border-radius: 0 4pt 4pt 0; break-inside: avoid; }
blockquote p:last-child { margin-bottom: 0; }
blockquote.warn { border-left-color: #dc2626; background: #fef2f2; }
blockquote.warn strong:first-child { color: #b91c1c; }
blockquote.tip { border-left-color: #16a34a; background: #f0fdf4; }
blockquote.tip strong:first-child { color: #15803d; }
blockquote.def { border-left-color: #7c3aed; background: #f5f3ff; }
blockquote.def strong:first-child { color: #6d28d9; }
.tasks-heading { font-family: 'DejaVu Serif', serif; font-size: 18pt; color: #0f172a; margin: 0 0 10pt 0;
                 break-before: page; bookmark-level: 2; bookmark-label: "Zadania"; }

/* ---- wizualizacja rozwiązań ---- */
.numbered .cl { display: block; padding-left: 26pt; text-indent: -26pt; }
.numbered .ln { color: #94a3b8; display: inline-block; width: 16pt; margin-right: 6pt; text-align: right;
                border-right: 0.6pt solid var(--line); padding-right: 4pt; text-indent: 0; }
.viz { margin: 5pt 0 4pt 0; break-inside: avoid; }
.viz-head { font-size: 7.6pt; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5pt; color: #1e3a8a;
            margin-bottom: 3pt; }
.viz-head code { text-transform: none; letter-spacing: 0; font-weight: normal; }
.viz-note { font-size: 7.4pt; color: var(--muted); margin-top: 2pt; }
.trace { width: 100%; font-size: 7.6pt; border: 0.6pt solid var(--line); }
.trace th { background: var(--soft); color: #334155; font-weight: bold; padding: 2pt 4pt; text-align: left;
            border-bottom: 0.8pt solid #cbd5e1; vertical-align: bottom; }
.trace th code { background: none; padding: 0; font-size: 7.8pt; color: #1e3a8a; }
.trace .t-scope { display: block; font-weight: normal; color: #94a3b8; font-size: 6.4pt; }
.trace td { padding: 1.2pt 4pt; border-bottom: 0.4pt solid #eef2f7; font-family: 'DejaVu Sans Mono', monospace; }
.trace td.t-line { white-space: nowrap; }
.trace td.t-line code { background: none; padding: 0; font-size: 7.4pt; }
.trace .t-ln { display: inline-block; min-width: 12pt; color: #94a3b8; text-align: right; }
.trace td.t-val { color: #94a3b8; white-space: nowrap; }
.trace td.chg { color: #0f172a; background: #fef3c7; font-weight: bold; }
.trace td.t-out { color: #15803d; white-space: nowrap; }
.trace .t-skip td { text-align: center; color: #94a3b8; font-family: 'DejaVu Sans', sans-serif; background: #f8fafc; }
.call-tree { display: block; margin: 2pt auto; max-width: 100%; }

/* ---- dodatek z rozwiązaniami ---- */
.sol-chapter { font-family: 'DejaVu Serif', serif; font-size: 14pt; color: #0f172a; margin: 16pt 0 6pt 0;
               padding-bottom: 3pt; border-bottom: 1.5pt solid var(--accent-2); bookmark-level: 2;
               string-set: chapter "Rozwiązania · " content(); }
.solution { margin: 7pt 0 9pt 0; }
.sol-head { display: flex; align-items: center; gap: 6pt; margin-bottom: 3pt; break-after: avoid; }
.sol-title { font-weight: bold; font-size: 9.6pt; }
.back-ref { margin-left: auto; font-size: 7.8pt; color: var(--muted); }
.back-ref::after { content: " → s. " target-counter(attr(href url), page); }
.solution .code { break-inside: auto; }
"""


def build_css() -> str:
    pygments_css = ""
    if highlight:
        pygments_css = _FORMATTER.get_style_defs(".hl")
        # Tło i ramkę bloku ustala .code — z motywu bierzemy tylko kolory tokenów.
        pygments_css = re.sub(r"^\.hl\s*\{[^}]*\}\n?", "", pygments_css, flags=re.M)
        pygments_css = re.sub(r"^pre \{[^}]*\}\n?", "", pygments_css, flags=re.M)
        pygments_css = re.sub(
            r"^td\.linenos[^\n]*\n|^span\.linenos[^\n]*\n|^\.hl \.hll[^\n]*\n",
            "",
            pygments_css,
            flags=re.M,
        )
    return CSS.replace("PYGMENTS_CSS", pygments_css)


# --------------------------------------------------------------------------- całość


def build_html(chapters: Dict[str, Dict[str, Any]], with_solutions: bool) -> str:
    title = "Nauka Programowania — " + (
        "Zbiór zadań z rozwiązaniami" if with_solutions else "Zbiór zadań"
    )
    body = [
        cover_html(chapters, with_solutions),
        how_to_html(with_solutions),
        toc_html(chapters, with_solutions),
    ]
    body += [
        chapter_html(stem, chapter, with_solutions)
        for stem, chapter in chapters.items()
    ]
    if with_solutions:
        body.append(solutions_html(chapters))
    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<title>{esc(title)}</title>
<meta name="author" content="{AUTHOR}">
<meta name="description" content="Zbiór zadań programistycznych od podstaw: wejście/wyjście, warunki, pętle, funkcje, listy, napisy, rekurencja, klasy, pliki, sortowanie, wyrażenia regularne.">
<meta name="keywords" content="programowanie, Python, zadania, nauka programowania, algorytmy">
<meta name="generator" content="scripts/generate_pdf.py">
<style>{build_css()}</style>
</head>
<body>
{chr(10).join(body)}
</body>
</html>
"""


def load(prefixes: Optional[List[str]]) -> Tuple[Dict[str, Dict[str, Any]], List[str]]:
    problems = md_to_json.Problems()
    chapters = md_to_json.load_chapters(
        TASKS_DIR, TESTS_DIR, ["szablon.md"], problems, prefixes
    )
    if problems.items:
        print(
            f"Uwaga: treści mają problemy ({len(problems.items)}) — szczegóły: md_to_json.py --validate"
        )
        for item in problems.items[:10]:
            print(f"  - {item}")
    return chapters, problems.items


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-o", "--output", type=Path, help="plik PDF (domyślnie w katalogu repozytorium)"
    )
    parser.add_argument(
        "--rozwiazania",
        action="store_true",
        help="dołącz dodatek z rozwiązaniami w Pythonie",
    )
    parser.add_argument(
        "--rozdzialy",
        nargs="+",
        metavar="NN",
        help="tylko wybrane rozdziały (prefiks nazwy pliku)",
    )
    parser.add_argument(
        "--html", type=Path, help="zapisz też HTML (np. do podglądu w przeglądarce)"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="błąd, gdy treści mają problemy lub wzory używają nieobsługiwanych poleceń LaTeX-a (CI)",
    )
    args = parser.parse_args()

    chapters, problems = load(args.rozdzialy)
    if not chapters:
        print("Nie znaleziono rozdziałów.", file=sys.stderr)
        return 1
    document = build_html(chapters, args.rozwiazania)
    if LATEX.unknown:
        print(
            "Uwaga: nieobsługiwane polecenia LaTeX-a (dodaj je do LatexToHtml): "
            + ", ".join(f"\\{name}" for name in sorted(LATEX.unknown))
        )
    if MISSING_FIGURES:
        print("Błąd: brak plików rysunków: " + ", ".join(sorted(set(MISSING_FIGURES))))
    if args.strict and (problems or LATEX.unknown or MISSING_FIGURES):
        return 1

    if args.html:
        args.html.write_text(document, encoding="utf-8")
        print(f"HTML: {args.html}")
        if not args.output:
            return 0

    from weasyprint import HTML

    output = args.output or REPO_ROOT / (
        DEFAULT_OUTPUT_SOLUTIONS if args.rozwiazania else DEFAULT_OUTPUT
    )
    total = sum(len(c["exercises"]) for c in chapters.values())
    print(f"Składanie PDF: {len(chapters)} rozdz., {total} zad. ...")
    pdf = HTML(string=document, base_url=str(REPO_ROOT)).render()
    pdf.write_pdf(output)
    size_mb = output.stat().st_size / (1024 * 1024)
    print(f"Gotowe: {output} ({len(pdf.pages)} stron, {size_mb:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
