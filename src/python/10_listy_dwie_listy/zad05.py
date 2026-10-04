r"""
ZAD-05 — Obliczenie średniej ważonej

**Poziom:** ★☆☆
**Tagi:** `listy`, `float`, `średnia`

### Treść

Wczytaj dwie listy liczb zmiennoprzecinkowych tej samej długości: listę wartości $x_1, x_2, \ldots, x_n$ oraz listę odpowiadających im wag $w_1, w_2, \ldots, w_n$.
Oblicz średnią ważoną wartości:
$\frac{x_1 w_1 + x_2 w_2 + \ldots + x_n w_n}{w_1 + w_2 + \ldots + w_n}$.

### Wejście

* 1. linia: wartości — liczby zmiennoprzecinkowe oddzielone spacjami
* 2. linia: wagi — liczby zmiennoprzecinkowe oddzielone spacjami (tyle samo co wartości)

### Wyjście

Jedna linia: średnia ważona zaokrąglona do **2 miejsc po przecinku** (np. `0.29`, `7.50`).

### Ograniczenia

* Wagi są nieujemne, a ich suma jest większa od zera.

### Przykład

**Wejście:**

```
0.2 0.4 0.1 0.2 0.1
2.0 5.0 0.0 2.0 1.0
```

**Wyjście:**

```
0.29
```

$\frac{0.2 \cdot 2 + 0.4 \cdot 5 + 0.1 \cdot 0 + 0.2 \cdot 2 + 0.1 \cdot 1}{2 + 5 + 0 + 2 + 1} = \frac{2.9}{10} = 0.29$.

### Uwagi

* Wynik sformatujesz np. tak: `print(f"{wynik:.2f}")`.

"""


def srednia_wazona(wartosci, wagi):
    suma_iloczynow = 0
    for wartosc, waga in zip(wartosci, wagi):
        suma_iloczynow += wartosc * waga
    return suma_iloczynow / sum(wagi)


if __name__ == "__main__":
    wartosci = [float(x) for x in input().split()]
    wagi = [float(x) for x in input().split()]

    print(f"{srednia_wazona(wartosci, wagi):.2f}")
