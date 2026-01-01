{-
ZAD-03 — Sortowanie listy par względem kryterium

\**Poziom:** ★☆☆
\**Tagi:** `sort`, `tuple`, `list`

### Treść

Otrzymujesz listę par `(napis, liczba)`.

a) Posortuj pary rosnąco po liczbie.
b) Posortuj pary rosnąco po długości napisu.

Wypisz wyniki dla a) i b) w osobnych liniach.

### Wejście

\* 1 linia: liczba naturalna `N`
\* następnie `N` linii: `napis liczba` (napis bez spacji)

### Wyjście

\* 1 linia: lista par posortowana jak w podpunkcie a)
\* 2 linia: lista par posortowana jak w podpunkcie b)

### Przykład

\**Wejście:**

```
3
ab 3
bca 1
c 2
```

\**Wyjście:**

```
[('bca', 1), ('c', 2), ('ab', 3)]
[('c', 2), ('ab', 3), ('bca', 1)]
```

-}

import Data.List (sortBy)
import Data.Ord (comparing)

-- Sortowanie po długości słowa
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    zdanie <- getLine
    let slowa = words zdanie
    let posortowane = sortBy (comparing length) slowa
    putStrLn $ unwords posortowane
