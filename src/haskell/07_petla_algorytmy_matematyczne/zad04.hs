{-
ZAD-04 — Obliczanie silni liczby

\**Poziom:** ★☆☆
\**Tagi:** `pętle`, `silnia`, `mnożenie`

### Treść

Napisz funkcję `silnia(n)`, która zwraca `n!` obliczone przy użyciu pętli.
Przyjmij, że `0! = 1`.

### Wejście

Jeden argument funkcji:

\* `n` (liczba naturalna, `n ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `n!`.

### Przykład

\**Wywołanie funkcji:**

```python
print(silnia(3))
```

\**Wyjście:**

```
6
```

-}
silnia :: Int -> Int
silnia n = product [1..n]

main :: IO ()
main = do
  print $ silnia 3
