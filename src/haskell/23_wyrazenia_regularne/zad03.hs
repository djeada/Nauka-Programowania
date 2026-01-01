{-
ZAD-03 — Sprawdź, czy napis składa się wyłącznie z cyfr

\**Poziom:** ★☆☆
\**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis. Sprawdź, czy składa się wyłącznie z cyfr (`0–9`).

### Wejście

Jedna linia:

\* `s`

### Wyjście

Jedna linia:

\* `Prawda` — jeśli napis zawiera tylko cyfry
\* `Fałsz` — w przeciwnym razie

### Przykład

\**Wejście:**

```
1234
```

\**Wyjście:**

```
Prawda
```

-}

import Data.List (isPrefixOf)

-- Wyciąganie URL z tekstu (uproszczona wersja)
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
extractURLs :: String -> [String]
extractURLs text = filter isURL $ words text
    where
        isURL w = any (`isPrefixOf` w) ["http://", "https://", "www."]

main :: IO ()
main = do
    text <- getLine
    let urls = extractURLs text
    print urls
