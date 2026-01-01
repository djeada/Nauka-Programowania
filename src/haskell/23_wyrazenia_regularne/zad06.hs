{-
ZAD-06 — Wiersze kończące się określonym napisem

\**Poziom:** ★☆☆
\**Tagi:** `regex`, `string`, `linijki`

### Treść

Otrzymujesz dwa napisy:

1. tekst wielowierszowy,
2. słowo lub fragment.

Znajdź wszystkie wiersze, które kończą się podanym napisem (wiersz może kończyć się znakiem interpunkcyjnym).

### Wejście

Dwie części:

1. Tekst (wiele wierszy)
2. W osobnej linii: `koncowka`

\*(Sposób wczytania tekstu wielowierszowego zależy od platformy — przyjmij, że tekst jest podany w całości jako wejście, a ostatnia linia to `koncowka`.)*

### Wyjście

Wiersze spełniające warunek, każdy w osobnej linii, w kolejności występowania.

### Przykład

\**Wejście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godności trzeba nie za nic tu cnota,
Miłości pragną nie pragną tu złota.
da
```

\**Wyjście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
```

-}

import Data.Char (isAlphaNum)
import Data.List (isSuffixOf)

-- Wiersze kończące się określonym napisem
-- Złożoność czasowa: O(n*m) gdzie n to liczba wierszy, m to długość końcówki
-- Złożoność pamięciowa: O(n)

-- Usuń znaki interpunkcyjne z końca linii
stripTrailingPunctuation :: String -> String
stripTrailingPunctuation = reverse . dropWhile (not . isAlphaNum) . reverse

-- Sprawdź czy linia kończy się danym napisem (ignorując interpunkcję na końcu)
endsWithPattern :: String -> String -> Bool
endsWithPattern line pattern = pattern `isSuffixOf` stripTrailingPunctuation line

main :: IO ()
main = do
    content <- getContents
    let allLines = lines content
        ending = last allLines
        textLines = init allLines
        matchingLines = filter (`endsWithPattern` ending) textLines
    mapM_ putStrLn matchingLines
