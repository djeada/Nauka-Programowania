r"""
ZAD-06 — Permutacje słowa, które są palindromami

**Poziom:** ★★☆
**Tagi:** `napisy`, `palindrom`, `permutacje`

### Treść

Wczytaj słowo i wypisz wszystkie **różne** palindromy, które można ułożyć z jego liter (używając każdej litery dokładnie tyle razy, ile razy występuje w słowie).

### Wejście

* 1. linia: słowo złożone z małych liter alfabetu angielskiego (`a`–`z`); litery mogą się powtarzać

### Wyjście

Każdy palindrom w osobnej linii, bez powtórzeń, w **kolejności alfabetycznej**. Jeśli z liter słowa nie da się ułożyć żadnego palindromu, program nic nie wypisuje.

### Ograniczenia

* Długość słowa: od 1 do 10.

### Przykład 1

**Wejście:**

```
aabb
```

**Wyjście:**

```
abba
baab
```

### Przykład 2

**Wejście:**

```
abc
```

**Wyjście:** *(brak)*

### Uwagi

* Palindrom da się ułożyć tylko wtedy, gdy co najwyżej jedna litera występuje nieparzystą liczbę razy (ta litera trafia na środek).
* Wystarczy wygenerować permutacje „połówki” palindromu (po połowie wystąpień każdej litery, np. funkcją `permutations` z zadania ZAD-02) i do każdej dokleić środek oraz odwróconą połówkę. Gdy litery się powtarzają, `permutations` zwraca te same układy wielokrotnie — powtórzenia usuniesz, zbierając wyniki w zbiorze (`set`).

"""

from itertools import permutations


def palindromy_z_liter(slowo):
    """Zwraca posortowaną listę różnych palindromów ułożonych z liter słowa."""
    srodek = ""
    polowka = ""
    for litera in sorted(set(slowo)):
        liczba = slowo.count(litera)
        if liczba % 2 == 1:
            if srodek:
                return []  # więcej niż jedna litera o nieparzystej liczbie wystąpień
            srodek = litera
        polowka += litera * (liczba // 2)

    wynik = set()
    for krotka in permutations(polowka):
        lewa = "".join(krotka)
        wynik.add(lewa + srodek + lewa[::-1])
    return sorted(wynik)


if __name__ == "__main__":
    slowo = input().strip()

    for palindrom in palindromy_z_liter(slowo):
        print(palindrom)
