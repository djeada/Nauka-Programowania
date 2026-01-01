{-
ZAD-02 — Wypisywanie cyfr liczby w odwrotnej kolejności

\**Poziom:** ★☆☆
\**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz jej cyfry w kolejności od cyfry jedności (czyli w odwrotnej kolejności niż w zapisie liczby). Każdą cyfrę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

\* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Kolejne cyfry `n` w odwrotnej kolejności, każda w nowej linii.

### Przykład

\**Wejście:**

```
8214
```

\**Wyjście:**

```
4
1
2
8
```

### Uwagi o formatowaniu

\* Dla `n = 0` wypisz jedną linię z `0`.

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  let printDigitsReverse num
        | num == 0 = print 0
        | otherwise = mapM_ print $ reverse $ map (\c -> read [c] :: Int) $ show num
  printDigitsReverse n
