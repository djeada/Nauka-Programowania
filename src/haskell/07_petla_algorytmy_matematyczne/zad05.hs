{-
ZAD-05 — Największy wspólny dzielnik (NWD)

\**Poziom:** ★☆☆
\**Tagi:** `Euklides`, `modulo`, `pętle`

### Treść

Napisz funkcję `nwd(a, b)`, która zwraca największy wspólny dzielnik dwóch liczb naturalnych.

### Wejście

Dwa argumenty funkcji:

\* `a` (liczba naturalna, `a > 0`)
\* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWD(a, b)`.

### Przykład

\**Wywołanie funkcji:**

```python
print(nwd(60, 45))
```

\**Wyjście:**

```
15
```

-}
nwd :: Int -> Int -> Int
nwd a b
  | b == 0 = a
  | otherwise = nwd b (a `mod` b)

main :: IO ()
main = do
  print $ nwd 60 45
