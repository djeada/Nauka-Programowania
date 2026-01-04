{-
ZAD-06 — Histogram znaków w słowie

\**Poziom:** ★☆☆
\**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Zwróć słownik: znak → liczba wystąpień.

### Wejście

\* 1 linia: napis

### Wyjście

\* Słownik, np. `{'k': 1, 'l': 1, 'a': 2, 's': 1}`

### Przykład

\**Wejście:**

```
klasa
```

\**Wyjście:**

```
{'k': 1, 'l': 1, 'a': 2, 's': 1}
```

-}

import Data.List (group, intercalate, sort)
import Data.Map (Map)
import qualified Data.Map as Map

-- Histogram znaków w słowie
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  napis <- getLine
  let histogram = Map.fromListWith (+) [(c, 1) | c <- napis]
  putStrLn $ "{" ++ intercalate ", " ["'" ++ [k] ++ "': " ++ show v | (k, v) <- Map.toList histogram] ++ "}"
