# Jak współtworzyć zbiór zadań

Repozytorium ma trzy warstwy, które muszą być ze sobą zgodne:

| Warstwa | Pliki | Rola |
|---|---|---|
| Treści zadań | `zbior_zadan/NN_*.md` | Źródło prawdy o treści, formacie wejścia/wyjścia i przykładach. |
| Testy | `zbior_zadan_tests/NN_*.json` | Ukryte przypadki testowe dla każdego zadania. |
| Rozwiązania | `src/<język>/NN_*/` | Rozwiązania w 7 językach; **Python jest rozwiązaniem wzorcowym**. |

`zbior_zadan_json/` jest generowany automatycznie (`scripts/md_to_json.py`) i stanowi publiczne API
zbioru — korzysta z niego m.in. [kurs Pythona z automatyczną sprawdzarką](https://adamdjellouli.com/courses/kurs_podstaw_pythona/).
Nie edytuj tych plików ręcznie.

## Szybka ścieżka

```bash
python3 scripts/md_to_json.py          # walidacja treści + regeneracja JSON
python3 scripts/run_tests.py 07        # rozwiązania wzorcowe z rozdziału 07 na testach i przykładach
python3 scripts/generate_readme.py     # odświeżenie tabel w README
bash scripts/check_sources.sh          # kompilacja/składnia wszystkich języków
```

CI uruchamia te same polecenia dla każdego pull requesta.

## Zasady pisania zadań

Szablon zadania: [`zbior_zadan/szablon.md`](zbior_zadan/szablon.md).

1. **Każde zadanie to program stdin → stdout.** Także zadania o funkcjach: treść mówi, jaką funkcję
   napisać, a program wczytuje dane, wywołuje funkcję i wypisuje wynik. Dzięki temu każde zadanie
   da się sprawdzić automatycznie.
2. **Wejście bez literałów Pythona.** Dane podajemy tak, by dało się je wczytać przez `input()`,
   `int()` i `split()` (np. `3 2 1`, a nie `[3, 2, 1]`).
3. **Wyjście jednoznaczne.** Opisz dokładnie format (separator, liczba miejsc po przecinku,
   wielkość liter, komunikat dla przypadków brzegowych). Program nie wypisuje komunikatów typu
   „Podaj liczbę:”.
4. **Wzory w LaTeX-u** między `$…$`, np. `$\frac{1}{2} a h$`. Nie używaj zapisu `( … )`.
5. **Przykład zgodny z testami.** Przykłady są sprawdzane tak samo jak testy.
6. **Stabilne identyfikatory.** `ZAD-NN` jest częścią adresu zadania na stronie i kluczem postępu
   ucznia — nie zmieniaj numeracji istniejących zadań.

## Zasady pisania testów

Plik `zbior_zadan_tests/NN_*.json` to słownik `{"ZAD-NN": [{"input": "…", "output": "…"}, …]}`.

* Co najmniej **4 testy** na zadanie, wszystkie różne i różne od przykładu.
* Testy obejmują przypadki brzegowe (0, 1, liczby ujemne, pusty napis, maksimum z ograniczeń…).
* Testy mają różne oczekiwane wyjścia, żeby nie dało się ich zaliczyć wypisując stałą
  (wyjątek: zadania, w których wynik z definicji jest stały, np. „Witaj, świecie!”).
* Zadanie interaktywne (bez automatycznej oceny) ma pustą listę: `"ZAD-11": []`.
* Zadania na plikach używają pól `files` (pliki przed uruchomieniem) i `expected_files`
  (stan po uruchomieniu, `null` = plik ma nie istnieć). Szczegóły: `scripts/judge_harness.py`.
  Przykłady w treści opisują pliki znacznikami `**Pliki przed:**` / `**Pliki po:**` (format w `szablon.md`).

Sposób porównywania wyników (identyczny w CI i na stronie): końcowe spacje i puste linie są
ignorowane, liczba linii musi się zgadzać, tekst musi być identyczny, a liczby mogą różnić się
o 0,01.

## Rozwiązania

* Python: `src/python/NN_*/zadNN.py`, a dla podpunktów `zadNNa.py`, `zadNNb.py`… Każdy plik czyta
  stdin i przechodzi wszystkie testy (`scripts/run_tests.py`). Logikę umieść w funkcjach,
  a wczytywanie danych w bloku `if __name__ == "__main__":`.
* Pozostałe języki: `zadNN.<ext>` (Java: `zadN/Main.java`). Muszą się kompilować
  (`scripts/check_sources.sh`).
* Opis zadania na początku pliku generuje `scripts/update_descriptions.py` — nie edytuj go ręcznie.

## Pull request

1. Zrób fork i sklonuj repozytorium: `git clone https://github.com/djeada/Nauka-Programowania.git`.
2. Utwórz gałąź: `git checkout -b moja-zmiana`.
3. Uruchom polecenia z sekcji „Szybka ścieżka” i zacommituj także wygenerowane pliki.
4. Otwórz pull request z krótkim opisem zmiany.
