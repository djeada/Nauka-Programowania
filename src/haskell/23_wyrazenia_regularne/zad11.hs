{-
ZAD-11 — Nazwa pliku bez rozszerzenia

\**Poziom:** ★★☆
\**Tagi:** `regex`, `string`, `ścieżki`

### Treść

Otrzymujesz napis reprezentujący pełną ścieżkę do pliku. Wyodrębnij nazwę pliku (bez katalogów) i usuń rozszerzenie (część po ostatniej kropce). Zwróć samą nazwę bez rozszerzenia.

Ścieżka może zawierać separator `\` lub `/`.

### Wejście

Jedna linia:

\* `sciezka`

### Wyjście

Jedna linia:

\* `nazwa_pliku_bez_rozszerzenia`

### Przykład

\**Wejście:**

```
C:\my-long\path_directory\file.html
```

\**Wyjście:**

```
file
```

-}

-- Dzielenie tekstu według separatora
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
splitText :: Char -> String -> [String]
splitText sep text = 
    case break (== sep) text of
        (part, []) -> [part]
        (part, _:rest) -> part : splitText sep rest

main :: IO ()
main = do
    sep <- getLine
    text <- getLine
    let separator = if null sep then ',' else head sep
    print $ splitText separator text
