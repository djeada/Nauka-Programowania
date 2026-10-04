r"""
ZAD-03 — Sortowanie przez wstawianie

**Poziom:** ★★☆
**Tagi:** `sorting`, `insertion-sort`, `list`

### Treść

Napisz funkcję `sortowanie_przez_wstawianie(lista)`, która sortuje listę rosnąco (w miejscu) algorytmem **sortowania przez wstawianie**.

Algorytm buduje posortowany fragment od lewej strony. Dla każdej pozycji $i = 1, 2, \dots, n-1$:

1. zapamiętaj element `lista[i]` (klucz),
2. przesuwaj o jedną pozycję w prawo te elementy posortowanego fragmentu `lista[0..i-1]`, które są **większe** od klucza (idąc od prawej strony),
3. wstaw klucz na zwolnione miejsce,
4. wypisz aktualny stan listy.

### Wejście

* 1. linia: liczba całkowita $n$ — liczba elementów
* 2. linia: $n$ liczb całkowitych oddzielonych spacjami

### Wyjście

$n - 1$ linii: stan listy po wstawieniu każdego kolejnego elementu, w formacie listy Pythona. Ostatnia linia to lista posortowana.

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
[2, 6, 1, 4, 27]
[1, 2, 6, 4, 27]
[1, 2, 4, 6, 27]
[1, 2, 4, 6, 27]
```

Najpierw `2` trafia przed `6`, potem `1` przed `2`, potem `4` między `2` a `6`; `27` zostaje na swoim miejscu.

### Uwagi o algorytmie

* Po kroku $i$ fragment `lista[0..i]` jest posortowany, a reszta listy jest jeszcze nieruszona.
* Algorytm działa bardzo szybko dla danych prawie posortowanych; w najgorszym przypadku ma złożoność $O(n^2)$.

### Kod startowy

```python
def sortowanie_przez_wstawianie(lista):
    pass


n = int(input())
lista = [int(x) for x in input().split()]
sortowanie_przez_wstawianie(lista)
```

"""


def sortowanie_przez_wstawianie(lista):
    for i in range(1, len(lista)):
        klucz = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > klucz:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = klucz
        print(lista)


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    sortowanie_przez_wstawianie(lista)
