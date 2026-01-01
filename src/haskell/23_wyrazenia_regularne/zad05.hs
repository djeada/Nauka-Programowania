{-
ZAD-05 — Wyodrębnij cyfry z tekstu

\**Poziom:** ★☆☆
\**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis zawierający różne znaki. Wyodrębnij wszystkie cyfry i wypisz je jako jeden napis (z zachowaniem kolejności).

### Wejście

Jedna linia:

\* `tekst`

### Wyjście

Jedna linia:

\* napis złożony tylko z cyfr z tekstu wejściowego

### Przykład

\**Wejście:**

```
Terminator2001
```

\**Wyjście:**

```
2001
```

-}

-- Zamiana formatu daty (DD-MM-YYYY -> YYYY-MM-DD)
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
convertDate :: String -> String
convertDate date = 
    case break (== '-') date of
        (day, '-':rest) -> 
            case break (== '-') rest of
                (month, '-':year) -> year ++ "-" ++ month ++ "-" ++ day
                _ -> date
        _ -> date

main :: IO ()
main = do
    date <- getLine
    putStrLn $ convertDate date
