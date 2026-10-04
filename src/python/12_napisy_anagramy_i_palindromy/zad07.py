r"""
ZAD-07 — Minimalna liczba usunięć, aby uzyskać anagramy

**Poziom:** ★★☆
**Tagi:** `napisy`, `anagram`, `zliczanie`

### Treść

Wczytaj dwa słowa (mogą mieć różne długości). Oblicz, ile **łącznie** znaków trzeba co najmniej usunąć z obu słów, aby pozostałe napisy były anagramami (pozostałe napisy mogą też być puste).

### Wejście

* 1. linia: słowo `s1` (małe litery)
* 2. linia: słowo `s2` (małe litery)

### Wyjście

Jedna linia: minimalna łączna liczba usuniętych znaków.

### Przykład 1

**Wejście:**

```
grazyna
razynax
```

**Wyjście:**

```
2
```

Z pierwszego słowa usuwamy `g`, z drugiego `x` — zostają anagramy `razyna` i `razyna`.

### Przykład 2

**Wejście:**

```
kajak
ak
```

**Wyjście:**

```
3
```

Z `kajak` usuwamy `k`, `j` i `a` — zostaje `ka`, które jest anagramem `ak`. Z `ak` nic nie usuwamy.

### Uwagi

* Dla każdej litery policz, ile razy występuje w `s1` (np. `s1.count(litera)`) i ile w `s2`. Nadmiarowe wystąpienia trzeba usunąć, więc wynik to suma wartości $|c_1 - c_2|$ po wszystkich literach występujących w którymkolwiek słowie (np. po literach zbioru `set(s1 + s2)`).

"""


def minimalne_usuniecia(slowo1, slowo2):
    """Łączna liczba znaków do usunięcia, aby słowa stały się anagramami."""
    suma = 0
    for litera in set(slowo1 + slowo2):
        suma += abs(slowo1.count(litera) - slowo2.count(litera))
    return suma


if __name__ == "__main__":
    slowo1 = input().strip()
    slowo2 = input().strip()

    print(minimalne_usuniecia(slowo1, slowo2))
