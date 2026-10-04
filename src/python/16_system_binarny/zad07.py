r"""
ZAD-07 — Zamiana sąsiadujących bitów

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `maski`, `swap bits`

### Treść

Wczytaj liczbę naturalną `n`. Zamień miejscami każdą parę sąsiadujących bitów jej zapisu binarnego (bity numerujemy od `0` — najmłodszy, czyli skrajnie prawy):

* bit 0 z bitem 1,
* bit 2 z bitem 3,
* bit 4 z bitem 5,
* itd.

Wypisz otrzymaną liczbę w systemie dziesiętnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: wynik po zamianie bitów.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
9131
```

**Wyjście:**

```
4951
```

`9131` to binarnie `10001110101011`, a po zamianie par bitów otrzymujemy `01001101010111`, czyli `4951`.

### Uwagi

* Brakujące bity na początku zapisu traktujemy jak zera. Na przykład `4` to `100`: bit 2 (jedynka) zamienia się z bitem 3 (zerem), więc wynik to `1000`, czyli `8`.
* Maska `0x55555555` (`…0101`) wybiera bity o numerach parzystych, a `0xAAAAAAAA` (`…1010`) — o numerach nieparzystych.

"""


def zamien_sasiednie_bity(n):
    """
    Zamienia miejscami bity 0 i 1, 2 i 3, 4 i 5 itd.
    Maska 0x55555555 = 0101...01 wybiera bity parzyste,
    maska 0xAAAAAAAA = 1010...10 wybiera bity nieparzyste.
    """
    parzyste = n & 0x55555555
    nieparzyste = n & 0xAAAAAAAA
    return (parzyste << 1) | (nieparzyste >> 1)


if __name__ == "__main__":
    n = int(input())
    print(zamien_sasiednie_bity(n))
