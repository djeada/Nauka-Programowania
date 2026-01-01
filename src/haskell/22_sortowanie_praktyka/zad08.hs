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

import Data.List (sortBy)

-- Sortowanie niestandardowe
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    putStrLn "Sortowanie niestandardowe"
    -- Przykład: sortowanie według własnej funkcji
    let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    -- Sortowanie: najpierw parzyste, potem nieparzyste
    let sorted = sortBy (\a b -> compare (even b, a) (even a, b)) nums
    print sorted
