{-
ZAD-06 — Rotacje napisów

\**Poziom:** ★★★
\**Tagi:** `string`, `rotation`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Sprawdź, czy jeden z nich jest **rotacją** drugiego (mają tę samą długość i da się uzyskać jeden przez przesunięcie cykliczne drugiego).

### Wejście

\* 1 linia: napis `A`
\* 2 linia: napis `B`

### Wyjście

\* 1 linia: `Prawda` albo `Fałsz`

### Przykład

\**Wejście:**

```
malpka
pkamal
```

\**Wyjście:**

```
Prawda
```

-}
import Data.List (isInfixOf)

-- Rotacje napisów
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
isRotation :: String -> String -> Bool
isRotation a b = length a == length b && a `isInfixOf` (b ++ b)

main :: IO ()
main = do
  a <- getLine
  b <- getLine
  putStrLn $ if isRotation a b then "Prawda" else "Fałsz"
