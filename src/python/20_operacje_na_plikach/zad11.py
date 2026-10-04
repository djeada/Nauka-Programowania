r"""
ZAD-11 — Zamień miejscami treści dwóch plików

**Poziom:** ★★☆
**Tagi:** `files`, `swap`, `read/write`

### Treść

Wczytaj ścieżki dwóch plików A i B. Zamień ich treści miejscami:

* plik A ma mieć dawną treść pliku B,
* plik B ma mieć dawną treść pliku A.

Nazwy plików się nie zmieniają. Jeśli obie ścieżki są takie same, plik pozostaje bez zmian.

### Wejście

* 1. linia: ścieżka pliku A
* 2. linia: ścieżka pliku B

### Wyjście

* Gdy oba pliki istnieją — nic (wynikiem są zmienione pliki).
* `Plik nie istnieje.` — jeśli którakolwiek ścieżka nie wskazuje istniejącego pliku. Wtedy niczego nie zmieniaj i nie twórz.

### Przykład

**Pliki przed:**

```
plik1.txt
| Ala ma kota
dane/plik2.txt
| Kot ma Alę
| i mysz.
```

**Wejście:**

```
plik1.txt
dane/plik2.txt
```

**Wyjście:** *(brak)*

**Pliki po:**

```
plik1.txt
| Kot ma Alę
| i mysz.
dane/plik2.txt
| Ala ma kota
```

### Przykład 2

**Pliki przed:**

```
plik1.txt
| Ala ma kota
```

**Wejście:**

```
plik1.txt
plik2.txt
```

**Wyjście:**

```
Plik nie istnieje.
```

**Pliki po:**

```
plik1.txt
| Ala ma kota
plik2.txt (usunięty)
```

### Uwagi

* Najprościej wczytać obie treści do zmiennych, a dopiero potem zapisać każdy plik od nowa.

"""

import os


def wczytaj(sciezka):
    with open(sciezka, encoding="utf-8") as plik:
        return plik.read()


def zapisz(sciezka, tresc):
    with open(sciezka, "w", encoding="utf-8") as plik:
        plik.write(tresc)


def zamien_tresci(plik_a, plik_b):
    """Plik A dostaje treść pliku B, a plik B — treść pliku A."""
    tresc_a = wczytaj(plik_a)
    tresc_b = wczytaj(plik_b)
    zapisz(plik_a, tresc_b)
    zapisz(plik_b, tresc_a)


if __name__ == "__main__":
    plik_a = input()
    plik_b = input()

    if os.path.isfile(plik_a) and os.path.isfile(plik_b):
        zamien_tresci(plik_a, plik_b)
    else:
        print("Plik nie istnieje.")
