r"""
ZAD-02 — Połączenie dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `indeksy`, `łączenie`

### Treść

Wczytaj dwie listy liczb całkowitych i utwórz z nich dwie nowe listy:

a) Listę powstałą przez doklejenie listy 2 na koniec listy 1.
b) Kopię listy 1, w której elementy o **parzystych indeksach** (0, 2, 4, …) zastąpiono elementami listy 2 o tych samych indeksach. Element zastępujesz tylko wtedy, gdy indeks istnieje w obu listach — pozostałe elementy listy 1 zostają bez zmian.

Oba podpunkty wykonaj na **oryginalnych** listach z wejścia.

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

* 1. linia: wynik podpunktu a) jako lista, np. `[1, 2, 3, 4, 5, 6]`
* 2. linia: wynik podpunktu b) jako lista

### Przykład 1

**Wejście:**

```
1 2 3
4 5 6
```

**Wyjście:**

```
[1, 2, 3, 4, 5, 6]
[4, 2, 6]
```

### Przykład 2

**Wejście:**

```
-2 8 3 6
7 5 0
```

**Wyjście:**

```
[-2, 8, 3, 6, 7, 5, 0]
[7, 8, 0, 6]
```

Indeksy parzyste listy 1 to 0 i 2 — ich wartości (`-2` i `3`) zastępujemy wartościami `7` i `0` z listy 2.

"""


def dostaw_na_koniec(lista_a, lista_b):
    return lista_a + lista_b


def podmien_parzyste_indeksy(lista_a, lista_b):
    wynik = lista_a[:]
    for i in range(0, min(len(lista_a), len(lista_b)), 2):
        wynik[i] = lista_b[i]
    return wynik


if __name__ == "__main__":
    lista_a = [int(x) for x in input().split()]
    lista_b = [int(x) for x in input().split()]

    print(dostaw_na_koniec(lista_a, lista_b))
    print(podmien_parzyste_indeksy(lista_a, lista_b))
