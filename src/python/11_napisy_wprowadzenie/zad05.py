r"""
ZAD-05 — Co k-ty znak poziomo i pionowo

**Poziom:** ★☆☆
**Tagi:** `napisy`, `wycinanie`, `pętle`

### Treść

Wczytaj napis i liczbę `k`. Wybierz co `k`-ty znak napisu, czyli znaki na pozycjach $k, 2k, 3k, \ldots$ (pozycje liczymy od 1).

a) Wypisz wybrane znaki w jednej linii, oddzielone pojedynczymi spacjami.
b) Wypisz wybrane znaki pionowo — każdy w osobnej linii.

### Wejście

* 1. linia: napis bez spacji
* 2. linia: liczba naturalna `k`

### Wyjście

* 1. linia: wynik podpunktu a)
* kolejne linie: wynik podpunktu b) — po jednym znaku w linii

### Ograniczenia

* $1 \le k \le$ długość napisu (wybrany zostanie więc co najmniej jeden znak).

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

Znaki na pozycjach 3, 6 i 9 to `z`, `h` i `n`.

### Uwagi

* Pozycja $k$ to indeks `k - 1` w Pythonie, więc wybrane znaki to `napis[k - 1::k]`.

"""


def co_kty_znak(napis, k):
    wybrane = []
    for i in range(k - 1, len(napis), k):
        wybrane.append(napis[i])
    return wybrane


if __name__ == "__main__":
    napis = input()
    k = int(input())

    znaki = co_kty_znak(napis, k)

    print(" ".join(znaki))
    for znak in znaki:
        print(znak)
