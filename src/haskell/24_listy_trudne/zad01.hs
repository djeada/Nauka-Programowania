{-
ZAD-01 — Najdłuższy ciąg jedynek

\**Poziom:** ★★☆
\**Tagi:** `list`, `0/1`, `analiza`, `indeksy`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Znajdź **indeks zera**, które po zamianie na `1` da **najdłuższy ciąg kolejnych jedynek**.

Jeśli lista składa się wyłącznie z zer **albo** wyłącznie z jedynek — wypisz `-1`.

### Wejście

\* 1 linia: lista `A` (tylko `0` i `1`)

### Wyjście

\* 1 linia: indeks (liczba całkowita) albo `-1`

### Przykład

\**Wejście:**

```
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
```

\**Wyjście:**

```
7
```

### Uwagi

\* Jeśli kilka zer daje ten sam maksymalny wynik — wybierz to o **najmniejszym indeksie** (jeśli nie określono inaczej w testach).

-}
import Text.Read (readMaybe)

-- Najdłuższy ciąg jedynek po zamianie jednego zera
-- Złożoność czasowa: O(n^2)
-- Złożoność pamięciowa: O(1)
findBestZeroToFlip :: [Int] -> Int
findBestZeroToFlip xs
  | all (== 0) xs || all (== 1) xs = -1
  | otherwise = snd $ maximum [(consecutiveOnes i, i) | (i, x) <- zip [0 ..] xs, x == 0]
  where
    consecutiveOnes idx =
      let (before, _ : after) = splitAt idx xs
          countBack = length $ takeWhile (== 1) (reverse before)
          countForward = length $ takeWhile (== 1) after
       in countBack + countForward + 1

main :: IO ()
main = do
  input <- getLine
  case readMaybe input :: Maybe [Int] of
    Just xs -> print $ findBestZeroToFlip xs
    Nothing -> print (-1 :: Int)
