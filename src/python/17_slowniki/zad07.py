r"""
ZAD-07 — Histogram słów w tekście (ignoruj wielkość liter)

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`, `tekst`

### Treść

Wczytaj tekst. Policz, ile razy występuje w nim każde słowo, nie rozróżniając wielkości liter. Wypisz słownik: słowo (małymi literami) → liczba wystąpień.

### Wejście

* 1. linia: tekst

### Wyjście

Słownik w postaci `{'słowo': liczba, …}` — słowa zapisane małymi literami, w kolejności pierwszego wystąpienia w tekście. Jeśli w tekście nie ma żadnego słowa — `{}`.

### Ograniczenia

* tekst ma od 1 do 300 znaków

### Przykład

**Wejście:**

```
Ala ma kota. Ala lubi koty.
```

**Wyjście:**

```
{'ala': 2, 'ma': 1, 'kota': 1, 'lubi': 1, 'koty': 1}
```

### Uwagi

* **Słowo** to najdłuższy ciąg kolejnych liter (także polskich, np. `ż`, `ó`). Wszystkie inne znaki — spacje, cyfry, znaki interpunkcyjne — rozdzielają słowa.
* `Kot`, `KOT` i `kot` to to samo słowo `kot`.

"""


def podziel_na_slowa(tekst):
    """Zwraca listę słów (ciągów liter) zapisanych małymi literami."""
    bez_innych_znakow = ""
    for znak in tekst:
        if znak.isalpha():
            bez_innych_znakow += znak.lower()
        else:
            bez_innych_znakow += " "
    return bez_innych_znakow.split()


def histogram_slow(tekst):
    """Zwraca słownik: słowo -> liczba wystąpień (w kolejności pierwszego wystąpienia)."""
    histogram = {}
    for slowo in podziel_na_slowa(tekst):
        histogram[slowo] = histogram.get(slowo, 0) + 1
    return histogram


if __name__ == "__main__":
    print(histogram_slow(input()))
