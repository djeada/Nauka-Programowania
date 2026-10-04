r"""
ZAD-10 — Ile bitów trzeba odwrócić (A → B)

**Poziom:** ★★☆
**Tagi:** `XOR`, `popcount`, `bitwise`

### Treść

Wczytaj dwie liczby naturalne `A` i `B`. Oblicz, ile bitów trzeba odwrócić w liczbie `A`, aby otrzymać `B`, czyli na ilu pozycjach ich zapisy binarne się różnią.

### Wejście

* 1. linia: `A`
* 2. linia: `B`

### Wyjście

Jedna liczba naturalna: liczba różniących się bitów.

### Ograniczenia

* $0 \le A, B \le 10^9$

### Przykład

**Wejście:**

```
34
73
```

**Wyjście:**

```
5
```

`34` = `0100010`, `73` = `1001001` — różnią się na 5 pozycjach.

### Uwagi

* Krótszy zapis uzupełniamy zerami z lewej strony.
* `A ^ B` ma jedynki dokładnie na pozycjach, na których bity `A` i `B` są różne.

"""


def liczba_jedynek(n):
    jedynki = 0
    while n > 0:
        jedynki += n & 1
        n >>= 1
    return jedynki


def bity_do_zmiany(a, b):
    """
    Zwraca liczbę bitów, którymi różnią się a i b.
    W a ^ b jedynki stoją dokładnie na pozycjach, na których bity są różne.
    """
    return liczba_jedynek(a ^ b)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(bity_do_zmiany(a, b))
