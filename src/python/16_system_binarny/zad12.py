r"""
ZAD-12 — Najdłuższy ciąg zer otoczony jedynkami

**Poziom:** ★★★
**Tagi:** `binarne`, `binary gap`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. W jej zapisie binarnym znajdź długość najdłuższego ciągu kolejnych zer, który jest **z obu stron otoczony jedynkami** (tzw. *binary gap*). Jeśli takiego ciągu nie ma, wypisz `0`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: długość najdłuższego takiego ciągu zer.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
14
```

**Wyjście:**

```
0
```

`14` ma zapis `1110` — zero na końcu nie ma jedynki po prawej stronie, więc wynik to `0`.

### Przykład 2

**Wejście:**

```
20
```

**Wyjście:**

```
1
```

`20` ma zapis `10100` — zero między jedynkami tworzy ciąg długości `1`, a końcowe `00` się nie liczy.

### Uwagi

* Dla `n = 0` (zapis `0`) wynik to `0`.

"""


def najdluzsza_przerwa(n):
    """
    Zwraca długość najdłuższego ciągu zer otoczonego z obu stron jedynkami
    w zapisie binarnym n.
    """
    if n == 0:
        return 0
    # Zera na końcu zapisu nie mają jedynki po prawej stronie — pomijamy je.
    while n & 1 == 0:
        n >>= 1

    najdluzsza = 0
    biezaca = 0
    while n > 0:
        if n & 1:
            najdluzsza = max(najdluzsza, biezaca)
            biezaca = 0
        else:
            biezaca += 1
        n >>= 1
    return najdluzsza


if __name__ == "__main__":
    n = int(input())
    print(najdluzsza_przerwa(n))
