{-
ZAD-03 — Pierwsze wystąpienie klucza

\**Poziom:** ★☆☆
\**Tagi:** `listy`, `wyszukiwanie`, `indeksy`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego wystąpienia `klucz` w liście.
Jeśli `klucz` nie występuje — wypisz `-1`.

### Wejście

\* 1. linia: `N` (`N ≥ 1`)
\* kolejne `N` linii: liczby całkowite
\* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna liczba całkowita — indeks (od `0`) lub `-1`.

### Przykład

\**Wejście:**

```
5
2
9
-1
3
8
-1
```

\**Wyjście:**

```
2
```

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1..n]
  klucz <- readLn :: IO Int
  
  let findIndex _ [] = -1
      findIndex x (y:ys)
        | x == y = 0
        | otherwise = let idx = findIndex x ys
                      in if idx == -1 then -1 else idx + 1
  
  print $ findIndex klucz nums
