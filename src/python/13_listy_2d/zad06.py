r"""
ZAD-06 — Scalanie przedziałów

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `przedziały`, `algorytmy`

### Treść

Wczytaj `n` przedziałów domkniętych $[a_i, b_i]$. Scal wszystkie przedziały, które na siebie nachodzą, i wypisz otrzymane rozłączne przedziały w kolejności rosnącej według początku.

### Wejście

* 1. linia: `n`
* następnie `n` linii, w każdej dwie liczby całkowite `a_i b_i` (`a_i ≤ b_i`)

### Wyjście

Każdy scalony przedział w osobnej linii w postaci `a b`, posortowane rosnąco według `a`.

### Ograniczenia

* `1 ≤ n ≤ 1000`
* $-10^6 \le a_i \le b_i \le 10^6$

### Przykład

**Wejście:**

```
7
23 67
23 53
45 88
77 88
10 22
11 12
42 45
```

**Wyjście:**

```
10 22
23 88
```

### Uwagi

* Przedziały na wejściu mogą być podane w dowolnej kolejności — najpierw je posortuj.
* Dwa przedziały (po posortowaniu) nachodzą na siebie, gdy początek następnego jest **mniejszy lub równy** końcowi bieżącego. Przedziały stykające się końcami, np. `1 3` i `3 5`, scalamy w `1 5`, natomiast `10 22` i `23 88` pozostają osobno.

"""


def scal_przedzialy(przedzialy):
    """
    Scala nachodzące na siebie przedziały [a, b] i zwraca listę rozłącznych
    przedziałów posortowaną rosnąco po początku. Przedziały stykające się
    końcami (np. [1, 3] i [3, 5]) również są scalane.
    """
    wynik = []
    for poczatek, koniec in sorted(przedzialy):
        if wynik and poczatek <= wynik[-1][1]:
            wynik[-1][1] = max(wynik[-1][1], koniec)
        else:
            wynik.append([poczatek, koniec])
    return wynik


if __name__ == "__main__":
    n = int(input())
    przedzialy = []
    for _ in range(n):
        a, b = input().split()
        przedzialy.append([int(a), int(b)])

    for poczatek, koniec in scal_przedzialy(przedzialy):
        print(poczatek, koniec)
