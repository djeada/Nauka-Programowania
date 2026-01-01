"""
ZAD-05 — Zbiór potęgowy listy

**Poziom:** ★★★
**Tagi:** `list`, `subsets`, `combinatorics`

### Treść

Otrzymujesz listę liczb naturalnych (mogą występować powtórzenia). Wygeneruj zbiór wszystkich możliwych podzbiorów tej listy.

Wynik ma zawierać wszystkie podzbiory (włącznie z pustym).

### Wejście

* 1 linia: lista liczb naturalnych `A`

### Wyjście

* 1 linia: lista list (wszystkie podzbiory)

### Przykład

**Wejście:**

```
[1, 2, 1]
```

**Wyjście:**

```
[[], [1], [2], [1, 2], [1, 1], [2, 1], [1, 1, 2], [1, 2, 1]]
```

### Uwagi

* Jeśli sprawdzarka wymaga konkretnej kolejności podzbiorów, musi być ona opisana w treści — w przeciwnym razie dopuszczalna może być dowolna. (Jeśli chcesz, mogę dopisać sztywną konwencję kolejności, ale bez rozwiązań.)

"""


# Zlozonosc O(n.2^n)
def zbior_potegowy(lista):
    # wymaga sortowania O(nlogn)
    lista.sort()

    N = int(pow(2, len(lista)))
    zbior_potegowy = set()

    for i in range(N):
        subset = [lista[j] for j in range(len(lista)) if i & (1 << j)]
        zbior_potegowy.add(tuple(subset))

    return zbior_potegowy


# Testy Poprawnosci
def test_1():
    lista = [1, 2, 1]
    wynik = {(1, 2), (1,), (2,), (1, 1, 2), (), (1, 1)}

    assert sorted(zbior_potegowy(lista)) == sorted(wynik)


def test_2():
    lista = [5, 3]
    wynik = {(), (3,), (3, 5), (5,)}

    assert sorted(zbior_potegowy(lista)) == sorted(wynik)


def test_3():
    lista = []
    wynik = {()}

    assert zbior_potegowy(lista) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
