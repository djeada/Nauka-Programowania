{-
ZAD-04 — Usuń powtórzenia znaków

\**Poziom:** ★★★
\**Tagi:** `string`, `set`, `unique`, `kolejność`

### Treść

Otrzymujesz napis. Usuń wszystkie powtórzenia znaków tak, aby **każdy znak wystąpił tylko raz**, zachowując **kolejność pierwszych wystąpień**.

### Wejście

\* 1 linia: napis `S`

### Wyjście

\* 1 linia: napis z unikalnymi znakami

### Przykład

\**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

\**Wyjście:**

```
AB
```

-}
import Data.List (nub)

-- Usuń wszystkie powtórzenia znaków
-- Złożoność czasowa: O(n^2)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  text <- getLine
  putStrLn $ nub text
