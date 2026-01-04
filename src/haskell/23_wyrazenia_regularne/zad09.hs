{-
ZAD-09 — Usuń fragment napisu od pierwszego wystąpienia słowa klucz

\**Poziom:** ★★☆
\**Tagi:** `regex`, `string`

### Treść

Otrzymujesz tekst (wiele zdań lub wierszy) oraz słowo klucz. Jeśli słowo klucz wystąpi w tekście, usuń całą część od **pierwszego wystąpienia** tego słowa do końca tekstu. Jeśli słowo klucz nie występuje, wypisz tekst bez zmian.

### Wejście

Dwie części:

1. Tekst (może mieć wiele wierszy)
2. W osobnej linii: `klucz`

### Wyjście

Zmodyfikowany tekst.

### Przykład

\*(jak w treści zadania — długi tekst)*

-}

import Data.List (isPrefixOf)

-- Usuń fragment napisu od pierwszego wystąpienia słowa klucz
-- Złożoność czasowa: O(n*m) gdzie n to długość tekstu, m to długość klucza
-- Złożoność pamięciowa: O(n)

-- Znajdź pozycję pierwszego wystąpienia wzorca w tekście
findPattern :: String -> String -> Maybe Int
findPattern pattern text = findAt 0 text
  where
    findAt _ [] = Nothing
    findAt pos str
      | pattern `isPrefixOf` str = Just pos
      | otherwise = case str of
          [] -> Nothing
          (_ : rest) -> findAt (pos + 1) rest

-- Usuń od pierwszego wystąpienia klucza do końca
removeFromKeyword :: String -> String -> String
removeFromKeyword keyword text =
  case findPattern keyword text of
    Nothing -> text
    Just pos -> take pos text

main :: IO ()
main = do
  content <- getContents
  let allLines = lines content
      keyword = last allLines
      textLines = init allLines
      text = unlines textLines
      -- Remove the trailing newline that unlines adds
      textWithoutTrailingNewline = if null text then "" else init text
      result = removeFromKeyword keyword textWithoutTrailingNewline
  putStr result
