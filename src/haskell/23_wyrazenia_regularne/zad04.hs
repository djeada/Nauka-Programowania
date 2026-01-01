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

import Data.Char (isUpper, isLower, isDigit)

-- Walidacja hasła
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(1)
validatePassword :: String -> Bool
validatePassword pwd = 
    length pwd >= 8 &&
    any isUpper pwd &&
    any isLower pwd &&
    any isDigit pwd &&
    any (`elem` "!@#$%^&*()_+-=[]{}|;:,.<>?") pwd

main :: IO ()
main = do
    password <- getLine
    putStrLn $ if validatePassword password then "Prawda" else "Fałsz"
