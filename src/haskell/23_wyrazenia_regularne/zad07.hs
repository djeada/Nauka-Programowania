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

-- Usuwanie HTML tagów (uproszczona wersja)
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
removeHTMLTags :: String -> String
removeHTMLTags [] = []
removeHTMLTags ('<':rest) = removeHTMLTags (dropTag rest)
    where
        dropTag [] = []
        dropTag ('>':xs) = xs
        dropTag (_:xs) = dropTag xs
removeHTMLTags (c:rest) = c : removeHTMLTags rest

main :: IO ()
main = do
    html <- getLine
    putStrLn $ removeHTMLTags html
