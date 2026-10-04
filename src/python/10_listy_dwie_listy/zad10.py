r"""
ZAD-10 — Mediana dwóch posortowanych list

**Poziom:** ★★☆
**Tagi:** `listy`, `mediana`, `scalanie`

### Treść

Wczytaj dwie listy liczb całkowitych. Obie są posortowane niemalejąco i mają **tę samą** długość $n \ge 1$.

Znajdź medianę wszystkich $2n$ liczb z obu list. Ponieważ liczb jest parzyście wiele, mediana to średnia arytmetyczna dwóch środkowych wartości po ustawieniu wszystkich liczb w kolejności niemalejącej.

### Wejście

* 1. linia: lista 1 (posortowana niemalejąco) — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 (posortowana niemalejąco, tej samej długości) — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: mediana jako liczba zmiennoprzecinkowa, np. `4.5`. Jeśli mediana jest liczbą całkowitą, wypisz ją z `.0`, np. `4.0`.

### Przykład

**Wejście:**

```
2 4 7
3 5 9
```

**Wyjście:**

```
4.5
```

Po scaleniu otrzymujemy `[2, 3, 4, 5, 7, 9]`; dwie środkowe wartości to `4` i `5`, więc mediana wynosi $\frac{4 + 5}{2} = 4.5$.

"""


def scal(lista_a, lista_b):
    wynik = []
    i = 0
    j = 0
    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i] <= lista_b[j]:
            wynik.append(lista_a[i])
            i += 1
        else:
            wynik.append(lista_b[j])
            j += 1
    return wynik + lista_a[i:] + lista_b[j:]


def mediana_dwoch_list(lista_a, lista_b):
    scalona = scal(lista_a, lista_b)
    srodek = len(scalona) // 2
    return (scalona[srodek - 1] + scalona[srodek]) / 2


if __name__ == "__main__":
    lista_a = [int(x) for x in input().split()]
    lista_b = [int(x) for x in input().split()]

    print(mediana_dwoch_list(lista_a, lista_b))
