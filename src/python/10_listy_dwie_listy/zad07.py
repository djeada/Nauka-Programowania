r"""
ZAD-07 — Różnica między dwoma listami

**Poziom:** ★☆☆
**Tagi:** `listy`, `różnica symetryczna`

### Treść

Wczytaj dwie listy liczb całkowitych i utwórz listę elementów, które występują **tylko w jednej** z list (tzw. różnica symetryczna).

* Najpierw umieść elementy listy 1, których nie ma w liście 2 (w kolejności z listy 1), a potem elementy listy 2, których nie ma w liście 1 (w kolejności z listy 2).
* Każdy element umieść w wyniku **tylko raz**, nawet jeśli w liście się powtarza.
* Jeśli takich elementów nie ma, wypisz `[]`.

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: lista elementów występujących tylko w jednej z list.

### Przykład

**Wejście:**

```
9 2 5 4
4 2 1
```

**Wyjście:**

```
[9, 5, 1]
```

"""


def roznica_symetryczna(lista_a, lista_b):
    wynik = []
    for element in lista_a:
        if element not in lista_b and element not in wynik:
            wynik.append(element)
    for element in lista_b:
        if element not in lista_a and element not in wynik:
            wynik.append(element)
    return wynik


if __name__ == "__main__":
    lista_a = [int(x) for x in input().split()]
    lista_b = [int(x) for x in input().split()]

    print(roznica_symetryczna(lista_a, lista_b))
