{-
ZAD-06 — Zamień litery „a” na „?”

\**Poziom:** ★☆☆
\**Tagi:** `string`, `replace`

### Treść

Wczytaj napis i zamień wszystkie wystąpienia litery `a` na znak `?`.

### Wejście

\* 1. linia: napis

### Wyjście

\* 1. linia: napis po zamianie

### Przykład

\**Wejście:**

```
Latarnik
```

\**Wyjście:**

```
L?t?rnik
```

-}

-- Zamienia wszystkie wystąpienia litery 'a' na '?'
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    napis <- getLine
    let wynik = map (\c -> if c == 'a' then '?' else c) napis
    putStrLn wynik
