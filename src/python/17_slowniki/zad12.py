"""
ZAD-12 — Porównanie dwóch słowników z listami (kolejność list bez znaczenia)

**Poziom:** ★★☆
**Tagi:** `dict`, `porównanie`, `list`

### Treść

Wczytaj dwa „słowniki” (opis w wejściu). Dla każdego klucza wartościami są listy liczb całkowitych, ale **kolejność w listach nie ma znaczenia**.
Wypisz `Prawda` jeśli słowniki są identyczne (te same klucze i te same wielozbiory wartości), w przeciwnym razie `Fałsz`.

### Wejście

* Najpierw:

  * 1 linia: `n`
  * następnie `n` linii: `klucz v1 v2 v3 ...` (co najmniej jedna wartość)
* Potem:

  * 1 linia: `m`
  * następnie `m` linii: `klucz v1 v2 v3 ...`

### Wyjście

* `Prawda` lub `Fałsz`

### Przykład

**Wejście:**

```
2
a 1 2 3
b 4 5
2
a 3 2 1
b 5 4
```

**Wyjście:**

```
Prawda
```

"""


def czy_slowniki_identyczne(slownik_a, slownik_b):
    """
    Funkcja sprawdza czy dwa slowniki maja takie same elementy.
    """
    for klucz in slownik_a:
        if klucz not in slownik_b:
            return False
        elif sorted(slownik_a[klucz]) != sorted(slownik_b[klucz]):
            return False
    return True


def test_czy_slowniki_identyczne():

    assert czy_slowniki_identyczne(
        {"a": [1, 2, 3], "b": [4, 5, 6]}, {"a": [3, 1, 2], "b": [5, 4, 6]}
    )


if __name__ == "__main__":

    test_czy_slowniki_identyczne()
