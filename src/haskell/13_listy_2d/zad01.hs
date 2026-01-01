{-
ZAD-01 — Macierz z identycznymi wierszami 0..b

\**Poziom:** ★☆☆
\**Tagi:** `macierze`, `pętle`, `print`

### Treść

Wczytaj `a` i `b`. Wypisz macierz składającą się z `a` identycznych wierszy, gdzie każdy wiersz to liczby od `0` do `b` włącznie.

### Wejście

\* 1. linia: `a`
\* 2. linia: `b`

### Wyjście

\* `a` wierszy, w każdym: `0 1 2 ... b`

### Przykład

\**Wejście:**

```
3
2
```

\**Wyjście:**

```
0 1 2
0 1 2
0 1 2
```

-}

import Data.List (intercalate)

main :: IO ()
main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    let wiersz = [0..b]
    let macierz = replicate a wiersz
    mapM_ (putStrLn . intercalate " " . map show) macierz
