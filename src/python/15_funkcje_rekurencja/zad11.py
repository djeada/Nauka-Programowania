r"""
ZAD-11 — Fibonacci z zapamiętywaniem

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `Fibonacci`, `memoizacja`

### Treść

Oblicz $F_N$ — $N$-ty wyraz ciągu Fibonacciego ($F_0 = 0$, $F_1 = 1$, $F_n = F_{n-1} + F_{n-2}$), ale tym razem dla $N$ aż do $90$. Prosta rekurencja z ZAD-05 nie zdąży: dla $N = 90$ wykonałaby około $10^{19}$ wywołań.

Napisz rekurencyjną funkcję `fibonacci(n, pamiec)`, która **zapamiętuje** obliczone wyniki (memoizacja): `pamiec` to lista, w której `pamiec[k]` jest równe `None`, dopóki $F_k$ nie zostało obliczone, a potem przechowuje jego wartość. Każdy wyraz ciągu jest wtedy liczony tylko raz.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — wartość $F_N$.

### Ograniczenia

* `0 ≤ N ≤ 90`

### Przykład

**Wejście:**

```
40
```

**Wyjście:**

```
102334155
```

### Uwagi

* Funkcja: jeśli $n < 2$, zwróć $n$. Jeśli `pamiec[n]` nie jest `None`, zwróć zapamiętaną wartość. W przeciwnym razie oblicz `fibonacci(n - 1, pamiec) + fibonacci(n - 2, pamiec)`, zapisz wynik w `pamiec[n]` i zwróć go.
* Porównanie liczby wywołań: wersja bez pamięci liczy te same wyrazy wielokrotnie — dla $N$ wykonuje $2F_{N+1} - 1$ wywołań, czyli liczba wywołań rośnie **wykładniczo** (dla $N = 40$ to już ponad 300 milionów). Wersja z pamięcią oblicza każdy wyraz raz, więc wykonuje mniej niż $2N$ wywołań — liczba wywołań rośnie **liniowo**.
* Dla chętnych: Python ma gotowy mechanizm zapamiętywania. Dekorator `@lru_cache` z modułu `functools`, dopisany nad definicją funkcji, sam zapamiętuje wyniki dla każdego argumentu:

  ```python
  from functools import lru_cache

  @lru_cache(maxsize=None)
  def fib(n):
      if n < 2:
          return n
      return fib(n - 1) + fib(n - 2)
  ```

### Kod startowy

```python
def fibonacci(n, pamiec):
    pass


n = int(input())
pamiec = [None] * (n + 1)
print(fibonacci(n, pamiec))
```

"""


def fibonacci(n, pamiec):
    """Zwraca F_n; pamiec[k] przechowuje obliczone F_k (albo None)."""
    if n < 2:
        return n
    if pamiec[n] is None:
        pamiec[n] = fibonacci(n - 1, pamiec) + fibonacci(n - 2, pamiec)
    return pamiec[n]


if __name__ == "__main__":
    n = int(input())
    pamiec = [None] * (n + 1)
    print(fibonacci(n, pamiec))
