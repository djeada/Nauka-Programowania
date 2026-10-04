r"""
ZAD-13 — Znaki na indeksach będących liczbami pierwszymi

**Poziom:** ★☆☆
**Tagi:** `napisy`, `indeksy`, `liczby pierwsze`

### Treść

Wczytaj napis i zbierz do listy znaki, których **indeksy** (liczone od 0) są liczbami pierwszymi: 2, 3, 5, 7, 11, … Wypisz tę listę.

### Wejście

* 1. linia: napis (może zawierać spacje)

### Wyjście

Jedna linia: lista znaków wypisana tak jak przez `print(lista)`, np. `['o', 'ń']`. Jeśli napis ma mniej niż 3 znaki, wypisz `[]`.

### Przykład

**Wejście:**

```
Słoń
```

**Wyjście:**

```
['o', 'ń']
```

Indeksy: `S` — 0, `ł` — 1, `o` — 2, `ń` — 3. Liczbami pierwszymi są 2 i 3.

"""


def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    dzielnik = 2
    while dzielnik * dzielnik <= liczba:
        if liczba % dzielnik == 0:
            return False
        dzielnik += 1
    return True


def znaki_na_indeksach_pierwszych(napis):
    znaki = []
    for indeks, znak in enumerate(napis):
        if czy_pierwsza(indeks):
            znaki.append(znak)
    return znaki


if __name__ == "__main__":
    napis = input()
    print(znaki_na_indeksach_pierwszych(napis))
