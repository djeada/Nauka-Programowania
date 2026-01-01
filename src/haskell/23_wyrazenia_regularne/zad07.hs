{-
ZAD-07 — Podziel tekst względem znaków interpunkcyjnych

\**Poziom:** ★☆☆
\**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis (jedno lub kilka zdań). Podziel tekst na fragmenty w miejscach występowania znaków interpunkcyjnych (np. `, . ! ? ; :`). Usuń spacje na początku i końcu każdego fragmentu.

### Wejście

Jedna linia:

\* `tekst`

### Wyjście

Każdy fragment w osobnej linii.

### Przykład

\**Wejście:**

```
Ani nie poszedł do kina, ani nie wybrał się do teatru.
```

\**Wyjście:**

```
Ani nie poszedł do kina
ani nie wybrał się do teatru
```

-}

-- Podziel tekst względem znaków interpunkcyjnych
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)

-- Sprawdź czy znak jest interpunkcyjny
isPunctuation :: Char -> Bool
isPunctuation c = c `elem` ",.!?;:"

-- Podziel tekst według interpunkcji i usuń białe znaki z brzegów
splitByPunctuation :: String -> [String]
splitByPunctuation text = filter (not . null) $ map trim $ split text
    where
        split [] = [""]
        split (c:cs)
            | isPunctuation c = "" : split cs
            | otherwise = case split cs of
                (x:xs) -> (c:x):xs
                [] -> [[c]]
        
        trim = dropWhile (== ' ') . reverse . dropWhile (== ' ') . reverse

main :: IO ()
main = do
    text <- getLine
    mapM_ putStrLn $ splitByPunctuation text
