"""
ZAD-09 — Znaki występujące co najmniej dwa razy

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Wypisz napis złożony z **unikalnych** znaków, które występują co najmniej 2 razy, w kolejności pierwszego pojawienia się w wejściu.

### Wejście

* 1 linia: napis

### Wyjście

* 1 linia: wynikowy napis

### Przykład

**Wejście:**

```
aaabbbccc
```

**Wyjście:**

```
abc
```

"""


def znaki_powtarzajace_sie_wiecej_niz_raz(napis):
    """
    Funkcja zwraca liste znakow powtarzajacych sie wiecej niz raz.
    """
    znaki = []
    for znak in napis:
        if napis.count(znak) > 1:
            znaki.append(znak)
    return znaki


def test_znaki_powtarzajace_sie_wiecej_niz_raz():
    assert znaki_powtarzajace_sie_wiecej_niz_raz("ababab") == ["a", "b"]
    assert znaki_powtarzajace_sie_wiecej_niz_raz("abc") == []


if __name__ == "__main__":

    test_znaki_powtarzajace_sie_wiecej_niz_raz()
