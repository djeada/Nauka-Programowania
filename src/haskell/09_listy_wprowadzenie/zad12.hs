{-
ZAD-12 — Rotacja w lewo / prawo

\**Poziom:** ★★☆
\**Tagi:** `listy`, `rotacja`, `modulo`

### Treść

Wczytaj listę liczb całkowitych, a następnie:

\* `kierunek = 0` → rotacja w lewo,
\* `kierunek = 1` → rotacja w prawo,

o `K` pozycji (gdzie `K ≥ 0`). Wypisz listę po rotacji, przecinkami bez spacji.

### Wejście

\* 1. linia: `N` (`N ≥ 1`)
\* kolejne `N` linii: liczby całkowite
\* kolejna linia: `kierunek` (0 lub 1)
\* ostatnia linia: `K` (`K ≥ 0`)

### Wyjście

Jedna linia: lista po rotacji, elementy oddzielone przecinkami.

### Przykład

\**Wejście:**

```
7
5
27
6
2
1
10
8
0
2
```

\**Wyjście:**

```
6,2,1,10,8,5,27
```

### Uwagi

\* Zredukuj `K` przez `K % N`.

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1 .. n]
  kierunek <- readLn :: IO Int
  k <- readLn :: IO Int

  let intercalate sep [] = ""
      intercalate sep [x] = x
      intercalate sep (x : xs) = x ++ sep ++ intercalate sep xs
  let k' = k `mod` n
  let result =
        if kierunek == 0
          then drop k' nums ++ take k' nums -- lewo
          else drop (n - k') nums ++ take (n - k') nums -- prawo
  putStrLn $ intercalate "," $ map show result
