{-
ZAD-01 — Słownik: liczby i ich kwadraty

\**Poziom:** ★☆☆
\**Tagi:** `dict`, `pętla`

### Treść

Wczytaj liczbę `n`. Utwórz słownik, gdzie klucze to liczby od `1` do `n-1`, a wartości to ich kwadraty.

### Wejście

\* 1 linia: `n` (n ≥ 1)

### Wyjście

\* Słownik w postaci: `{1: 1, 2: 4, ...}`

### Przykład

\**Wejście:**

```
5
```

\**Wyjście:**

```
{1: 1, 2: 4, 3: 9, 4: 16}
```

-}

import Data.Map (Map)
import qualified Data.Map as Map

-- Tworzy słownik liczb i ich kwadratów
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    n <- readLn :: IO Int
    let dict = Map.fromList [(i, i*i) | i <- [1..n-1]]
    putStrLn $ formatMap dict

-- Formatuje mapę w stylu Pythona
formatMap :: (Show k, Show v) => Map k v -> String
formatMap m = "{" ++ intercalate ", " [show k ++ ": " ++ show v | (k, v) <- Map.toList m] ++ "}"
    where intercalate sep = concat . intersperse sep
          intersperse _ [] = []
          intersperse _ [x] = [x]
          intersperse sep (x:xs) = x : sep : intersperse sep xs
