# Podręcznik: wprowadzenia do rozdziałów

Każdy rozdział zbioru zadań w wersji PDF zaczyna się od **wprowadzenia**: krótkiej teorii
z diagramami, wzorami i rozwiązanym przykładem. Wprowadzenia są tylko w PDF-ie
(`scripts/generate_pdf.py`) — nie trafiają do JSON-ów ani na stronę kursu.

```
podrecznik/
├── 02_instrukcja_warunkowa.md     # wprowadzenie; nazwa = nazwa pliku rozdziału w zbior_zadan/
└── diagramy/
    ├── preambula.tex              # wspólne kolory, style i makra TikZ
    ├── 02_if_else.tex             # źródło diagramu (jedno środowisko tikzpicture)
    └── svg/02_if_else.svg         # wygenerowane przez scripts/build_diagrams.py (commitowane)
```

Wzorem jest [`02_instrukcja_warunkowa.md`](02_instrukcja_warunkowa.md).

## Budowa wprowadzenia

1. `# Rozdział N: Tytuł — wprowadzenie` — pomijany w PDF-ie (tytuł jest w nagłówku rozdziału).
2. `## Czego się nauczysz` — 3–5 punktów.
3. 2–5 sekcji `##` z teorią potrzebną do zadań z rozdziału: pojęcie → krótki kod → diagram.
   Pisz do ucznia („wczytujesz”, „zauważ”), krótko i konkretnie. Każdy fragment kodu ma działać.
4. `## Przykład rozwiązany: …` — problem **inny niż zadania z rozdziału** (nie zdradzaj
   rozwiązań!), rozpisany krok po kroku: analiza (najlepiej z diagramem), kod, sprawdzenie
   (tabela stanu zmiennych albo diagram kolejnych kroków).
5. `## Typowe błędy` — 3–6 punktów, każdy z wyjaśnieniem, jak go uniknąć.

Objętość: 1,5–3 strony PDF-u, 2–4 diagramy.

## Składnia

* **Wzory:** `$a^2 + b^2 = c^2$` w tekście, `$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$` jako
  osobny wiersz (wyśrodkowany). Konwerter (`LatexToHtml` w `generate_pdf.py`) obsługuje
  indeksy `^ _`, `\frac`, `\sqrt`, `\binom`, `\left( … \right)`, `\text{}`, `\texttt{}`,
  `\overline{}`, `\underbrace{…}_{opis}`, greckie litery, relacje (`\le \ge \ne \approx \equiv \in \to \Rightarrow`),
  działania (`\cdot \times \pm \land \lor \neg \oplus \bmod`), `\lfloor \rceil`, `\sum \prod`,
  `\log \sin \max …`, odstępy `\, \; \quad \qquad`. Bez `\begin{…}` (macierze, `cases`) —
  takie rzeczy rysuj w TikZ albo tabelą. Nieznane polecenie przerywa `generate_pdf.py --strict`.
  We wzorze blokowym granice `\sum`/`\prod` stoją nad i pod znakiem. Odstępy dobierane są jak w TeX-u
  (odstępy w źródle wzoru nie mają znaczenia); wzór w tekście może przechodzić do następnej linii.
* **Rysunki:** `![Podpis rysunku](diagramy/svg/NN_nazwa.svg)` w osobnym akapicie. Tekst
  alternatywny staje się podpisem „Rys. N.k.”.
* **Ramki:** cytat zaczynający się od pogrubionego słowa —
  `> **Uwaga:** …` / `> **Pułapka:** …` (czerwone), `> **Wskazówka:** …` / `> **Pamiętaj:** …`
  (zielone), `> **Definicja:** …` / `> **Zapamiętaj:** …` (fioletowe), `> **Ciekawostka:** …` (niebieskie).
* Tabele markdown, listy, bloki ```` ```python ```` (kolorowanie składni).

## Diagramy (TikZ)

Plik `diagramy/NN_nazwa.tex` zawiera **tylko** `\begin{tikzpicture} … \end{tikzpicture}`;
preambułę dokleja skrypt. Korzystaj ze stylów z `preambula.tex` zamiast własnych kolorów:

| Styl / makro | Do czego |
|---|---|
| `start`, `blok`, `decyzja`, `we`, `strzalka`, `tak`, `nie` | schematy blokowe |
| `komorka`, `komorka wyr`, `komorka ok`, `komorka zla`, `komorka szara`, `indeks`, `wskaznik` | listy, napisy, macierze |
| `\tablica{nazwa}{x}{y}{3,1,4}` / `\tablicabez{…}` | rząd komórek (węzły `nazwa-0`, `nazwa-1`, …) |
| `zmienna` | pudełko zmiennej w pamięci |
| `kod`, `podpis`, `notka`, `ramka`, `klamra` | opisy, ramki z kodem, klamry |
| kolory `akcent`, `bursztyn`, `fiolet`, `czerwien`, `zielen` (+ `…jasny/jasna`), `tusz`, `szary`, `linia`, `tlo` | wszystko inne |

Zasady: szerokość do ok. 16 cm, czcionka domyślna (`\small`), polskie znaki i symbole
`≠ ≤ ≥ ≈ → ← ⇒ − √ ∞ π ∈ ∑ ⌊ ⌋ ⌈ ⌉ ✓ ✗` wpisuj wprost, kod w `\kod{…}` (w `\kod` znaki
`_ # % & { }` poprzedzaj `\`; `<<`, `--` i `'` zostają dosłowne). Dostępne są też `amssymb`
(`\checkmark`) i `pifont` (`\ding{…}`). Makra `\tablica` nie wywołuj w `\foreach` z listą w makrze —
wtedy rysuj komórki pętlą wprost. Rysunek ma tłumaczyć
**mechanizm** (co się dzieje krok po kroku), a nie być ozdobą.

```bash
python3 scripts/build_diagrams.py               # buduje nowe/zmienione SVG (wymaga latex + dvisvgm)
python3 scripts/build_diagrams.py --check       # CI: SVG zgodne ze źródłami
python3 scripts/generate_pdf.py --rozdzialy 02 -o /tmp/r02.pdf --strict   # podgląd rozdziału
pdftoppm -r 80 -png -f 3 -l 8 /tmp/r02.pdf /tmp/r02                       # strony jako PNG
```
