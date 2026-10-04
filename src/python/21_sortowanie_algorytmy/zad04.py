r"""
ZAD-04 — Sortowanie przez scalanie

**Poziom:** ★★☆
**Tagi:** `sorting`, `merge-sort`, `recursion`

### Treść

Napisz rekurencyjną funkcję `sortowanie_przez_scalanie(lista)`, która zwraca nową, posortowaną rosnąco listę, korzystając z algorytmu **sortowania przez scalanie**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana, zwróć ją.
2. Podziel listę na dwie części: lewa to pierwsze $\lfloor n/2 \rfloor$ elementów (`lista[:n // 2]`), prawa — pozostałe.
3. Rekurencyjnie posortuj najpierw lewą, a potem prawą część.
4. **Scal** obie posortowane części w jedną posortowaną listę (pomocnicza funkcja `scal(lewa, prawa)`), **wypisz** wynik scalenia i go zwróć.

Scalanie: dopóki obie listy mają elementy, porównuj ich pierwsze (najmniejsze) nieużyte elementy i dopisuj do wyniku mniejszy z nich; na koniec dopisz pozostałe elementy.

### Wejście

* 1. linia: liczba całkowita $n$ — liczba elementów
* 2. linia: $n$ liczb całkowitych oddzielonych spacjami

### Wyjście

$n - 1$ linii: wynik każdego scalenia, w kolejności wykonywania, w formacie listy Pythona. Ostatnie scalenie daje całą posortowaną listę.

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
[2, 6]
[4, 27]
[1, 4, 27]
[1, 2, 4, 6, 27]
```

Lista dzieli się na `[6, 2]` i `[1, 4, 27]`. Lewa część daje scalenie `[6]` + `[2]` → `[2, 6]`. Prawa dzieli się na `[1]` i `[4, 27]`; najpierw scalane są `[4]` + `[27]`, potem `[1]` + `[4, 27]`. Na końcu scalane są obie połowy.

### Uwagi o algorytmie

* Złożoność czasowa: $O(n \log n)$.

### Kod startowy

```python
def scal(lewa, prawa):
    pass


def sortowanie_przez_scalanie(lista):
    pass


n = int(input())
lista = [int(x) for x in input().split()]
sortowanie_przez_scalanie(lista)
```

"""


def scal(lewa, prawa):
    wynik = []
    i = j = 0
    while i < len(lewa) and j < len(prawa):
        if lewa[i] <= prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1
    wynik.extend(lewa[i:])
    wynik.extend(prawa[j:])
    return wynik


def sortowanie_przez_scalanie(lista):
    if len(lista) < 2:
        return lista
    srodek = len(lista) // 2
    lewa = sortowanie_przez_scalanie(lista[:srodek])
    prawa = sortowanie_przez_scalanie(lista[srodek:])
    wynik = scal(lewa, prawa)
    print(wynik)
    return wynik


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    sortowanie_przez_scalanie(lista)
