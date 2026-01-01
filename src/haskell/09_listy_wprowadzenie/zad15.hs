{-
ZAD-15 — Element dominujący

\**Poziom:** ★★☆
\**Tagi:** `zliczanie`, `dict`, `majority`

### Treść

Wczytaj listę liczb naturalnych. Jeśli istnieje liczba, która występuje **więcej niż N/2 razy**, wypisz ją. W przeciwnym razie wypisz `-1`.

### Wejście

\* 1. linia: `N` (`N ≥ 1`)
\* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — element dominujący lub `-1`.

### Przykład

\**Wejście:**

```
5
4
7
4
4
2
```

\**Wyjście:**

```
4
```

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1..n]
  
  let count x = length $ filter (== x) nums
  let majority = filter (\x -> count x > n `div` 2) $ nub nums
  
  if null majority
    then print (-1)
    else print $ head majority
  where
    nub [] = []
    nub (x:xs) = x : nub (filter (/= x) xs)
