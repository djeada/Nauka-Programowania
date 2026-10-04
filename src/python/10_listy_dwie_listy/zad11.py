r"""
ZAD-11 — Operacje na zbiorach

**Poziom:** ★☆☆
**Tagi:** `zbiory`, `set`, `listy`

### Treść

Wczytaj dwie listy liczb całkowitych i zamień każdą z nich na zbiór: $A$ (z listy 1) i $B$ (z listy 2). Powtórzenia elementów w listach znikają, bo zbiór przechowuje każdą wartość tylko raz.

Wypisz:

1. sumę zbiorów $A \cup B$ (elementy należące do $A$ lub do $B$),
2. część wspólną $A \cap B$ (elementy należące do $A$ i do $B$),
3. różnicę $A \setminus B$ (elementy $A$, których nie ma w $B$),
4. różnicę symetryczną (elementy należące do dokładnie jednego ze zbiorów),
5. odpowiedź na pytanie, czy $A$ jest podzbiorem $B$ (czy każdy element $A$ należy do $B$).

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Pięć linii:

* linie 1–4: wyniki działań 1–4 jako listy posortowane rosnąco, wypisane przez `print(sorted(...))`, np. `[1, 2, 5]`; pusty wynik to `[]`,
* linia 5: `Tak`, jeśli $A$ jest podzbiorem $B$, w przeciwnym razie `Nie`.

### Przykład 1

**Wejście:**

```
1 2 3 4 2
3 4 5
```

**Wyjście:**

```
[1, 2, 3, 4, 5]
[3, 4]
[1, 2]
[1, 2, 5]
Nie
```

### Przykład 2

**Wejście:**

```
2 2 1
1 2 3
```

**Wyjście:**

```
[1, 2, 3]
[1, 2]
[]
[3]
Tak
```

### Uwagi

* Zbiór tworzysz z listy funkcją `set`, np. `set([2, 2, 1])` to zbiór `{1, 2}`.
* Działania na zbiorach w Pythonie: `A | B` (suma), `A & B` (część wspólna), `A - B` (różnica), `A ^ B` (różnica symetryczna), `A <= B` (czy $A$ jest podzbiorem $B$ — wynik `True` lub `False`).
* Zbiór nie pamięta kolejności elementów, dlatego przed wypisaniem zamień go na posortowaną listę: `sorted(A | B)`.

"""


def operacje_na_zbiorach(zbior_a, zbior_b):
    return [
        sorted(zbior_a | zbior_b),
        sorted(zbior_a & zbior_b),
        sorted(zbior_a - zbior_b),
        sorted(zbior_a ^ zbior_b),
    ]


if __name__ == "__main__":
    zbior_a = set([int(x) for x in input().split()])
    zbior_b = set([int(x) for x in input().split()])

    for wynik in operacje_na_zbiorach(zbior_a, zbior_b):
        print(wynik)
    print("Tak" if zbior_a <= zbior_b else "Nie")
