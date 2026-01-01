{-
ZAD-15 — Słowa jako lista

\**Poziom:** ★☆☆
\**Tagi:** `split`, `list`

### Treść

Wczytaj zdanie i wypisz listę słów w formacie `["Ala", "ma", "kota"]`.

### Wejście

\* 1. linia: zdanie

### Wyjście

\* 1. linia: lista słów (jak w przykładzie)

### Przykład

\**Wejście:**

```
Ala ma kota
```

\**Wyjście:**

```
["Ala", "ma", "kota"]
```

-}

-- Wypisuje listę słów w formacie ["słowo1", "słowo2", ...]
-- Złożoność czasowa: O(n), gdzie n to długość zdania
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    zdanie <- getLine
    let slowa = words zdanie
    putStrLn $ "[" ++ concat [if i == 0 then "\"" ++ w ++ "\"" else ", \"" ++ w ++ "\"" | (w, i) <- zip slowa [0..]] ++ "]"
