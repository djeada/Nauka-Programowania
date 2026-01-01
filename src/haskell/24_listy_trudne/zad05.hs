{-
ZAD-05 — Zbiór potęgowy listy

\**Poziom:** ★★★
\**Tagi:** `list`, `subsets`, `combinatorics`

### Treść

Otrzymujesz listę liczb naturalnych (mogą występować powtórzenia). Wygeneruj zbiór wszystkich możliwych podzbiorów tej listy.

Wynik ma zawierać wszystkie podzbiory (włącznie z pustym).

### Wejście

\* 1 linia: lista liczb naturalnych `A`

### Wyjście

\* 1 linia: lista list (wszystkie podzbiory)

### Przykład

\**Wejście:**

```
[1, 2, 1]
```

\**Wyjście:**

```
[[], [1], [2], [1, 2], [1, 1], [2, 1], [1, 1, 2], [1, 2, 1]]
```

### Uwagi

\* Jeśli sprawdzarka wymaga konkretnej kolejności podzbiorów, musi być ona opisana w treści — w przeciwnym razie dopuszczalna może być dowolna. (Jeśli chcesz, mogę dopisać sztywną konwencję kolejności, ale bez rozwiązań.)

-}
import Text.Read (readMaybe)

-- Zbiór potęgowy listy
-- Złożoność czasowa: O(2^n * n)
-- Złożoność pamięciowa: O(2^n * n)
powerSet :: [a] -> [[a]]
powerSet [] = [[]]
powerSet (x:xs) = 
    let ps = powerSet xs
    in ps ++ map (x:) ps

main :: IO ()
main = do
    input <- getLine
    case readMaybe input :: Maybe [Int] of
        Just xs -> print $ powerSet xs
        Nothing -> print ([] :: [[Int]])
