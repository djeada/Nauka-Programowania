{-
ZAD-06 — Najmniejsza wspólna wielokrotność (NWW)

\**Poziom:** ★☆☆
\**Tagi:** `nww`, `nwd`, `arytmetyka`

### Treść

Napisz funkcję `nww(a, b)`, która zwraca najmniejszą wspólną wielokrotność liczb `a` i `b`.

### Wejście

Dwa argumenty funkcji:

\* `a` (liczba naturalna, `a > 0`)
\* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWW(a, b)`.

### Przykład

\**Wywołanie funkcji:**

```python
print(nww(7, 9))
```

\**Wyjście:**

```
63
```

### Ograniczenia / gwarancje

\* Możesz użyć zależności: `NWW(a, b) = (a * b) // NWD(a, b)`.

-}
nwd :: Int -> Int -> Int
nwd a b
  | b == 0 = a
  | otherwise = nwd b (a `mod` b)

nww :: Int -> Int -> Int
nww a b = (a * b) `div` nwd a b

main :: IO ()
main = do
  print $ nww 7 9
