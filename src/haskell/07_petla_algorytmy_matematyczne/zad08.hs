{-
ZAD-08 — Naiwny test pierwszości liczby

\**Poziom:** ★★☆
\**Tagi:** `pierwszość`, `pętle`, `dzielniki`

### Treść

Napisz funkcję `czy_pierwsza(n)`, która zwraca `True`, jeśli `n` jest liczbą pierwszą, w przeciwnym razie `False`.

### Wejście

Jeden argument funkcji:

\* `n` (liczba naturalna, `n ≥ 2`)

### Wyjście

Funkcja zwraca wartość logiczną:

\* `True` lub `False`

### Przykład

\**Wywołanie funkcji:**

```python
print(czy_pierwsza(7))
print(czy_pierwsza(4))
```

\**Wyjście:**

```
True
False
```

### Uwagi

\* Dla prostego rozwiązania możesz sprawdzać dzielniki od `2` do `n-1`.
\* Dla szybszego rozwiązania możesz sprawdzać dzielniki do `⌊sqrt(n)⌋`.

-}
czyPierwsza :: Int -> Bool
czyPierwsza n
  | n < 2 = False
  | n == 2 = True
  | otherwise = null [x | x <- [2 .. floor (sqrt (fromIntegral n))], n `mod` x == 0]

main :: IO ()
main = do
  print $ czyPierwsza 7
  print $ czyPierwsza 4
