{-
ZAD-08 — Wypisz pionowo słowa ze zdania

\**Poziom:** ★☆☆
\**Tagi:** `split`, `string`

### Treść

Wczytaj zdanie, podziel na słowa i wypisz każde słowo w osobnej linii. Interpunkcja nie jest słowem.

### Wejście

\* 1. linia: zdanie

### Wyjście

\* wiele linii: słowa w kolejności występowania

### Przykład

\**Wejście:**

```
Ala ma kota
```

\**Wyjście:**

```
Ala
ma
kota
```

-}

-- Dzieli zdanie na słowa i wypisuje każde w osobnej linii
-- Złożoność czasowa: O(n), gdzie n to długość zdania
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    zdanie <- getLine
    let slowa = words zdanie
    mapM_ putStrLn slowa
