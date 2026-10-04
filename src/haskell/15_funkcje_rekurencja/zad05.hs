{-
ZAD-05 — Liczba Fibonacciego

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `Fibonacci`

### Treść

Napisz rekurencyjną funkcję `fibonacci(n)`, która zwraca $n$-ty wyraz ciągu Fibonacciego, zdefiniowanego następująco:

* $F_0 = 0$,
* $F_1 = 1$,
* $F_n = F_{n-1} + F_{n-2}$ dla $n \ge 2$.

Program wczytuje $N$ i wypisuje $F_N$.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — wartość $F_N$.

### Ograniczenia

* `0 ≤ N ≤ 25`

### Przykład

**Wejście:**

```
7
```

**Wyjście:**

```
13
```

Kolejne wyrazy ciągu to `0, 1, 1, 2, 3, 5, 8, 13, …`, a wyraz o numerze `7` (licząc od zera) to `13`.

### Uwagi

* Funkcja ma dwa przypadki bazowe ($n = 0$ i $n = 1$) i wywołuje samą siebie dwa razy.
* Ta prosta wersja wykonuje bardzo dużo powtórzonych obliczeń (liczba wywołań rośnie wykładniczo), ale dla $N \le 25$ działa wystarczająco szybko.

### Kod startowy

```python
def fibonacci(n):
    pass


n = int(input())
print(fibonacci(n))
```

-}

import Control.Monad (unless)

-- Zwraca n-ty wyraz ciągu Fibonacciego (F_0 = 0, F_1 = 1).
-- Złożoność czasowa: O(2^n)
-- Złożoność pamięciowa: O(n) - przez stos rekurencji
fibonacci :: Int -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)

main :: IO ()
main = do
  let testy =
        [ fibonacci 0 == 0,
          fibonacci 1 == 1,
          fibonacci 7 == 13,
          fibonacci 20 == 6765
        ]
  unless (and testy) $ error "Test nie przeszedl"
  putStrLn "Wszystkie testy zakonczone sukcesem"
