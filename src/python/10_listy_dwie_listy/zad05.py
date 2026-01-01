"""
ZAD-05 — Obliczenie średniej ważonej

**Poziom:** ★☆☆
**Tagi:** `list`, `float`

### Treść

Wczytaj dwie listy liczb zmiennoprzecinkowych tej samej długości:

* lista wartości,
* lista wag.

Oblicz średnią ważoną:
[
\frac{\sum (wartość_i \cdot waga_i)}{\sum waga_i}
]

### Wejście

* 1 linia: lista wartości (float)
* 2 linia: lista wag (float)

### Wyjście

* 1 linia: jedna liczba zmiennoprzecinkowa — średnia ważona **z dokładnością do 2 miejsc po przecinku**

### Przykład

**Wejście:**

```
[0.2, 0.4, 0.1, 0.2, 0.1]
[2.0, 5.0, 0.0, 2.0, 1.0]
```

**Wyjście:**

```
0.29
```

"""


def srednia_wazona(wartosci, wagi):

    if len(wartosci) != len(wagi):
        raise ValueError("Listy roznej dlugosci")

    suma = 0
    for waga, wartosc in zip(wagi, wartosci):
        suma += waga * wartosc

    return suma / sum(wartosci)


def test_srednia_wazona():
    assert srednia_wazona([1, 2, 3], [1, 1, 1]) == 1
    assert srednia_wazona([0, -23, -5, 2, -3, 4, 9], [1, 2, 3, 4, 5, 6, 7]) == -1.1875


if __name__ == "__main__":
    test_srednia_wazona()
