r"""
ZAD-07 — Sortowanie listy 0/1/2

**Poziom:** ★★☆
**Tagi:** `sort`, `counting`

### Treść

Wczytaj listę składającą się wyłącznie z liczb `0`, `1` i `2` i posortuj ją rosnąco.

### Wejście

* 1. linia: liczba elementów $N$
* 2. linia: $N$ liczb (każda to `0`, `1` albo `2`) oddzielonych spacjami

### Wyjście

* 1. linia: posortowana lista — liczby oddzielone pojedynczymi spacjami

### Ograniczenia

* $1 \le N \le 1000$

### Przykład

**Wejście:**

```
7
1 0 1 2 2 0 1
```

**Wyjście:**

```
0 0 1 1 1 2 2
```

### Uwagi

* Zadanie da się rozwiązać w czasie $O(N)$, bez sortowania. Najprościej policzyć zera, jedynki i dwójki, a potem wypisać odpowiednio wiele zer, jedynek i dwójek (to sortowanie przez zliczanie z rozdziału 21).
* Ambitniejszy wariant działa w miejscu, w jednym przejściu po liście: trzymaj trzy indeksy — koniec obszaru zer, bieżący element i początek obszaru dwójek — i zamieniaj elementy miejscami (tzw. problem flagi holenderskiej).

"""


def sortuj_liste_012(lista):
    """Sortuje listę w miejscu w jednym przejściu (problem flagi holenderskiej)."""
    poczatek, srodek, koniec = 0, 0, len(lista) - 1
    while srodek <= koniec:
        if lista[srodek] == 0:
            lista[poczatek], lista[srodek] = lista[srodek], lista[poczatek]
            poczatek += 1
            srodek += 1
        elif lista[srodek] == 2:
            lista[srodek], lista[koniec] = lista[koniec], lista[srodek]
            koniec -= 1
        else:
            srodek += 1
    return lista


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(" ".join(str(x) for x in sortuj_liste_012(lista)))
