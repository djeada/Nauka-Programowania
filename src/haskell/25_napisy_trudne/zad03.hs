{-
ZAD-03 — Czy napis A jest początkiem napisu B?

\**Poziom:** ★★☆
\**Tagi:** `string`, `prefix`

### Treść

Otrzymujesz dwa napisy:

1. Napis `A` — potencjalny przedrostek,
2. Napis `B` — napis testowany.

Sprawdź, czy `B` **zaczyna się** od `A`.

### Wejście

\* 1 linia: `A`
\* 2 linia: `B`

### Wyjście

\* 1 linia: `Prawda` albo `Fałsz`

### Przykład

\**Wejście:**

```
Dino
Dinozaur jest zly
```

\**Wyjście:**

```
Prawda
```

-}
import Data.List (isPrefixOf)

-- Czy napis A jest początkiem napisu B?
-- Złożoność czasowa: O(min(m,n))
-- Złożoność pamięciowa: O(1)
main :: IO ()
main = do
    a <- getLine
    b <- getLine
    putStrLn $ if a `isPrefixOf` b then "Prawda" else "Fałsz"
