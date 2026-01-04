"""
ZAD-01 — Najdłuższy ciąg jedynek

**Poziom:** ★★☆
**Tagi:** `list`, `0/1`, `analiza`, `indeksy`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Znajdź **indeks zera**, które po zamianie na `1` da **najdłuższy ciąg kolejnych jedynek**.

Jeśli lista składa się wyłącznie z zer **albo** wyłącznie z jedynek — wypisz `-1`.

### Wejście

* 1 linia: lista `A` (tylko `0` i `1`)

### Wyjście

* 1 linia: indeks (liczba całkowita) albo `-1`

### Przykład

**Wejście:**

```
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
```

**Wyjście:**

```
7
```

### Uwagi

* Jeśli kilka zer daje ten sam maksymalny wynik — wybierz to o **najmniejszym indeksie** (jeśli nie określono inaczej w testach).

"""


def znajdz_zero_do_podmiany_v1(lista):
    licznik_jedynek = 0
    indeks_zera = -1

    licznik_zer = 0
    poprzedni_indeks_zera = -1

    for i in range(len(lista)):

        if lista[i] == 1:
            licznik_zer += 1

        else:
            licznik_zer = i - poprzedni_indeks_zera
            poprzedni_indeks_zera = i

        if licznik_zer > licznik_jedynek:
            licznik_jedynek = licznik_zer
            indeks_zera = poprzedni_indeks_zera

    return indeks_zera


# Testy Poprawnosci
def test_1():
    lista = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
    wynik = 7

    assert znajdz_zero_do_podmiany_v1(lista) == wynik


def test_2():
    lista = [1, 1, 1, 1, 1, 1, 1, 1]
    wynik = -1

    assert znajdz_zero_do_podmiany_v1(lista) == wynik


def test_3():
    lista = [1, 0, 1, 1, 1, 1, 1, 1]
    wynik = 1

    assert znajdz_zero_do_podmiany_v1(lista) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
