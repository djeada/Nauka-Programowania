r"""
ZAD-17 — Konwersja listy na napis

**Poziom:** ★☆☆
**Tagi:** `napisy`, `listy`, `str`

### Treść

Napisz funkcję `lista_na_napis(liczby)`, która otrzymuje listę liczb naturalnych i zwraca napis powstały przez zapisanie tych liczb jedna za drugą, bez separatorów (każdą liczbę zamień na napis funkcją `str`).

Program wczytuje listę liczb, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczby naturalne oddzielone spacjami (co najmniej jedna)

### Wyjście

Jedna linia: napis z połączonych liczb.

### Przykład

**Wejście:**

```
2 4 7
```

**Wyjście:**

```
247
```

### Kod startowy

```python
def lista_na_napis(liczby):
    pass


liczby = [int(x) for x in input().split()]
print(lista_na_napis(liczby))
```

"""


def lista_na_napis(liczby):
    napis = ""
    for liczba in liczby:
        napis += str(liczba)
    return napis


if __name__ == "__main__":
    liczby = [int(x) for x in input().split()]
    print(lista_na_napis(liczby))
