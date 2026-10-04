r"""
ZAD-18 — Indeks najmniejszego elementu w przesuniętej liście

**Poziom:** ★★☆
**Tagi:** `binarne`, `rotacja`, `minimum`

### Treść

Wczytaj listę `n` różnych liczb całkowitych, która była posortowana rosnąco, a następnie została cyklicznie przesunięta w prawo o nieznaną liczbę miejsc (być może o zero). Znajdź indeks najmniejszego elementu.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` różnych liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna liczba całkowita: indeks najmniejszego elementu.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
7 8 -1 4 5
```

**Wyjście:**

```
2
```

### Uwagi

* Najmniejszy element to jedyne miejsce, w którym kolejny element listy jest mniejszy od poprzedniego. Jeśli takiego miejsca nie ma, lista nie została przesunięta.

"""


def indeks_minimum(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return i + 1
    return 0


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(indeks_minimum(lista))
