{-
ZAD-09 — Znaki występujące co najmniej dwa razy

\**Poziom:** ★☆☆
\**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Wypisz napis złożony z **unikalnych** znaków, które występują co najmniej 2 razy, w kolejności pierwszego pojawienia się w wejściu.

### Wejście

\* 1 linia: napis

### Wyjście

\* 1 linia: wynikowy napis

### Przykład

\**Wejście:**

```
aaabbbccc
```

\**Wyjście:**

```
abc
```

-}

import Data.Map (Map)
import qualified Data.Map as Map
import Data.List (intercalate)

-- Histogram częstości znaków
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    napis <- getLine
    let freq = Map.fromListWith (+) [(c, 1) | c <- napis]
    putStrLn $ "{" ++ intercalate ", " ["'" ++ [k] ++ "': " ++ show v | (k, v) <- Map.toList freq] ++ "}"
