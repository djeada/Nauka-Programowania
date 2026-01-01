"""
ZAD-04 — Usuń pary ze słownika na podstawie wartości

**Poziom:** ★☆☆
**Tagi:** `dict`, `filtrowanie`

### Treść

Wczytaj słownik (`n` par: klucz-napis, wartość-liczba) oraz liczbę `k`. Usuń wszystkie pary, gdzie wartość == `k`. Wypisz wynikowy słownik.

### Wejście

* 1 linia: `n`
* następnie `n` linii: `klucz wartość`
* ostatnia linia: `k`

### Wyjście

* Słownik po usunięciu par

### Przykład

**Wejście:**

```
4
aaa 5
abc 1
xxx 5
cba 3
5
```

**Wyjście:**

```
{'abc': 1, 'cba': 3}
```

"""


def usun(slownik, liczba):
    """
    Funkcja usuwa ze slownika pary, dla ktorych wartosc rowna jest
    otrzymanej liczbie.
    """
    for klucz in list(slownik.keys())[:]:
        if slownik[klucz] == liczba:
            del slownik[klucz]
    return slownik


def test_usun():
    assert usun({"a": 1, "b": 2, "c": 3, "d": 1}, 1) == {"b": 2, "c": 3}
    assert usun({"a": 1, "b": 2, "c": 3}, 4) == {"a": 1, "b": 2, "c": 3}


if __name__ == "__main__":
    test_usun()
