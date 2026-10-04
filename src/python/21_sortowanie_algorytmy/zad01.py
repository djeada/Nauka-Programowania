r"""
ZAD-01 — Sortowanie bąbelkowe

**Poziom:** ★☆☆
**Tagi:** `sorting`, `bubble-sort`, `list`

### Treść

Napisz funkcję `sortowanie_babelkowe(lista)`, która sortuje listę rosnąco (w miejscu) algorytmem **sortowania bąbelkowego**.

Algorytm wykonuje kolejne **przebiegi**. W jednym przebiegu porównuje kolejne pary sąsiednich elementów — na pozycjach $(0, 1)$, $(1, 2)$, $(2, 3)$, … — i zamienia je miejscami, jeśli lewy element jest **większy** od prawego. Przebiegi powtarza tak długo, aż w całym przebiegu nie zajdzie żadna zamiana — wtedy lista jest posortowana i algorytm się kończy.

Po każdym przebiegu (także po ostatnim, w którym nie było już żadnej zamiany) funkcja wypisuje aktualny stan listy.

### Wejście

* 1. linia: liczba całkowita $n$ — liczba elementów
* 2. linia: $n$ liczb całkowitych oddzielonych spacjami

### Wyjście

Stan listy po każdym przebiegu — każdy w osobnej linii, w formacie listy Pythona. Ostatnia linia to lista posortowana.

### Ograniczenia

* $2 \le n \le 20$
* Elementy są liczbami całkowitymi z przedziału $[-1000, 1000]$.

### Przykład

**Wejście:**

```
5
6 2 1 4 27
```

**Wyjście:**

```
[2, 1, 4, 6, 27]
[1, 2, 4, 6, 27]
[1, 2, 4, 6, 27]
```

W 1. przebiegu zamieniane są pary $(6, 2)$, $(6, 1)$ i $(6, 4)$; w 2. przebiegu para $(2, 1)$; w 3. przebiegu nie ma żadnej zamiany, więc algorytm się kończy.

### Uwagi o algorytmie

* Po każdym przebiegu największy z nieposortowanych elementów „wypływa” na swoje miejsce na końcu listy, dlatego w kolejnych przebiegach możesz zmniejszać zakres sprawdzania o 1 — nie zmienia to wypisywanych stanów.
* Złożoność czasowa: $O(n^2)$, a dla listy już posortowanej — tylko jeden przebieg, czyli $O(n)$.

### Kod startowy

```python
def sortowanie_babelkowe(lista):
    pass


n = int(input())
lista = [int(x) for x in input().split()]
sortowanie_babelkowe(lista)
```

"""


def sortowanie_babelkowe(lista):
    koniec = len(lista) - 1
    while True:
        zamiana = False
        for j in range(koniec):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                zamiana = True
        print(lista)
        if not zamiana:
            break
        koniec -= 1


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    sortowanie_babelkowe(lista)
