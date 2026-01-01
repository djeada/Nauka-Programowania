"""
ZAD-05 — Liczby z przedziału

**Poziom:** ★☆☆
**Tagi:** `pętle`, `przedziały`, `modulo`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Najpierw ustal:

* `lo = min(a, b)`
* `hi = max(a, b)`

Następnie:

a) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` (każda w osobnej linii).

b) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` oraz `x` jest podzielne przez `3` (każda w osobnej linii).

### Wejście

Dwie liczby naturalne:

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Najpierw wyniki podpunktu (a), potem wyniki podpunktu (b), każda liczba w osobnej linii.

### Przykład

**Wejście:**

```
9
5
```

**Wyjście:**

```
6
7
8
6
```

### Uwagi o formatowaniu

* Nie wypisuj nagłówków typu „a)” i „b)”.
* Jeśli w którymś podpunkcie nie ma liczb do wypisania, w tej części nie wypisuj nic.
* Nie dodawaj pustej linii między podpunktami.

"""

if __name__ == "__main__":

    print("Podaj dwie liczby: ")
    pierwsza_liczba = int(input())
    druga_liczba = int(input())

    print(
        "Liczby naturalne wieksze od mniejszej pobranej liczby i jednoczesnie mniejsze od wiekszej pobranej liczby:"
    )
    if pierwsza_liczba > druga_liczba:
        for i in range(druga_liczba, pierwsza_liczba + 1):
            print(i)
    else:
        for i in range(pierwsza_liczba, druga_liczba + 1):
            print(i)

    print("\n")
    print(
        "Liczby naturalne podzielne przez 3 wieksze od mniejszej pobranej liczby i jednoczesnie mniejsze od wiekszej pobranej liczby:"
    )

    if pierwsza_liczba > druga_liczba:
        for i in range(druga_liczba, pierwsza_liczba + 1):
            if i % 3 == 0:
                print(i)
    else:
        for i in range(pierwsza_liczba, druga_liczba + 1):
            if i % 3 == 0:
                print(i)
