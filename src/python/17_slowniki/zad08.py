r"""
ZAD-08 — Najczęstsza litera w zdaniu

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj zdanie. Policz wystąpienia liter, pomijając spacje, cyfry i znaki interpunkcyjne oraz nie rozróżniając wielkości liter. Wypisz literę, która występuje najczęściej.
Jeśli kilka liter występuje tyle samo razy, wybierz tę, która **pojawia się w zdaniu jako pierwsza**.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedną literę)

### Wyjście

Jedna linia: najczęstsza litera, zapisana jako mała litera.

### Ograniczenia

* zdanie ma od 1 do 300 znaków

### Przykład

**Wejście:**

```
lezy jerzy na wiezy
```

**Wyjście:**

```
e
```

Litery `e`, `z` i `y` występują po 3 razy; najwcześniej w zdaniu pojawia się `e`.

### Uwagi

* `A` i `a` to ta sama litera — w zdaniu `Ala ma Asa` litera `a` występuje 5 razy.
* Zliczanie można powierzyć klasie `Counter` z modułu `collections` (`from collections import Counter`). `Counter` to słownik element → liczba wystąpień, np. `Counter("abca")` daje `Counter({'a': 2, 'b': 1, 'c': 1})`, a metoda `most_common(1)` zwraca listę z jedną parą `(element, liczba)` o największej liczbie wystąpień: `Counter("abca").most_common(1)` to `[('a', 2)]`.
* Przy remisie `most_common` zachowuje kolejność pierwszego wystąpienia, więc spełnia regułę z treści: `Counter("baab").most_common(1)` to `[('b', 2)]`.

"""


def najczestsza_litera(zdanie):
    """
    Zwraca najczęściej występującą literę (małą), nie rozróżniając wielkości liter.
    Przy remisie wygrywa litera, która pojawia się w zdaniu wcześniej.
    """
    licznik = {}
    for znak in zdanie.lower():
        if znak.isalpha():
            licznik[znak] = licznik.get(znak, 0) + 1

    najczestsza = None
    for litera in licznik:  # kolejność pierwszego wystąpienia
        if najczestsza is None or licznik[litera] > licznik[najczestsza]:
            najczestsza = litera
    return najczestsza


if __name__ == "__main__":
    print(najczestsza_litera(input()))
