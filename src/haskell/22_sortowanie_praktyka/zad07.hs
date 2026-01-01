{-
ZAD-07 — Sortowanie listy 0/1/2

\**Poziom:** ★★☆
\**Tagi:** `sort`, `counting`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0`, `1` lub `2`. Posortuj ją rosnąco.

### Wejście

\* 1 linia: liczba naturalna `N`
\* 2 linia: `N` liczb (0/1/2) oddzielonych spacjami

### Wyjście

\* 1 linia: posortowana lista w formacie jak w przykładzie

### Przykład

\**Wejście:**

```
7
1 0 1 2 2 0 1
```

\**Wyjście:**

```
[0, 0, 1, 1, 1, 2, 2]
```

-}

import Data.List (sortBy)
import Data.Ord (comparing)

-- Sortowanie po wielu kryteriach
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    putStrLn "Sortowanie po wielu kryteriach"
    -- Przykład: sortowanie po długości, potem alfabetycznie
    let slowa = ["kot", "pies", "dom", "auto"]
    let sorted = sortBy (\a b -> compare (length a, a) (length b, b)) slowa
    print sorted
