"""
ZAD-02 — Przesuń zera na koniec listy

**Poziom:** ★★☆
**Tagi:** `list`, `stabilność`, `przekształcenie`

### Treść

Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, **zachowując kolejność** pozostałych elementów.

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista po przekształceniu

### Przykład

**Wejście:**

```
[0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
```

**Wyjście:**

```
[1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]
```

"""


# Wersja 1
def przesun_zera(lista):
    pierwotna_dlugosc = len(lista)
    lista = list(filter(lambda x: x != 0, lista))
    lista.extend([0] * (pierwotna_dlugosc - len(lista)))
    return lista


# Testy Poprawnosci
def test_1():
    lista = [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
    wynik = [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]

    assert przesun_zera(lista) == wynik


def test_2():
    lista = [0, 0, 0, 0]
    wynik = [0, 0, 0, 0]

    assert przesun_zera(lista) == wynik


def test_3():
    lista = [1, 2, 3, 4, 5, 6]
    wynik = [1, 2, 3, 4, 5, 6]

    assert przesun_zera(lista) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
