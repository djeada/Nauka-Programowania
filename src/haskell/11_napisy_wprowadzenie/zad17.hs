{-
ZAD-17 — Konwersja listy na napis

\**Poziom:** ★☆☆
\**Tagi:** `list`, `string`

### Treść

Otrzymujesz listę liczb naturalnych w zapisie tekstowym (np. `[2, 4, 7]`). Połącz liczby bez separatorów i wypisz jako napis.

### Wejście

\* 1. linia: lista w formacie podobnym do Pythona, np. `[2, 4, 7]`

### Wyjście

\* 1. linia: napis z połączonych liczb, np. `247`

### Przykład

\**Wejście:**

```
[2, 4, 7]
```

\**Wyjście:**

```
247
```

### Uwagi

\* Najprościej: usuń nawiasy `[` `]`, rozdziel po przecinkach, `strip()`, potem sklej.

-}

import Data.Char (isDigit)

-- Parsuje listę liczb w formacie [2, 4, 7] i łączy je w napis
-- Złożoność czasowa: O(n), gdzie n to liczba elementów w liście
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    linia <- getLine
    -- Usuń nawiasy i podziel po przecinkach
    let bezNawiasow = filter (\c -> c /= '[' && c /= ']') linia
    let liczbyStr = map (filter isDigit) $ words $ map (\c -> if c == ',' then ' ' else c) bezNawiasow
    let wynik = concat liczbyStr
    putStrLn wynik
