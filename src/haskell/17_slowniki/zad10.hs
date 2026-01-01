{-
ZAD-10 — Znalezienie anagramów w tekście (grupy)

\**Poziom:** ★★☆
\**Tagi:** `dict`, `anagramy`, `string`

### Treść

Wczytaj tekst. Znajdź grupy słów będących anagramami (ignoruj wielkość liter, słowa to tylko litery).
Wypisz wynik jako listę list, np. `[['absurd', 'brudas'], ...]`.
Do grup wypisuj tylko te klucze, które mają co najmniej 2 słowa.

### Wejście

\* 1 linia: tekst

### Wyjście

\* Lista list słów

### Przykład

Wejście jak w treści zadania → wyjście:

```
[["absurd", "brudas"], ["tyran", "narty"], ["bandzior", "zbrodnia"], ["burza", "arbuz"], ["galeria", "alergia"]]
```

-}

import Data.Map (Map)
import qualified Data.Map as Map
import Data.List (sort)

-- Anagramy grupowane
-- Złożoność czasowa: O(n * m log m), gdzie n to liczba słów, m to długość słowa
-- Złożoność pamięciowa: O(n * m)
main :: IO ()
main = do
    putStrLn "Placeholder - anagramy grupowane"
