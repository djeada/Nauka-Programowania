r"""
ZAD-04B — Ograniczenie liczby do przedziału

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`, `max`

### Treść

Napisz funkcję `ogranicz(x, dolna, gorna)`, która „przycina” liczbę `x` do przedziału $[\text{dolna}, \text{gorna}]$ i zwraca:

* `dolna`, jeśli $x < \text{dolna}$,
* `gorna`, jeśli $x > \text{gorna}$,
* samo `x` w pozostałych przypadkach (gdy $\text{dolna} \le x \le \text{gorna}$).

Program wczytuje `x`, `dolna` i `gorna`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `x`
* 2. linia: liczba całkowita `dolna` — lewy koniec przedziału
* 3. linia: liczba całkowita `gorna` — prawy koniec przedziału

### Wyjście

Jedna liczba całkowita: wartość `x` ograniczona do przedziału $[\text{dolna}, \text{gorna}]$.

### Ograniczenia

* $\text{dolna} \le \text{gorna}$
* $-10^9 \le x, \text{dolna}, \text{gorna} \le 10^9$

### Przykład

**Wejście:**

```
15
0
10
```

**Wyjście:**

```
10
```

Liczba $15$ wychodzi poza przedział $[0, 10]$ z prawej strony, więc zostaje zastąpiona prawym końcem — $10$.

### Uwagi

* Funkcja przydaje się np. w grach, gdy pozycja postaci nie może wyjść poza planszę, albo gdy głośność ma się mieścić w zakresie od $0$ do $100$.
* Całe ciało funkcji da się zapisać jednym wyrażeniem złożonym z minimum i maksimum dwóch liczb: najpierw $\max(x, \text{dolna})$, a z tego wyniku $\min(\ldots, \text{gorna})$. Możesz skorzystać z funkcji `min_z_dwoch` z zadania ZAD-04A.

### Kod startowy

```python
def ogranicz(x, dolna, gorna):
    pass


x = int(input())
dolna = int(input())
gorna = int(input())
print(ogranicz(x, dolna, gorna))
```

"""


def min_z_dwoch(a, b):
    """Zwraca mniejszą z dwóch liczb."""
    if a < b:
        return a
    return b


def ogranicz(x, dolna, gorna):
    """Zwraca x przycięte do przedziału [dolna, gorna]."""
    if x < dolna:
        x = dolna
    return min_z_dwoch(x, gorna)


if __name__ == "__main__":
    x = int(input())
    dolna = int(input())
    gorna = int(input())
    print(ogranicz(x, dolna, gorna))
