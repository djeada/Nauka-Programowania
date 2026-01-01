{-
ZAD-01 — Odwróć napis

\**Poziom:** ★☆☆
\**Tagi:** `string`, `I/O`

### Treść

Wczytaj napis i wypisz go od tyłu.

### Wejście

\* 1. linia: napis

### Wyjście

\* 1. linia: odwrócony napis

### Przykład

\**Wejście:**

```
barszcz
```

\**Wyjście:**

```
zczsrab
```

-}

-- Odwraca podany napis
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    napis <- getLine
    putStrLn (reverse napis)
