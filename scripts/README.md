# Skrypty

Wszystkie polecenia uruchamiaj z katalogu głównego repozytorium. Poza `generate_pdf.py`
skrypty używają wyłącznie biblioteki standardowej Pythona (3.8+).

| Skrypt | Co robi | W CI |
|---|---|---|
| `md_to_json.py` | Waliduje `zbior_zadan/*.md` + `zbior_zadan_tests/*.json` i generuje `zbior_zadan_json/*.json`. | `--check` |
| `run_tests.py` | Uruchamia rozwiązania wzorcowe z `src/python` na testach i przykładach. | ✓ |
| `run_tests_pyodide.mjs` | To samo co `run_tests.py`, ale w Pyodide (Python w WebAssembly), czyli w środowisku kursu online. | ✓ |
| `judge_harness.py` | Sędzia: uruchomienie programu i porównanie wyniku. Wspólny dla CI i strony kursu. | (używany przez `run_tests.py`) |
| `generate_readme.py` | Generuje indeks zadań i statystyki w `README.md`. | `--check` |
| `check_sources.sh` | Kompilacja / sprawdzenie składni rozwiązań we wszystkich językach. | ✓ (`--lang …`) |
| `update_descriptions.py` | Wstawia treść zadania jako komentarz na początku plików z rozwiązaniami. | — |
| `format_all.sh` | Formatuje kod (black, clang-format, prettier, rustfmt, ormolu, shfmt). | — |
| `generate_pdf.py` | Składa wszystkie treści w jeden PDF. | — |

## Typowy przebieg pracy

```bash
# 1. edytuj zbior_zadan/NN_*.md, zbior_zadan_tests/NN_*.json, src/python/NN_*/
python3 scripts/md_to_json.py --validate --chapters NN   # szybka walidacja jednego rozdziału
python3 scripts/run_tests.py NN -v                         # rozwiązania wzorcowe na testach

# 2. przed commitem
python3 scripts/md_to_json.py          # regeneracja JSON
python3 scripts/generate_readme.py     # regeneracja README
python3 scripts/update_descriptions.py # odświeżenie opisów w plikach rozwiązań (opcjonalnie)
bash scripts/check_sources.sh
```

## md_to_json.py

Format zadań opisuje [`zbior_zadan/szablon.md`](../zbior_zadan/szablon.md), a zasady
[`CONTRIBUTING.md`](../CONTRIBUTING.md). Skrypt kończy się błędem, gdy:

* zadanie ma nieznaną sekcję, brak treści, wejścia, wyjścia lub przykładu,
* przykład nie ma pary **Wejście:** / **Wyjście:** (np. używa „Wywołanie funkcji”),
* zadanie nie ma testów lub ma ich mniej niż 4 (1 dla zadań bez wejścia), testy się powtarzają albo
  powtarzają wejście z przykładu,
* plik z testami zawiera klucz nieistniejącego zadania.

Opcje: `--check` (CI: nie zapisuje, sprawdza aktualność plików), `--validate` (tylko walidacja),
`--chapters 03 15` (z `--validate`), `--lenient` (raportuje, ale nie przerywa).

### Schemat JSON

```json
{
  "file": "02_instrukcja_warunkowa.md",
  "chapter_title": "Rozdział 2: Instrukcja warunkowa",
  "chapter_description": "markdown",
  "exercises": [
    {
      "id": "ZAD-02",
      "slug": "02_instrukcja_warunkowa/ZAD-02",
      "title": "Porównanie dwóch liczb",
      "difficulty": 1,
      "difficulty_display": "★☆☆",
      "tags": ["if-else"],
      "description": "markdown; wzory LaTeX w $...$",
      "input": "markdown",
      "output": "markdown",
      "examples": [{"input": "7\n4", "output": "Liczby są różne.", "explanation": ""}],
      "testcases": [{"input": "9\n9", "output": "Liczby są identyczne."}],
      "constraints": "markdown",
      "notes": "markdown",
      "starter_code": "kod startowy w Pythonie albo pusty napis"
    }
  ]
}
```

Przypadek testowy może mieć pola `files` i `expected_files` (zadania na plikach) — opis w
`judge_harness.py`. Pusta lista `testcases` oznacza zadanie interaktywne.

**Stabilność API:** `slug` jest kluczem adresu zadania i postępu ucznia na stronie kursu —
nie zmieniaj identyfikatorów istniejących zadań.

## judge_harness.py

Zasady oceny (identyczne w CI i w przeglądarce): końcowe spacje i puste linie na końcu są
ignorowane, liczba linii musi się zgadzać, tekst musi być identyczny, liczby mogą się różnić
o 0,01 (lub względnie o 1e-9). Tekst przekazany do `input("…")` nie jest wypisywany.
Strona kursu kopiuje ten plik bez zmian (`scripts/sync_course_tasks.py` w repozytorium Personal-Website),
więc każda zmiana zasad oceny trafia tam przy następnej synchronizacji.

## generate_pdf.py

Składa wszystkie treści z `zbior_zadan` w jeden dokument A4 ze stroną tytułową i spisem treści.

```bash
pip install -r scripts/requirements-pdf.txt
python3 scripts/generate_pdf.py   # -> Nauka_Programowania_Zbior_Zadan.pdf (ignorowany przez git)
```

## update_descriptions.py

Wstawia treść zadania z `zbior_zadan` jako komentarz na początku każdego pliku z rozwiązaniem
(w Pythonie jako surowy docstring `r"""…"""`). Dla Pythona każdy podpunkt (`ZAD-05A`) ma osobny
plik `zad05a.py`; w pozostałych językach podpunkty dzielą plik `zad05.<ext>`.

```bash
python3 scripts/update_descriptions.py                       # wszystkie języki
python3 scripts/update_descriptions.py zbior_zadan/ src/python/ py
```
