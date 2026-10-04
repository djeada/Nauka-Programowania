r"""
ZAD-06 — Znalezienie elementów wspólnych dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `część wspólna`

### Treść

Wczytaj dwie listy liczb całkowitych i utwórz listę elementów, które występują **w obu** listach.

* Elementy wyniku ustaw w kolejności ich pierwszego wystąpienia w liście 1.
* Każdy element wspólny umieść w wyniku **tylko raz**, nawet jeśli w listach się powtarza.
* Jeśli listy nie mają elementów wspólnych, wypisz `[]`.

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: lista elementów wspólnych.

### Przykład

**Wejście:**

```
9 2 5 4
4 2 1
```

**Wyjście:**

```
[2, 4]
```

"""


def czesc_wspolna(lista_a, lista_b):
    wynik = []
    for element in lista_a:
        if element in lista_b and element not in wynik:
            wynik.append(element)
    return wynik


if __name__ == "__main__":
    lista_a = [int(x) for x in input().split()]
    lista_b = [int(x) for x in input().split()]

    print(czesc_wspolna(lista_a, lista_b))
