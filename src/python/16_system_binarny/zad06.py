r"""
ZAD-06 — Konwersja między dowolnymi systemami (2..36)

**Poziom:** ★★☆
**Tagi:** `konwersja`, `base`, `string`

### Treść

Wczytaj zapis liczby naturalnej `X` w systemie o podstawie `p` oraz podstawę docelową `q`. Wypisz zapis tej samej liczby w systemie o podstawie `q`.

### Wejście

* 1. linia: `X` — zapis liczby w systemie o podstawie `p` (cyfry `0–9` i wielkie litery `A–Z`, gdzie `A` = 10, `B` = 11, …, `Z` = 35)
* 2. linia: `p` — podstawa systemu, w którym zapisano `X`
* 3. linia: `q` — podstawa systemu docelowego

### Wyjście

Jedna linia: zapis liczby w systemie o podstawie `q`, bez zer wiodących (cyfry `0–9` i wielkie litery `A–Z`).

### Ograniczenia

* `2 ≤ p, q ≤ 36`
* `X` ma od 1 do 20 znaków, każda cyfra jest mniejsza od `p`; `X` może zaczynać się od zer

### Przykład

**Wejście:**

```
4301
10
4
```

**Wyjście:**

```
1003031
```

### Uwagi

* Najpierw zamień `X` na liczbę (przechodząc po cyfrach od lewej: wynik = wynik · `p` + cyfra), a potem zamień ją na system `q` (reszty z dzielenia przez `q`).
* Spróbuj obejść się bez `int(X, p)` — zaimplementuj obie zamiany samodzielnie.
* Liczba `0` w każdym systemie to `0`.

"""

CYFRY = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def na_dziesietny(zapis, podstawa):
    """Zwraca wartość liczby zapisanej w systemie o podanej podstawie."""
    wartosc = 0
    for znak in zapis:
        wartosc = wartosc * podstawa + CYFRY.index(znak)
    return wartosc


def z_dziesietnego(wartosc, podstawa):
    """Zwraca zapis liczby naturalnej w systemie o podanej podstawie."""
    if wartosc == 0:
        return "0"
    zapis = ""
    while wartosc > 0:
        zapis = CYFRY[wartosc % podstawa] + zapis
        wartosc //= podstawa
    return zapis


def zmien_podstawe(zapis, stara_podstawa, nowa_podstawa):
    return z_dziesietnego(na_dziesietny(zapis, stara_podstawa), nowa_podstawa)


if __name__ == "__main__":
    zapis = input().strip().upper()
    p = int(input())
    q = int(input())
    print(zmien_podstawe(zapis, p, q))
