"""
ZAD-05 — Co k-ty znak poziomo i pionowo

**Poziom:** ★☆☆
**Tagi:** `string`, `slicing`, `pętle`

### Treść

Wczytaj napis i liczbę `k`.

a) Wypisz co `k`-ty znak w jednym wierszu, oddzielając znaki spacjami.
b) Wypisz co `k`-ty znak pionowo (każdy w osobnej linii).

### Wejście

* 1. linia: napis
* 2. linia: liczba naturalna `k` (k ≥ 1)

### Wyjście

* (a) 1 linia: znaki oddzielone spacjami
* (b) wiele linii: każdy znak osobno

### Przykład

**Wejście:**

```
Grzechotnik
3
```

**Wyjście:**

```
z h n
z
h
n
```

### Uwagi o formatowaniu

* Dokładnie jedna spacja między znakami w punkcie (a), bez spacji na końcu linii.

"""


def wypisz_poziomo(napis, k):
    for i in range(len(napis)):
        if i % k == 0:
            print(napis[i], end=" ")
    print()


def wypisz_pionowo(napis, k):
    for i in range(len(napis)):
        if i % k == 0:
            print(napis[i])


if __name__ == "__main__":

    napis = input("Podaj napis: ")
    k = int(input("Podaj liczbe k: "))

    print("Napis wypisany poziomo: ")
    wypisz_poziomo(napis, k)

    print("Napis wypisany pionowo: ")
    wypisz_pionowo(napis, k)
