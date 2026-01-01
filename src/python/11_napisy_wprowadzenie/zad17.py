"""
ZAD-17 — Konwersja listy na napis

**Poziom:** ★☆☆
**Tagi:** `list`, `string`

### Treść

Otrzymujesz listę liczb naturalnych w zapisie tekstowym (np. `[2, 4, 7]`). Połącz liczby bez separatorów i wypisz jako napis.

### Wejście

* 1. linia: lista w formacie podobnym do Pythona, np. `[2, 4, 7]`

### Wyjście

* 1. linia: napis z połączonych liczb, np. `247`

### Przykład

**Wejście:**

```
[2, 4, 7]
```

**Wyjście:**

```
247
```

### Uwagi

* Najprościej: usuń nawiasy `[` `]`, rozdziel po przecinkach, `strip()`, potem sklej.

"""


def znamien_na_napis(lista):
    napis = ""
    for liczba in lista:
        napis += str(liczba)
    return napis


def test_znamien_na_napis():
    assert znamien_na_napis([1, 2, 3, 4, 5]) == "12345"


if __name__ == "__main__":

    test_znamien_na_napis()
