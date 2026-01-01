{-
ZAD-03 — Sprawdzanie warunków logicznych

\**Poziom:** ★☆☆
\**Tagi:** `funkcje`, `bool`, `warunki`

### Treść

Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca cztery wartości logiczne (np. jako krotkę) odpowiadające warunkom:

a) Czy `a > b`?
b) Czy `a + b < 10`?
c) Czy obie liczby są nieparzyste?
d) Czy `max(a, b) < a^2`?

### Wejście

Dwa argumenty funkcji:

\* `a` (liczba całkowita, `a ≥ 0`)
\* `b` (liczba całkowita, `b ≥ 0`)

### Wyjście

Cztery wartości logiczne w kolejności a), b), c), d).

### Przykład

\**Wywołanie funkcji:**

```python
A, B, C, D = sprawdz_warunki(3, 2)
print(A)
print(B)
print(C)
print(D)
```

\**Wyjście:**

```
True
True
False
True
```

-}
sprawdzWarunki :: Int -> Int -> (Bool, Bool, Bool, Bool)
sprawdzWarunki a b = (condA, condB, condC, condD)
  where
    condA = a > b
    condB = a + b < 10
    condC = odd a && odd b
    condD = max a b < a * a

main :: IO ()
main = do
  let (condA, condB, condC, condD) = sprawdzWarunki 3 2
  print condA
  print condB
  print condC
  print condD
