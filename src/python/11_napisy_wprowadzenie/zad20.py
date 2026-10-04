r"""
ZAD-20 — Numerowanie wierszy do końca danych

**Poziom:** ★☆☆
**Tagi:** `napisy`, `sys.stdin`, `formatowanie`

### Treść

Wczytuj wiersze tekstu aż do **końca danych wejściowych** — nie wiadomo z góry, ile ich będzie. Wypisz wszystkie niepuste wiersze, poprzedzając każdy jego numerem w wejściu, a na końcu podaj, ile było wszystkich wierszy i ile niepustych.

Wiersz jest **pusty**, jeśli nie zawiera żadnych znaków albo zawiera same spacje. Puste wiersze nie są wypisywane, ale liczą się do numeracji.

### Wejście

* dowolna liczba wierszy tekstu (także zero)

### Wyjście

* Dla każdego niepustego wiersza jedna linia w formacie `nr | wiersz`, gdzie `nr` to numer wiersza w wejściu (od 1) wyrównany do prawej na szerokości 3 znaków, np. `  1 | Ala`, ` 12 | kot`. Wiersz wypisz bez zmian (z ewentualnymi spacjami na początku).
* Ostatnia linia: `Wierszy: X, niepustych: Y`.

### Przykład

**Wejście:**

```
Ala ma kota

Kot ma Alę
```

**Wyjście:**

```
  1 | Ala ma kota
  3 | Kot ma Alę
Wierszy: 3, niepustych: 2
```

### Uwagi

* Wszystkie wiersze aż do końca danych wczytasz za pomocą modułu `sys`: `sys.stdin.read().splitlines()` zwraca listę wierszy (bez znaków końca linii). Można też przejść po wierszach pętlą `for wiersz in sys.stdin:` — wtedy każdy wiersz kończy się znakiem `"\n"`, który usuniesz przez `wiersz.rstrip("\n")`.
* Wpisując dane ręcznie w konsoli, koniec danych zasygnalizujesz skrótem `Ctrl+D` (Linux, macOS) albo `Ctrl+Z` i `Enter` (Windows).
* Liczbę wyrównasz do prawej na szerokości 3 znaków w f-stringu: `f"{nr:>3}"`.
* Numerować wiersze pomoże `enumerate(wiersze, start=1)`.

### Kod startowy

```python
import sys

wiersze = sys.stdin.read().splitlines()

```

"""

import sys


def czy_pusty(wiersz):
    return wiersz.strip() == ""


def numeruj_wiersze(wiersze):
    niepuste = 0
    for nr, wiersz in enumerate(wiersze, start=1):
        if not czy_pusty(wiersz):
            print(f"{nr:>3} | {wiersz}")
            niepuste += 1
    print(f"Wierszy: {len(wiersze)}, niepustych: {niepuste}")


if __name__ == "__main__":
    wiersze = sys.stdin.read().splitlines()
    numeruj_wiersze(wiersze)
