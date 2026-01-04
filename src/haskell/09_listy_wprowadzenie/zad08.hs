{-
ZAD-08 — Usuń klucz

\**Poziom:** ★☆☆
\**Tagi:** `listy`, `remove`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych oraz `klucz`. Usuń **pierwsze** wystąpienie `klucz` (jeśli istnieje). Następnie wypisz listę po modyfikacji w jednej linii, elementy oddzielone przecinkami.

### Wejście

\* 1. linia: `N` (`N ≥ 1`)
\* kolejne `N` linii: liczby całkowite
\* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna linia: lista po usunięciu, elementy oddzielone przecinkami.

### Przykład

\**Wejście:**

```
5
6
2
1
4
27
4
```

\**Wyjście:**

```
6,2,1,27
```

### Uwagi

\* Jeśli `klucz` nie występuje, wypisz listę bez zmian.

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1 .. n]
  klucz <- readLn :: IO Int

  let removeFirst _ [] = []
      removeFirst k (x : xs)
        | x == k = xs
        | otherwise = x : removeFirst k xs

  let result = removeFirst klucz nums
  let intercalate sep [] = ""
      intercalate sep [x] = x
      intercalate sep (x : xs) = x ++ sep ++ intercalate sep xs

  putStrLn $ intercalate "," $ map show result
