r"""
ZAD-06 — Histogram znaków w słowie

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Utwórz słownik, w którym kluczami są znaki napisu, a wartościami liczby ich wystąpień, i wypisz go.

### Wejście

* 1. linia: napis

### Wyjście

Słownik w postaci `{'znak': liczba, …}` — znaki w kolejności pierwszego wystąpienia w napisie.

### Ograniczenia

* napis ma od 1 do 100 znaków, nie zaczyna się ani nie kończy spacją i nie zawiera apostrofów, cudzysłowów ani znaku `\`

### Przykład

**Wejście:**

```
klasa
```

**Wyjście:**

```
{'k': 1, 'l': 1, 'a': 2, 's': 1}
```

### Uwagi

* Liczą się wszystkie znaki, także spacje (klucz `' '`) i cyfry.
* Wielkość liter ma znaczenie: `a` i `A` to różne znaki.

"""


def histogram_znakow(napis):
    """Zwraca słownik: znak -> liczba wystąpień (w kolejności pierwszego wystąpienia)."""
    histogram = {}
    for znak in napis:
        if znak in histogram:
            histogram[znak] += 1
        else:
            histogram[znak] = 1
    return histogram


if __name__ == "__main__":
    print(histogram_znakow(input()))
