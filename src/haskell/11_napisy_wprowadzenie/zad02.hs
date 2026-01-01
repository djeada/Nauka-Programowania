{-
ZAD-02 — Policz wystąpienia znaku

\**Poziom:** ★☆☆
\**Tagi:** `string`, `count`

### Treść

Wczytaj napis oraz jeden znak. Wypisz, ile razy ten znak występuje w napisie.

### Wejście

\* 1. linia: napis
\* 2. linia: pojedynczy znak

### Wyjście

\* 1. linia: liczba wystąpień

### Przykład

\**Wejście:**

```
klamra
a
```

\**Wyjście:**

```
2
```

-}

-- Zlicza wystąpienia znaku w napisie
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(1)
main :: IO ()
main = do
    napis <- getLine
    znak <- getLine
    case znak of
        (c:_) -> do
            let liczba = length $ filter (== c) napis
            print liczba
        [] -> print 0
