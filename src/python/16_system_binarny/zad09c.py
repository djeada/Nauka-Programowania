r"""
ZAD-09C — Odwróć wielkość liter (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `toggle case`

### Treść

Wczytaj napis. Zamień wielkość każdej litery alfabetu łacińskiego na przeciwną (mała ↔ wielka), używając operacji bitowych na kodach ASCII. Pozostałe znaki pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje, cyfry i znaki interpunkcyjne)

### Wyjście

Jedna linia: napis po zmianie.

### Ograniczenia

* napis ma od 1 do 100 znaków i składa się wyłącznie ze znaków ASCII (bez polskich liter)

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
tEST
```

### Uwagi

* Odwrócenie bitu o wartości 32: `ord(znak) ^ 32`. Stosuj je tylko do liter `a–z` i `A–Z`.

"""

MASKA_WIELKOSCI = 0b100000  # 32 — jedyny bit różniący 'A' (65) od 'a' (97)


def odwroc_wielkosc(napis):
    """Zamienia wielkość każdej litery a-z / A-Z, odwracając bit 5 kodu ASCII."""
    wynik = ""
    for znak in napis:
        if "a" <= znak <= "z" or "A" <= znak <= "Z":
            znak = chr(ord(znak) ^ MASKA_WIELKOSCI)
        wynik += znak
    return wynik


if __name__ == "__main__":
    print(odwroc_wielkosc(input()))
