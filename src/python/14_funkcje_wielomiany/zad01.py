r"""
ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `Horner`

### Treść

Napisz funkcję `wartosc_wielomianu(wspolczynniki, x)`, która otrzymuje listę współczynników wielomianu $W(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0$ oraz liczbę $x$ i zwraca wartość $W(x)$.

Program wczytuje wielomian i liczbę $x$, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych `a_n a_{n-1} ... a_0`
* 3. linia: `x` — liczba całkowita

### Wyjście

Jedna liczba całkowita — wartość wielomianu w punkcie `x`.

### Ograniczenia

* `0 ≤ n ≤ 10`
* `-100 ≤ a_i ≤ 100`, `-10 ≤ x ≤ 10`

### Przykład

**Wejście:**

```
2
3 2 1
1
```

**Wyjście:**

```
6
```

Wielomian to $3x^2 + 2x + 1$, a $3 \cdot 1^2 + 2 \cdot 1 + 1 = 6$.

### Uwagi

* Najprościej skorzystać ze **schematu Hornera**: $W(x) = (\dots((a_n x + a_{n-1}) x + a_{n-2}) x + \dots) x + a_0$. Zacznij od wyniku równego `0` i dla każdego kolejnego współczynnika `a` wykonaj `wynik = wynik * x + a`.

### Kod startowy

```python
def wartosc_wielomianu(wspolczynniki, x):
    pass


n = int(input())
wspolczynniki = [int(s) for s in input().split()]
x = int(input())
print(wartosc_wielomianu(wspolczynniki, x))
```

"""


def wartosc_wielomianu(wspolczynniki, x):
    """Zwraca wartość wielomianu w punkcie x (schemat Hornera)."""
    wynik = 0
    for a in wspolczynniki:
        wynik = wynik * x + a
    return wynik


if __name__ == "__main__":
    n = int(input())
    wspolczynniki = [int(s) for s in input().split()]
    x = int(input())
    print(wartosc_wielomianu(wspolczynniki, x))
