{-
ZAD-01 — Wczytaj i wypisz

\**Poziom:** ★☆☆
\**Tagi:** `listy`, `I/O`, `odwracanie`

### Treść

Wczytaj `N`, następnie `N` liczb całkowitych do listy.

a) Wypisz elementy listy od początku do końca — każdy w osobnej linii.
b) Wypisz elementy listy od końca do początku — w **jednej** linii, oddzielone przecinkami (bez spacji).

### Wejście

\* 1. linia: `N` (`N ≥ 1`)
\* kolejne `N` linii: liczby całkowite

### Wyjście

a) `N` linii — elementy w kolejności wczytania.
b) 1 linia — elementy w kolejności odwrotnej, oddzielone przecinkami.

### Przykład

\**Wejście:**

```
3
8
12
7
```

\**Wyjście:**

```
8
12
7
7,12,8
```

### Uwagi o formatowaniu

\* W podpunkcie (b) nie dodawaj przecinka na końcu.

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1..n]
  
  -- a) Wypisz elementy od początku do końca
  mapM_ print nums
  
  -- b) Wypisz elementy od końca do początku, oddzielone przecinkami
  putStrLn $ intercalate "," $ map show $ reverse nums
  where
    intercalate sep [] = ""
    intercalate sep [x] = x
    intercalate sep (x:xs) = x ++ sep ++ intercalate sep xs
