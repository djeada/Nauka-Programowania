r"""
ZAD-12 — Rotacja w lewo / prawo

**Poziom:** ★★☆
**Tagi:** `listy`, `rotacja`, `modulo`

### Treść

Wczytaj listę `n` liczb całkowitych, kierunek rotacji oraz liczbę `k`. Przesuń cyklicznie elementy listy o `k` pozycji:

* `kierunek = 0` — w lewo (pierwszy element trafia na koniec),
* `kierunek = 1` — w prawo (ostatni element trafia na początek).

Wypisz listę po rotacji.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: `kierunek` (`0` albo `1`)
* 4. linia: liczba przesunięć `k`

### Wyjście

Jedna linia: lista po rotacji, w formacie `print(lista)`.

### Ograniczenia

* $n \ge 1$
* $k \ge 0$ (`k` może być większe od `n`)

### Przykład

**Wejście:**

```
7
5 27 6 2 1 10 8
0
2
```

**Wyjście:**

```
[6, 2, 1, 10, 8, 5, 27]
```

### Uwagi

* Rotacja o `n` pozycji nie zmienia listy, więc wystarczy przesunąć ją o $k \bmod n$ pozycji.

"""


def rotacja_w_lewo(lista, k):
    k = k % len(lista)
    return lista[k:] + lista[:k]


def rotacja(lista, kierunek, k):
    """Przesuwa cyklicznie listę o k pozycji: 0 - w lewo, 1 - w prawo."""
    if kierunek == 1:
        k = len(lista) - k % len(lista)
    return rotacja_w_lewo(lista, k)


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    kierunek = int(input())
    k = int(input())
    print(rotacja(lista, kierunek, k))
