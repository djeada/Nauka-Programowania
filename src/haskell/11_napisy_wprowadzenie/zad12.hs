{-
ZAD-12 — Usuń spacje ze zdania

\**Poziom:** ★☆☆
\**Tagi:** `replace`, `string`

### Treść

Wczytaj zdanie i usuń z niego wszystkie spacje.

### Wejście

\* 1. linia: zdanie

### Wyjście

\* 1. linia: zdanie bez spacji

### Przykład

\**Wejście:**

```
Ala ma kota
```

\**Wyjście:**

```
Alamakota
```

-}

-- Usuwa wszystkie spacje z napisu
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    zdanie <- getLine
    let bezSpacji = filter (/= ' ') zdanie
    putStrLn bezSpacji
