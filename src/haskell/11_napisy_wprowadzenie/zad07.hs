{-
ZAD-07 — Zamień znaki na kody ASCII

\**Poziom:** ★☆☆
\**Tagi:** `ASCII`, `ord`, `string`

### Treść

Wczytaj napis i wypisz kody ASCII wszystkich jego znaków, oddzielone przecinkiem i spacją `", "`.

### Wejście

\* 1. linia: napis

### Wyjście

\* 1. linia: kody ASCII oddzielone `, `

### Przykład

\**Wejście:**

```
Robot
```

\**Wyjście:**

```
82, 111, 98, 111, 116
```

-}

import Data.Char (ord)
import Data.List (intercalate)

-- Konwertuje napis na kody ASCII oddzielone ", "
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  napis <- getLine
  let kody = map (show . ord) napis
  putStrLn $ intercalate ", " kody
