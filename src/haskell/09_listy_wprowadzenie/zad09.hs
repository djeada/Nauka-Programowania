{-
ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)

\**Poziom:** ★☆☆
\**Tagi:** `listy`, `duplikaty`, `set`

### Treść

Wczytaj listę liczb naturalnych i usuń duplikaty tak, aby każda liczba występowała tylko raz — **zachowując kolejność pierwszego wystąpienia**.

### Wejście

\* 1. linia: `N` (`N ≥ 1`)
\* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna linia: lista bez duplikatów, elementy oddzielone przecinkami.

### Przykład

\**Wejście:**

```
6
3
2
1
3
2
2
```

\**Wyjście:**

```
3,2,1
```

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1 .. n]

  let nub [] = []
      nub (x : xs) = x : nub (filter (/= x) xs)

  let result = nub nums
  let intercalate sep [] = ""
      intercalate sep [x] = x
      intercalate sep (x : xs) = x ++ sep ++ intercalate sep xs

  putStrLn $ intercalate "," $ map show result
