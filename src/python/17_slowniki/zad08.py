"""
ZAD-08 — Najczęstsza litera w zdaniu

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj zdanie. Zignoruj spacje i znaki interpunkcyjne. Znajdź literę występującą najczęściej.
Jeśli jest kilka, wybierz tę, która **pojawia się jako pierwsza w zdaniu**.

### Wejście

* 1 linia: zdanie

### Wyjście

* 1 znak

### Przykład

**Wejście:**

```
lezy jerzy na wiezy
```

**Wyjście:**

```
e
```

"""


def najczestsza_litera(napis):
    """
    Zwraca najczesciej wystepujaca litere w napisie.
    """
    slownik = {}
    for litera in napis:
        if litera in slownik:
            slownik[litera] += 1
        else:
            slownik[litera] = 1
    return max(slownik, key=slownik.get)


def test_najczestsza_litera():

    assert najczestsza_litera("ala ma kota") == "a"


if __name__ == "__main__":

    test_najczestsza_litera()
