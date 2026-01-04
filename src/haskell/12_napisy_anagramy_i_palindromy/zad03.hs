{-
ZAD-03 — Czy dwa słowa są anagramami?

\**Poziom:** ★☆☆
\**Tagi:** `anagram`, `sortowanie`, `zliczanie`

### Treść

Wczytaj dwa słowa i sprawdź, czy są anagramami (czy da się utworzyć jedno przez przestawienie liter drugiego).

### Wejście

\* 1. linia: słowo `s1`
\* 2. linia: słowo `s2`

### Wyjście

Jedna linia:

\* `Prawda` — jeśli anagramy
\* `Fałsz` — jeśli nie

### Przykład

\**Wejście:**

```
ula
lua
```

\**Wyjście:**

```
Prawda
```

### Uwagi

\* Najprościej: porównaj posortowane litery albo słowniki zliczeń znaków.

-}

import Data.List (sort)

-- Sprawdza czy dwa słowa są anagramami
-- Złożoność czasowa: O(n log n), gdzie n to długość słowa
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  s1 <- getLine
  s2 <- getLine
  if sort s1 == sort s2
    then putStrLn "Prawda"
    else putStrLn "Fałsz"
