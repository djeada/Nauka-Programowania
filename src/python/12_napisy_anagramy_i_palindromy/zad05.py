r"""
ZAD-05 — Anagramy słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `napisy`, `anagram`, `słowa`

### Treść

Wczytaj zdanie oraz słowo-klucz `k`. Wypisz wszystkie słowa zdania, które są anagramami słowa `k` (także samo słowo `k`). Przy porównywaniu ignoruj wielkość liter.
Słowa wyznaczaj zgodnie z konwencją rozdziału (bez interpunkcji z brzegów).

### Wejście

* 1. linia: zdanie
* 2. linia: słowo-klucz `k`

### Wyjście

Każde słowo zdania będące anagramem `k` w osobnej linii, w kolejności występowania i w postaci z wejścia. Jeśli takich słów nie ma, program nic nie wypisuje.

### Przykład

**Wejście:**

```
Sroga kara, a potem raka.
arak
```

**Wyjście:**

```
kara
raka
```

### Uwagi

* Wykorzystaj rozwiązanie zadania ZAD-03: porównuj posortowane litery słów zapisanych małymi literami.

"""

import string


def czy_anagramy(slowo1, slowo2):
    """Sprawdza, czy słowa są anagramami, ignorując wielkość liter."""
    return sorted(slowo1.lower()) == sorted(slowo2.lower())


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
    klucz = input().strip()

    for slowo in podziel_na_slowa(zdanie):
        if czy_anagramy(slowo, klucz):
            print(slowo)
