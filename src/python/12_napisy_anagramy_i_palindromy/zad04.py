r"""
ZAD-04 — Palindromy w zdaniu

**Poziom:** ★★☆
**Tagi:** `napisy`, `palindrom`, `słowa`

### Treść

Wczytaj zdanie i wypisz wszystkie jego słowa, które są palindromami. Przy sprawdzaniu ignoruj wielkość liter.
Słowa wyznaczaj zgodnie z konwencją rozdziału (bez interpunkcji z brzegów). Pojedyncza litera też jest palindromem.

### Wejście

* 1. linia: zdanie (może zawierać znaki interpunkcyjne)

### Wyjście

Każde słowo będące palindromem w osobnej linii, w kolejności występowania w zdaniu i w postaci z wejścia (bez interpunkcji z brzegów). Słowo, które powtarza się w zdaniu, wypisz tyle razy, ile razy występuje. Jeśli w zdaniu nie ma palindromów, program nic nie wypisuje.

### Przykład 1

**Wejście:**

```
Anna zabrała kajak na wycieczkę i uderzyła się w oko.
```

**Wyjście:**

```
Anna
kajak
i
w
oko
```

`Anna` jest palindromem, bo po zamianie na małe litery daje `anna`; z `oko.` usuwamy kropkę.

### Przykład 2

**Wejście:**

```
Hello world
```

**Wyjście:** *(brak)*

"""

import string


def czy_palindrom(slowo):
    """Sprawdza, czy słowo jest palindromem, ignorując wielkość liter."""
    slowo_male = slowo.lower()
    return slowo_male == slowo_male[::-1]


def podziel_na_slowa(zdanie):
    """Dzieli zdanie na słowa i usuwa interpunkcję z ich brzegów."""
    slowa = []
    for fragment in zdanie.split():
        slowo = fragment.strip(string.punctuation)
        if slowo:
            slowa.append(slowo)
    return slowa


if __name__ == "__main__":
    zdanie = input()

    for slowo in podziel_na_slowa(zdanie):
        if czy_palindrom(slowo):
            print(slowo)
