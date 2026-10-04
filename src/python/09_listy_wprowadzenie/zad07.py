r"""
ZAD-07 — Średnia dwóch największych liczb

**Poziom:** ★☆☆
**Tagi:** `listy`, `max`, `sortowanie`, `float`

### Treść

Wczytaj listę `n` liczb naturalnych. Znajdź dwa największe elementy listy i wypisz ich średnią arytmetyczną.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb naturalnych oddzielonych spacjami

### Wyjście

Jedna liczba: średnia dwóch największych elementów, z dokładnością do **jednego** miejsca po przecinku (np. `8.0`, `5.5`).

### Ograniczenia

* $n \ge 2$

### Przykład

**Wejście:**

```
6
9 2 3 2 1 7
```

**Wyjście:**

```
8.0
```

Dwa największe elementy to $9$ i $7$, a $\frac{9 + 7}{2} = 8$.

### Uwagi

* Jeśli największa wartość występuje w liście kilka razy, oba największe elementy mają tę samą wartość, np. dla `5 3 5` wynik to `5.0`.
* Liczbę z jednym miejscem po przecinku wypiszesz np. tak: `print(f"{wynik:.1f}")`.

"""


def srednia_dwoch_najwiekszych(lista):
    kopia = list(lista)
    najwieksza = max(kopia)
    kopia.remove(najwieksza)
    druga = max(kopia)
    return (najwieksza + druga) / 2


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(f"{srednia_dwoch_najwiekszych(lista):.1f}")
