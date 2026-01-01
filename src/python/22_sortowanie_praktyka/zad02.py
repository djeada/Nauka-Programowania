"""
ZAD-02 — Sortowanie słów w zdaniu

**Poziom:** ★★☆
**Tagi:** `sort`, `string`, `split`

### Treść

Otrzymujesz zdanie. Podziel je na słowa, traktując znaki interpunkcyjne jako separatory, a następnie posortuj słowa alfabetycznie i wypisz listę.

### Wejście

* 1 linia: napis `zdanie`

### Wyjście

* 1 linia: lista słów w formacie jak w przykładzie, np. `['Ala', 'kota', 'ma']`

### Przykład

**Wejście:**

```
Lemur wygina śmiało ciało
```

**Wyjście:**

```
['Lemur', 'ciało', 'wygina', 'śmiało']
```

### Uwagi o formatowaniu

* Ignoruj znaki interpunkcyjne (np. `.,!?;:`) — nie są częścią słów.
* Wielkość liter pozostaje bez zmian (nie zamieniaj na małe/duże), sortujesz to, co w tekście.

"""

import string


def podziel_zdanie_na_slowa(zdanie):
    """
    Funkcja zwraca liste slow ze zdania.
    """
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def sortuj_slowa_w_zdaniu(zdanie):
    """
    Funkcja zwraca posortowana liste slow ze zdania.
    """
    return sorted(podziel_zdanie_na_slowa(zdanie))


def test_sortuj_slowa_w_zdaniu():
    assert sortuj_slowa_w_zdaniu("Lemur wygina smialo cialo") == [
        "Lemur",
        "cialo",
        "smialo",
        "wygina",
    ]


if __name__ == "__main__":
    test_sortuj_slowa_w_zdaniu()
