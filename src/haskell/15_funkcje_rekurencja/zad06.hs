{-
ZAD-06 — N-ty wyraz ciągu danego wzorem rekurencyjnym

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `ciągi`

### Treść

Ciąg jest zdefiniowany wzorem rekurencyjnym:

* $a_1 = 1$,
* $a_n = 1 + 2 \cdot a_{n-1}$ dla $n \ge 2$.

Napisz rekurencyjną funkcję `wyraz_ciagu(n)`, która zwraca $a_n$. Program wczytuje $N$ i wypisuje $a_N$.

### Wejście

Jedna liczba naturalna `N` (`N ≥ 1`).

### Wyjście

Jedna liczba naturalna — wartość $a_N$.

### Ograniczenia

* `1 ≤ N ≤ 30`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
31
```

Kolejne wyrazy: $a_1 = 1$, $a_2 = 3$, $a_3 = 7$, $a_4 = 15$, $a_5 = 31$.

### Kod startowy

```python
def wyraz_ciagu(n):
    pass


n = int(input())
print(wyraz_ciagu(n))
```

-}

import Control.Monad (unless)

-- a_1 = 1, a_n = 1 + 2 * a_(n-1)
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n) - przez stos rekurencji
wyrazCiagu :: Int -> Integer
wyrazCiagu 1 = 1
wyrazCiagu n = 1 + 2 * wyrazCiagu (n - 1)

main :: IO ()
main = do
  let testy =
        [ wyrazCiagu 1 == 1,
          wyrazCiagu 5 == 31,
          wyrazCiagu 10 == 1023,
          wyrazCiagu 30 == 1073741823
        ]
  unless (and testy) $ error "Test nie przeszedl"
  putStrLn "Wszystkie testy zakonczone sukcesem"
