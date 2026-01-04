{-
ZAD-02 — Wczytaj, zmodyfikuj i wypisz

\**Poziom:** ★☆☆
\**Tagi:** `listy`, `indeksy`, `modyfikacja`

### Treść

Wczytaj `N` oraz `N` liczb całkowitych do listy. Następnie:

a) Zwiększ każdy element o `1`.
b) Pomnóż każdy element przez jego indeks (indeksy od `0`).
c) Zastąp wszystkie elementy wartością pierwszego elementu.

Po każdym podpunkcie wypisz wynikową listę w **jednej** linii, elementy oddzielone przecinkami.

### Wejście

\* 1. linia: `N` (`N ≥ 1`)
\* kolejne `N` linii: liczby całkowite

### Wyjście

Trzy linie:

1. wynik po (a)
2. wynik po (b)
3. wynik po (c)

Elementy w linii oddzielone przecinkami (bez spacji).

### Przykład

\**Wejście:**

```
3
3
9
7
```

\**Wyjście:**

```
4,10,8
0,9,14
3,3,3
```

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1 .. n]

  -- a) Zwiększ każdy element o 1
  let resA = map (+ 1) nums
  putStrLn $ intercalate "," $ map show resA

  -- b) Pomnóż każdy element przez jego indeks
  let resB = zipWith (*) nums [0 ..]
  putStrLn $ intercalate "," $ map show resB

  -- c) Zastąp wszystkie elementy wartością pierwszego
  let resC = replicate n (head nums)
  putStrLn $ intercalate "," $ map show resC
  where
    intercalate sep [] = ""
    intercalate sep [x] = x
    intercalate sep (x : xs) = x ++ sep ++ intercalate sep xs
