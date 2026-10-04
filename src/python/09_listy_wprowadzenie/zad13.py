r"""
ZAD-13 — Brakujący element w ciągu arytmetycznym

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `ciąg arytmetyczny`, `listy`

### Treść

Wczytaj listę `n` liczb naturalnych. Po uzupełnieniu o **jeden brakujący wyraz** i uporządkowaniu rosnąco elementy listy tworzą ciąg arytmetyczny. Znajdź i wypisz brakujący wyraz.

Brakujący wyraz nie jest ani pierwszym, ani ostatnim wyrazem ciągu (leży między najmniejszym a największym elementem listy). Elementy listy mogą być podane w dowolnej kolejności.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` różnych liczb naturalnych oddzielonych spacjami

### Wyjście

Jedna liczba naturalna: brakujący wyraz ciągu.

### Ograniczenia

* $n \ge 2$
* Różnica ciągu jest dodatnia (elementy są różne).

### Przykład

**Wejście:**

```
4
5 2 1 3
```

**Wyjście:**

```
4
```

Po uzupełnieniu i uporządkowaniu otrzymujemy ciąg $1, 2, 3, 4, 5$.

### Uwagi

* Pełny ciąg ma $n + 1$ wyrazów, od najmniejszego do największego elementu listy. Suma wyrazów ciągu arytmetycznego to $\frac{(a_1 + a_{n+1})(n + 1)}{2}$.

"""


def brakujacy_element(lista):
    """Zwraca brakujący wyraz ciągu arytmetycznego (n + 1 wyrazów, jeden brakuje)."""
    liczba_wyrazow = len(lista) + 1
    suma_ciagu = (min(lista) + max(lista)) * liczba_wyrazow // 2
    return suma_ciagu - sum(lista)


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(brakujacy_element(lista))
