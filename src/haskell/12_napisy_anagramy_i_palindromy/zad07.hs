{-
ZAD-07 — Minimalna liczba usunięć, aby uzyskać anagramy

\**Poziom:** ★★★
\**Tagi:** `anagram`, `zliczanie`, `greedy`

### Treść

Wczytaj dwa słowa. Jeśli mają różne długości, wypisz `-1`.
W przeciwnym razie oblicz minimalną liczbę znaków, które trzeba usunąć (łącznie z obu słów), aby pozostałe napisy były anagramami.

### Wejście

\* 1. linia: słowo `s1`
\* 2. linia: słowo `s2`

### Wyjście

\* jedna liczba całkowita: minimalna liczba usunięć lub `-1`

### Przykład

\**Wejście:**

```
grazyna
razynax
```

\**Wyjście:**

```
2
```

### Uwagi

\* Dla tej samej długości: policz zliczenia liter i zsumuj wartości `abs(c1[lit] - c2[lit])`, a wynik wypisz jako tę sumę. (To jest łączna liczba usunięć.)

-}

import Data.Map (Map)
import qualified Data.Map as Map

countChars :: String -> Map Char Int
countChars s = Map.fromListWith (+) [(c, 1) | c <- s]

main :: IO ()
main = do
    s1 <- getLine
    s2 <- getLine
    if length s1 /= length s2
        then print (-1)
        else do
            let counts1 = countChars s1
            let counts2 = countChars s2
            let allChars = Map.keys (Map.union counts1 counts2)
            let diffs = [abs (Map.findWithDefault 0 c counts1 - Map.findWithDefault 0 c counts2) | c <- allChars]
            print $ sum diffs
