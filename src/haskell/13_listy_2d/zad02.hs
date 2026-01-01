{-
ZAD-02 — Macierz n×n: iloczyn indeksów

\**Poziom:** ★☆☆
\**Tagi:** `macierze`, `pętle zagnieżdżone`

### Treść

Wczytaj `n`. Utwórz i wypisz macierz `n×n`, gdzie element `[i][j]` (indeksy od 0) ma wartość `i*j`.

### Wejście

\* 1. linia: `n`

### Wyjście

\* `n` wierszy po `n` liczb

### Przykład

\**Wejście:**

```
3
```

\**Wyjście:**

```
0 0 0
0 1 2
0 2 4
```

-}

import Data.List (intercalate)

main :: IO ()
main = do
    n <- readLn :: IO Int
    let macierz = [[i * j | j <- [0..n-1]] | i <- [0..n-1]]
    mapM_ (putStrLn . intercalate " " . map show) macierz
