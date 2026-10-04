r"""
ZAD-03 — Suma elementów dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `iteracja`, `indeksy`

### Treść

Wczytaj dwie listy liczb całkowitych i utwórz listę, w której element o indeksie `i` jest sumą elementów o indeksie `i` z obu list.
Jeśli któraś lista jest krótsza, jej brakujące elementy traktuj jak `0` (wynik ma więc długość dłuższej listy).

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: lista sum, np. `[5, 9, 8, 10]`.

### Przykład

**Wejście:**

```
3 1 2 5
2 8 6 5
```

**Wyjście:**

```
[5, 9, 8, 10]
```

"""


def suma_list(lista_a, lista_b):
    wynik = []
    for i in range(max(len(lista_a), len(lista_b))):
        a = lista_a[i] if i < len(lista_a) else 0
        b = lista_b[i] if i < len(lista_b) else 0
        wynik.append(a + b)
    return wynik


if __name__ == "__main__":
    lista_a = [int(x) for x in input().split()]
    lista_b = [int(x) for x in input().split()]

    print(suma_list(lista_a, lista_b))
