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

import Data.Char (isAlphaNum)

-- Podmień napisy z listy A na napisy z listy B
-- Złożoność czasowa: O(n*m*k) gdzie n to liczba słów, m to długość list, k to długość słowa
-- Złożoność pamięciowa: O(n)

-- Zamień słowa w tekście według map
replaceWords :: [(String, String)] -> String -> String
replaceWords replacements text = unwords $ map replaceWord (words (map wordBoundary text))
    where
        wordBoundary c = if isAlphaNum c then c else ' '
        replaceWord w = case lookup w replacements of
            Just replacement -> replacement
            Nothing -> w

main :: IO ()
main = do
    content <- getContents
    let allLines = lines content
        text = head allLines
        n = read (allLines !! 1) :: Int
        listA = take n (drop 2 allLines)
        listB = take n (drop (2 + n) allLines)
        replacements = zip listA listB
        result = replaceWords replacements text
    putStrLn result
