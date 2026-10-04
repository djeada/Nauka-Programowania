r"""
ZAD-01B — Binarny → dziesiętny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `string`, `binarne`

### Treść

Wczytaj liczbę naturalną zapisaną w systemie binarnym (ciąg znaków `0` i `1`) i wypisz jej wartość w systemie dziesiętnym.

### Wejście

* 1. linia: `b` — niepusty ciąg znaków `0` i `1` (może zaczynać się od zer)

### Wyjście

Jedna linia: wartość liczby w systemie dziesiętnym.

### Ograniczenia

* długość `b` od 1 do 30 znaków

### Przykład

**Wejście:**

```
101
```

**Wyjście:**

```
5
```

### Uwagi

* Zera wiodące nie zmieniają wartości: `0010` to `2`.
* Spróbuj obejść się bez `int(b, 2)`: przechodząc po cyfrach od lewej, mnóż dotychczasowy wynik przez 2 i dodawaj kolejną cyfrę.

"""


def na_dziesietny(zapis):
    """Zwraca wartość liczby zapisanej w systemie binarnym (ciąg znaków 0 i 1)."""
    wartosc = 0
    for cyfra in zapis:
        wartosc = wartosc * 2 + int(cyfra)
    return wartosc


if __name__ == "__main__":
    zapis = input().strip()
    print(na_dziesietny(zapis))
