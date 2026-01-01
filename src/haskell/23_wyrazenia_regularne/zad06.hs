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

-- Wyszukiwanie słów zawierających podciąg
-- Złożoność czasowa: O(n*m), gdzie n to liczba słów, m to długość podciągu
-- Złożoność pamięciowa: O(n)
findWords :: String -> String -> [String]
findWords pattern text = filter (pattern `isInfixOf`) (words text)
    where
        isInfixOf [] _ = True
        isInfixOf _ [] = False
        isInfixOf needle haystack@(_:hs)
            | needle `isPrefixOf` haystack = True
            | otherwise = isInfixOf needle hs
        
        isPrefixOf [] _ = True
        isPrefixOf _ [] = False
        isPrefixOf (x:xs) (y:ys) = x == y && isPrefixOf xs ys

main :: IO ()
main = do
    pattern <- getLine
    text <- getLine
    print $ findWords pattern text
