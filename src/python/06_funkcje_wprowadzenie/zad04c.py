r"""
ZAD-04C — Środkowa z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`, `max`, `warunki`

### Treść

Napisz funkcję `srodkowa_z_trzech(a, b, c)`, która zwraca **środkową** z trzech liczb naturalnych, czyli tę, która po ustawieniu liczb od najmniejszej do największej znajdzie się w środku (tzw. medianę trzech liczb).

Program wczytuje `a`, `b` i `c`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba naturalna `a`
* 2. linia: liczba naturalna `b`
* 3. linia: liczba naturalna `c`

### Wyjście

Jedna liczba naturalna: środkowa z liczb `a`, `b`, `c`.

### Ograniczenia

* $a \ge 0$, $b \ge 0$, $c \ge 0$

### Przykład

**Wejście:**

```
3
1
2
```

**Wyjście:**

```
2
```

Po uporządkowaniu liczby tworzą ciąg $1, 2, 3$ — w środku stoi $2$.

### Uwagi

* Liczby mogą się powtarzać: dla `5`, `5`, `1` uporządkowany ciąg to $1, 5, 5$, więc wynikiem jest `5`.
* Nie sortuj liczb — wystarczą porównania. Liczba `a` jest środkowa, jeśli $b \le a \le c$ albo $c \le a \le b$; podobnie sprawdzisz `b`, a jeśli żadna z nich nie jest środkowa, zostaje `c`.
* Inny sposób: suma trzech liczb minus najmniejsza i minus największa z nich to właśnie liczba środkowa.

### Kod startowy

```python
def srodkowa_z_trzech(a, b, c):
    pass


a = int(input())
b = int(input())
c = int(input())
print(srodkowa_z_trzech(a, b, c))
```

"""


def srodkowa_z_trzech(a, b, c):
    """Zwraca środkową (medianę) z trzech liczb, używając tylko porównań."""
    if b <= a <= c or c <= a <= b:
        return a
    if a <= b <= c or c <= b <= a:
        return b
    return c


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(srodkowa_z_trzech(a, b, c))
