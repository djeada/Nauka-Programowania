r"""
ZAD-09 — Znaki występujące co najmniej dwa razy

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Wypisz napis złożony z tych znaków, które występują w nim **co najmniej 2 razy** — każdy taki znak tylko raz, w kolejności pierwszego wystąpienia w napisie.

### Wejście

* 1. linia: napis bez spacji

### Wyjście

Jedna linia: wynikowy napis. Jeśli żaden znak się nie powtarza — pusta linia (albo brak wyjścia).

### Ograniczenia

* napis ma od 1 do 100 znaków

### Przykład

**Wejście:**

```
aaabbbccc
```

**Wyjście:**

```
abc
```

### Uwagi

* Wielkość liter ma znaczenie: `A` i `a` to różne znaki.
* Policz wystąpienia znaków w słowniku — kolejność kluczy w słowniku to kolejność pierwszego wystąpienia.

"""


def powtarzajace_sie_znaki(napis):
    """
    Zwraca napis z różnych znaków występujących co najmniej dwa razy,
    w kolejności ich pierwszego wystąpienia.
    """
    licznik = {}
    for znak in napis:
        licznik[znak] = licznik.get(znak, 0) + 1

    wynik = ""
    for znak in licznik:
        if licznik[znak] >= 2:
            wynik += znak
    return wynik


if __name__ == "__main__":
    print(powtarzajace_sie_znaki(input().strip()))
