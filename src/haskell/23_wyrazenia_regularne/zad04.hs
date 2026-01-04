{-
ZAD-04 — Sprawdź, czy słowo występuje w zdaniu jako osobne słowo

\**Poziom:** ★☆☆
\**Tagi:** `regex`, `string`

### Treść

Otrzymujesz dwa napisy: zdanie oraz słowo. Sprawdź, czy słowo występuje w zdaniu jako samodzielne słowo (nie jako fragment innego słowa).

### Wejście

Dwie linie:

1. `zdanie`
2. `slowo`

### Wyjście

Jedna linia:

\* `Prawda` albo `Fałsz`

### Przykład

\**Wejście:**

```
Siała baba mak.
babcia
```

\**Wyjście:**

```
Fałsz
```

-}

import Data.Char (isAlphaNum)

-- Sprawdź, czy słowo występuje w zdaniu jako osobne słowo
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
containsWholeWord :: String -> String -> Bool
containsWholeWord sentence word = word `elem` words (map replaceNonAlnum sentence)
  where
    replaceNonAlnum c = if isAlphaNum c then c else ' '

main :: IO ()
main = do
  sentence <- getLine
  word <- getLine
  putStrLn $ if containsWholeWord sentence word then "Prawda" else "Fałsz"
