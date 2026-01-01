{-
ZAD-10 — Podmień napisy z listy A na napisy z listy B

\**Poziom:** ★★☆
\**Tagi:** `regex`, `string`, `zamiana`

### Treść

Otrzymujesz:

\* tekst,
\* listę A (napisy do znalezienia),
\* listę B (napisy do podmiany), tej samej długości co A.

Zastąp w tekście wszystkie wystąpienia słów z listy A odpowiadającymi im słowami z listy B (ten sam indeks). Zamieniaj tylko **całe słowa**, nie fragmenty innych słów.

### Wejście

1. Tekst (jedna lub wiele linii)
2. Liczba naturalna `n` — długość list
3. `n` wierszy: elementy listy A
4. `n` wierszy: elementy listy B

### Wyjście

Zmodyfikowany tekst.

### Przykład

\*(jak w treści — z listami A/B)*

-}

-- Zamiana tekstu (zastępowanie wzorca)
-- Złożoność czasowa: O(n*m), gdzie n to długość tekstu, m to długość wzorca
-- Złożoność pamięciowa: O(n)
replaceText :: String -> String -> String -> String
replaceText _ _ [] = []
replaceText pattern replacement text
    | pattern `isPrefixOf` text = replacement ++ replaceText pattern replacement (drop (length pattern) text)
    | otherwise = head text : replaceText pattern replacement (tail text)
    where
        isPrefixOf [] _ = True
        isPrefixOf _ [] = False
        isPrefixOf (x:xs) (y:ys) = x == y && isPrefixOf xs ys

main :: IO ()
main = do
    pattern <- getLine
    replacement <- getLine
    text <- getLine
    putStrLn $ replaceText pattern replacement text
