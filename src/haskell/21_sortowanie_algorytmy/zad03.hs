{-
ZAD-03 — Sortowanie przez wstawianie

\**Poziom:** ★★☆
\**Tagi:** `sorting`, `insertion-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez wstawianie**.
Buduj posortowany fragment od lewej strony: każdy kolejny element „wstaw” w odpowiednie miejsce, przesuwając większe elementy w prawo.

### Wejście

\* 1 linia: lista liczb całkowitych

### Wyjście

\* 1 linia: posortowana lista rosnąco

### Przykład

\**Wejście:**

```
[6, 2, 1, 4, 27]
```

\**Wyjście:**

```
[1, 2, 4, 6, 27]
```

### Uwagi o algorytmie

\* Działa bardzo dobrze dla danych prawie posortowanych.

-}

import Text.Read (readMaybe)

-- Sortowanie przez wstawianie
-- Złożoność czasowa: O(n^2)
-- Złożoność pamięciowa: O(n)
insertionSort :: Ord a => [a] -> [a]
insertionSort [] = []
insertionSort (x:xs) = insert x (insertionSort xs)
    where
        insert y [] = [y]
        insert y (z:zs)
            | y <= z = y : z : zs
            | otherwise = z : insert y zs

parseList :: String -> Maybe [Int]
parseList s = readMaybe s

main :: IO ()
main = do
    input <- getLine
    case parseList input of
        Just xs -> print $ insertionSort xs
        Nothing -> print ([] :: [Int])
