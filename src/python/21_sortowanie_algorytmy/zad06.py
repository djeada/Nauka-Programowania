r"""
ZAD-06 — Wyszukiwanie binarne

**Poziom:** ★★☆
**Tagi:** `searching`, `binary-search`, `list`

### Treść

Napisz funkcję `wyszukiwanie_binarne(lista, klucz)`, która w liście posortowanej rosnąco znajduje indeks elementu równego `klucz` algorytmem **wyszukiwania binarnego**:

1. Ustaw granice przeszukiwanego fragmentu: `lo = 0`, `hi = n - 1`.
2. Dopóki `lo <= hi`:
   * wyznacz środek `mid = (lo + hi) // 2` i zapamiętaj go na liście sprawdzonych indeksów,
   * jeśli `lista[mid] == klucz` — klucz znaleziony, wynikiem jest `mid`,
   * jeśli `lista[mid] < klucz` — klucz może być tylko na prawo od środka: `lo = mid + 1`,
   * w przeciwnym razie — tylko na lewo od środka: `hi = mid - 1`.
3. Jeśli fragment stał się pusty (`lo > hi`), klucza nie ma w liście — wynikiem jest `-1`.

Funkcja wypisuje listę sprawdzonych indeksów i zwraca wynik, który program wypisuje w następnej linii.

### Wejście

* 1. linia: liczba elementów $n$
* 2. linia: $n$ różnych liczb całkowitych posortowanych rosnąco, oddzielonych spacjami
* 3. linia: liczba całkowita $x$ — szukany klucz

### Wyjście

* 1. linia: kolejno sprawdzane indeksy `mid` w formacie listy Pythona, np. `[3, 5]`
* 2. linia: indeks elementu równego $x$ albo `-1`, jeśli takiego elementu nie ma

### Ograniczenia

* $1 \le n \le 1000$
* Elementy listy są różne i są liczbami całkowitymi z przedziału $[-10^6, 10^6]$.

### Przykład

**Wejście:**

```
8
1 3 5 7 9 11 13 15
11
```

**Wyjście:**

```
[3, 5]
5
```

Najpierw sprawdzamy `mid = (0 + 7) // 2 = 3`: `lista[3] = 7 < 11`, więc `lo = 4`. Potem `mid = (4 + 7) // 2 = 5`: `lista[5] = 11` — znaleziono.

### Uwagi o algorytmie

* Każde sprawdzenie zmniejsza przeszukiwany fragment mniej więcej o połowę, dlatego liczba sprawdzeń nie przekracza $\lfloor \log_2 n \rfloor + 1$ — dla $n = 1000$ to najwyżej 10 sprawdzeń, a dla miliona elementów najwyżej 20. Złożoność czasowa: $O(\log n)$.
* Wyszukiwanie binarne działa tylko na liście **posortowanej**.

### Kod startowy

```python
def wyszukiwanie_binarne(lista, klucz):
    pass


n = int(input())
lista = [int(x) for x in input().split()]
klucz = int(input())
print(wyszukiwanie_binarne(lista, klucz))
```

"""


def wyszukiwanie_binarne(lista, klucz):
    sprawdzone = []
    wynik = -1
    lo, hi = 0, len(lista) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        sprawdzone.append(mid)
        if lista[mid] == klucz:
            wynik = mid
            break
        if lista[mid] < klucz:
            lo = mid + 1
        else:
            hi = mid - 1
    print(sprawdzone)
    return wynik


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    klucz = int(input())
    print(wyszukiwanie_binarne(lista, klucz))
