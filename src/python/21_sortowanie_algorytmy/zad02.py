r"""
ZAD-02 — Sortowanie przez wybieranie

**Poziom:** ★★☆
**Tagi:** `sorting`, `selection-sort`, `list`

### Treść

Napisz funkcję `sortowanie_przez_wybieranie(lista)`, która sortuje listę rosnąco (w miejscu) algorytmem **sortowania przez wybieranie**.

Dla każdej pozycji $i = 0, 1, \dots, n-2$:

1. znajdź najmniejszy element we fragmencie od pozycji $i$ do końca listy — jeśli najmniejsza wartość występuje w nim kilka razy, wybierz jej **pierwsze** wystąpienie (o najmniejszym indeksie),
2. zamień ten element z elementem na pozycji $i$ (jeśli to ta sama pozycja, lista się nie zmienia),
3. wypisz aktualny stan listy.

### Wejście

* 1. linia: liczba całkowita $n$ — liczba elementów
* 2. linia: $n$ liczb całkowitych oddzielonych spacjami

### Wyjście

$n - 1$ linii: stan listy po każdym kroku $i$, w formacie listy Pythona. Ostatnia linia to lista posortowana.

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
[1, 2, 6, 4, 27]
[1, 2, 6, 4, 27]
[1, 2, 4, 6, 27]
[1, 2, 4, 6, 27]
```

Krok $i = 0$: najmniejszy element to `1` — zamieniamy go z `6`. Krok $i = 1$: najmniejszy z `[2, 6, 4, 27]` to `2`, stoi już na swoim miejscu. Krok $i = 2$: zamieniamy `4` z `6`.

### Uwagi o algorytmie

* Po kroku $i$ na pozycjach $0, \dots, i$ stoją już najmniejsze elementy listy w kolejności rosnącej.
* Złożoność czasowa: $O(n^2)$ — niezależnie od danych.

### Kod startowy

```python
def sortowanie_przez_wybieranie(lista):
    pass


n = int(input())
lista = [int(x) for x in input().split()]
sortowanie_przez_wybieranie(lista)
```

"""


def sortowanie_przez_wybieranie(lista):
    n = len(lista)
    for i in range(n - 1):
        i_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[i_min]:
                i_min = j
        lista[i], lista[i_min] = lista[i_min], lista[i]
        print(lista)


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    sortowanie_przez_wybieranie(lista)
