{-
ZAD-16 — Indeksy pierwszej pary o sumie x

\**Poziom:** ★★☆
\**Tagi:** `hashmap`, `indeksy`, `2-sum`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `x`. Znajdź indeksy **pierwszej** pary `(i, j)` (z `i < j`) takiej, że `lista[i] + lista[j] == x`.

Jeśli nie istnieje taka para — wypisz `-1 -1`.

### Wejście

\* 1. linia: `N` (`N ≥ 2`)
\* kolejne `N` linii: liczby całkowite
\* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Dwie liczby całkowite w jednej linii (oddzielone spacją): `i j` albo `-1 -1`.

### Przykład

\**Wejście:**

```
5
1
3
4
5
2
5
```

\**Wyjście:**

```
0 2
```

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1..n]
  x <- readLn :: IO Int
  
  let findPair [] = Nothing
      findPair (a:as) = case [j | (j, b) <- zip [1..] as, a + b == x] of
        (j:_) -> Just (0, j)
        [] -> case findPair as of
          Just (i, j) -> Just (i+1, j+1)
          Nothing -> Nothing
  
  case findPair nums of
    Just (i, j) -> putStrLn $ show i ++ " " ++ show j
    Nothing -> putStrLn "-1 -1"
