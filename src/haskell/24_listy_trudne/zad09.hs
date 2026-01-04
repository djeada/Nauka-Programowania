{-
ZAD-09 — Najdłuższy naprzemienny podciąg

\**Poziom:** ★★★
\**Tagi:** `dp`, `subsequence`, `naprzemienny`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź najdłuższy podciąg naprzemienny, w którym różnice między kolejnymi elementami zmieniają znak (raz dodatnia, raz ujemna, itd.).

### Wejście

\* 1 linia: lista liczb całkowitych `A`

### Wyjście

\* 1 linia: lista liczb — najdłuższy naprzemienny podciąg

### Przykład

\**Wejście:**

```
[1, -2, 6, 4, -3, 2, -4, -3]
```

\**Wyjście:**

```
[1, -2, 6, -3, 2, -4]
```

### Uwagi

\* Jeśli istnieje kilka podciągów o tej samej maksymalnej długości — wybierz ten, który pojawia się „najwcześniej” (najmniejszy możliwy indeks startu), o ile sprawdzarka tego wymaga.

-}
import Text.Read (readMaybe)

-- Najdłuższy podciąg naprzemienny
-- Złożoność czasowa: O(n^2)
-- Złożoność pamięciowa: O(n)
longestAlternating :: [Int] -> [Int]
longestAlternating xs = xs -- For now, just return the input

main :: IO ()
main = do
  input <- getLine
  case readMaybe input :: Maybe [Int] of
    Just xs -> print $ longestAlternating xs
    Nothing -> print ([] :: [Int])
