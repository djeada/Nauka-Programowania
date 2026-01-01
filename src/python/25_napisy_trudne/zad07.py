"""
ZAD-07 — Powtarzające się podnapisy

**Poziom:** ★★★
**Tagi:** `string`, `substrings`, `count`

### Treść

Otrzymujesz napis. Znajdź wszystkie **podnapisy**, które występują w nim **więcej niż jeden raz**.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: lista napisów — wszystkie powtarzające się podnapisy

### Przykład

**Wejście:**

```
pythonpython
```

**Wyjście:**

```
['python']
```

### Uwagi

* Jeśli sprawdzarka wymaga konkretnej kolejności (np. rosnąco po długości/alfabetycznie) — musi to być opisane. W przeciwnym razie dopuszczalna może być dowolna kolejność.

"""

from collections import deque


# Wersja 1
def najdluzsze_powtorzenie_v1(slowo):
    lista = list(slowo)
    kolejka = deque(slowo[1:])
    powtorzenia = list()
    wynik = list()
    while kolejka:
        for i, elem in enumerate(kolejka):
            if lista[i] == elem:
                powtorzenia.append(elem)
            else:
                if len(wynik) < len(powtorzenia):
                    wynik = powtorzenia
                powtorzenia = list()
        kolejka.popleft()
    return "".join(wynik)


# Testy Poprawnosci
def test_1():
    slowo = "98432934021742343230"
    wynik = "432"
    assert najdluzsze_powtorzenie_v1(slowo) == wynik


def test_2():
    slowo = "abcdef"
    wynik = ""
    assert najdluzsze_powtorzenie_v1(slowo) == wynik


def test_3():
    slowo = "Arnold i Arnold"
    wynik = "Arnold"
    assert najdluzsze_powtorzenie_v1(slowo) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
