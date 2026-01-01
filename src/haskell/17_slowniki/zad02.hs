{-
ZAD-02 — Słownik z dwóch list (klucze i wartości)

\**Poziom:** ★☆☆
\**Tagi:** `dict`, `listy`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, utwórz słownik: klucz z pierwszej listy → wartość z drugiej listy.
Jeśli długości są różne, wypisz pusty słownik `{}`.

### Wejście

\* 1 linia: `n`
\* 2 linia: `m`
\* następnie `n` liczb (pierwsza lista)
\* następnie `m` liczb (druga lista)

### Wyjście

\* Słownik albo `{}`

### Przykład

\**Wejście:**

```
3
3
3 5 8
1 2 -1
```

\**Wyjście:**

```
{3: 1, 5: 2, 8: -1}
```

-}

import Data.Map (Map)
import qualified Data.Map as Map
import Data.List (intercalate)

-- Tworzy słownik z dwóch list
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    n <- readLn :: IO Int
    m <- readLn :: IO Int
    keys <- map read . words <$> getLine :: IO [Int]
    values <- map read . words <$> getLine :: IO [Int]
    
    if n /= m
        then putStrLn "{}"
        else do
            let dict = Map.fromList $ zip keys values
            putStrLn $ "{" ++ intercalate ", " [show k ++ ": " ++ show v | (k, v) <- Map.toList dict] ++ "}"
