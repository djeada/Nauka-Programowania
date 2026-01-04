{-
ZAD-08 — Indeks klucza w cyklicznie posortowanej liście

\**Poziom:** ★★☆
\**Tagi:** `binary search`, `rotacja`, `list`

### Treść

Otrzymujesz cyklicznie posortowaną listę liczb całkowitych (lista była rosnąca, ale została przesunięta) oraz klucz. Znajdź indeks **pierwszego** wystąpienia klucza. Jeśli klucza nie ma — wypisz `-1`.

### Wejście

\* 1 linia: liczba naturalna `N`
\* 2 linia: `N` liczb całkowitych oddzielonych spacjami
\* 3 linia: liczba całkowita `x` (szukany klucz)

### Wyjście

\* 1 linia: indeks pierwszego wystąpienia `x` albo `-1`

### Przykład

\**Wejście:**

```
6
3 4 5 6 1 2
4
```

\**Wyjście:**

```
1
```

### Ograniczenia / gwarancje

\* Lista jest wynikiem rotacji listy posortowanej niemalejąco (mogą wystąpić duplikaty).

-}

import Data.List (elemIndex)
import Data.Maybe (fromMaybe)

-- Indeks klucza w cyklicznie posortowanej liście
-- Złożoność czasowa: O(n) dla prostej implementacji, O(log n) możliwe z binary search
-- Złożoność pamięciowa: O(1)

main :: IO ()
main = do
  _ <- getLine -- Read N but don't use it (list length is implicit)
  numsLine <- getLine
  let nums = map read (words numsLine) :: [Int]
  keyStr <- getLine
  let key = read keyStr :: Int
  let index = fromMaybe (-1) (elemIndex key nums)
  print index
