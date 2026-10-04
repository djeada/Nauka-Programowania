{-
ZAD-04 — Silnia

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `silnia`

### Treść

Napisz rekurencyjną funkcję `silnia(n)`, która zwraca $n! = 1 \cdot 2 \cdot \ldots \cdot n$, korzystając z zależności $0! = 1$ oraz $n! = n \cdot (n-1)!$ dla $n \ge 1$.

Program wczytuje $N$ i wypisuje $N!$.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — wartość $N!$.

### Ograniczenia

* `0 ≤ N ≤ 20`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
6
```

$3! = 3 \cdot 2 \cdot 1 = 6$.

### Kod startowy

```python
def silnia(n):
    pass


n = int(input())
print(silnia(n))
```

-}

import Control.Monad (unless)

-- Zwraca n! dla n >= 0.
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n) - przez stos rekurencji
silnia :: Integer -> Integer
silnia 0 = 1
silnia n = n * silnia (n - 1)

main :: IO ()
main = do
  let testy =
        [ silnia 0 == 1,
          silnia 3 == 6,
          silnia 10 == 3628800,
          silnia 20 == 2432902008176640000
        ]
  unless (and testy) $ error "Test nie przeszedl"
  putStrLn "Wszystkie testy zakonczone sukcesem"
