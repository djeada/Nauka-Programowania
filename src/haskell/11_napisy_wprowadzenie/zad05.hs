{-
ZAD-05 — Co k-ty znak poziomo i pionowo

\**Poziom:** ★☆☆
\**Tagi:** `string`, `slicing`, `pętle`

### Treść

Wczytaj napis i liczbę `k`.

a) Wypisz co `k`-ty znak w jednym wierszu, oddzielając znaki spacjami.
b) Wypisz co `k`-ty znak pionowo (każdy w osobnej linii).

### Wejście

\* 1. linia: napis
\* 2. linia: liczba naturalna `k` (k ≥ 1)

### Wyjście

\* (a) 1 linia: znaki oddzielone spacjami
\* (b) wiele linii: każdy znak osobno

### Przykład

\**Wejście:**

```
Grzechotnik
3
```

\**Wyjście:**

```
z h n
z
h
n
```

### Uwagi o formatowaniu

\* Dokładnie jedna spacja między znakami w punkcie (a), bez spacji na końcu linii.

-}

import Data.List (intercalate)

-- Pobiera co k-ty znak z napisu (indeksowanie od 0)
-- Złożoność czasowa: O(n/k), gdzie n to długość napisu
-- Złożoność pamięciowa: O(n/k)
coKtyZnak :: String -> Int -> String
coKtyZnak napis k = [napis !! i | i <- [k-1, k-1+k .. length napis - 1]]

-- Wypisuje co k-ty znak poziomo i pionowo
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(n/k)
main :: IO ()
main = do
    napis <- getLine
    k <- readLn :: IO Int
    let znaki = coKtyZnak napis k
    -- Wypisz poziomo z spacjami
    putStrLn $ intercalate " " $ map (:[]) znaki
    -- Wypisz pionowo
    mapM_ putStrLn $ map (:[]) znaki
