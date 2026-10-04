r"""
ZAD-06D — Trzycyfrowe podzielne przez sumę cyfr liczby n

**Poziom:** ★★☆
**Tagi:** `pętle`, `dzielenie`, `suma cyfr`

### Treść

Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr `s`. Następnie wypisz w kolejności rosnącej wszystkie liczby trzycyfrowe (od `100` do `999`), które są podzielne przez `s`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Liczby trzycyfrowe podzielne przez `s`, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Ograniczenia

* `n ≥ 1`, więc `s ≥ 1` i dzielenie jest zawsze wykonalne.

### Przykład

**Wejście:**

```
9999999
```

**Wyjście:**

```
126
189
252
315
378
441
504
567
630
693
756
819
882
945
```

Suma cyfr to $s = 7 \cdot 9 = 63$, a wypisane liczby to kolejne trzycyfrowe wielokrotności `63`.

"""


def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    return suma


if __name__ == "__main__":
    n = int(input())
    s = suma_cyfr(n)

    for x in range(100, 1000):
        if x % s == 0:
            print(x)
