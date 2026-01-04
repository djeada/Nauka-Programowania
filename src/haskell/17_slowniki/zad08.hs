{-
ZAD-08 — Najczęstsza litera w zdaniu

\**Poziom:** ★☆☆
\**Tagi:** `dict`, `string`

### Treść

Wczytaj zdanie. Zignoruj spacje i znaki interpunkcyjne. Znajdź literę występującą najczęściej.
Jeśli jest kilka, wybierz tę, która **pojawia się jako pierwsza w zdaniu**.

### Wejście

\* 1 linia: zdanie

### Wyjście

\* 1 znak

### Przykład

\**Wejście:**

```
lezy jerzy na wiezy
```

\**Wyjście:**

```
e
```

-}

import Data.Map (Map)
import qualified Data.Map as Map

-- Zliczanie wystąpień słów
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  text <- getLine
  let words' = words text
  let wordCount = Map.fromListWith (+) [(w, 1) | w <- words']
  print wordCount
