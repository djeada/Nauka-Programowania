r"""
ZAD-02 — Przesuń zera na koniec listy

**Poziom:** ★★☆
**Tagi:** `list`, `stabilność`, `przekształcenie`

### Treść

Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, **zachowując kolejność** pozostałych elementów.

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna linia: `n` liczb listy po przekształceniu, oddzielonych spacjami.

### Ograniczenia

* `1 ≤ n ≤ 1000`
* elementy listy są z przedziału $[-10^6, 10^6]$

### Przykład

**Wejście:**

```
11
0 1 3 0 8 12 0 4 0 7 0
```

**Wyjście:**

```
1 3 8 12 4 7 0 0 0 0 0
```

### Uwagi

* Spróbuj przekształcić listę **w miejscu**, bez tworzenia nowej listy: przepisuj kolejne niezerowe elementy na początek listy, a resztę wypełnij zerami. Takie rozwiązanie działa w czasie $O(n)$.

"""


def przesun_zera(lista):
    """Przenosi zera na koniec listy (w miejscu), zachowując kolejność pozostałych."""
    pozycja = 0

    for x in lista:
        if x != 0:
            lista[pozycja] = x
            pozycja += 1

    for i in range(pozycja, len(lista)):
        lista[i] = 0

    return lista


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(" ".join(str(x) for x in przesun_zera(lista)))
