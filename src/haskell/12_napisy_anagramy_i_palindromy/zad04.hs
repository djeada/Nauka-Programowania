{-
ZAD-04 — Palindromy w zdaniu

\**Poziom:** ★★☆
\**Tagi:** `string`, `tokenizacja`, `palindrom`

### Treść

Wczytaj zdanie i wypisz wszystkie słowa, które są palindromami.
Ignoruj wielkość liter przy sprawdzaniu.

### Wejście

\* 1. linia: zdanie (może zawierać spacje i znaki interpunkcyjne)

### Wyjście

Każdy znaleziony palindrom w osobnej linii, w kolejności występowania w zdaniu.

### Przykład

\**Wejście:**

```
Tata zabrał kajak na wycieczkę i uderzył się w oko
```

\**Wyjście:**

```
Tata
kajak
i
w
oko
```

### Uwagi o formatowaniu

\* Traktuj „słowo” jako ciąg liter/cyfr po usunięciu interpunkcji z brzegów (np. `kara.` → `kara`).
\* Porównuj w wersji `lower()`, ale wypisz w oryginalnym brzmieniu z wejścia (tak jak w przykładzie).

-}

import Data.Char (isPunctuation, toLower)

-- Usuwa interpunkcję z brzegów słowa
stripPunctuation :: String -> String
stripPunctuation = reverse . dropWhile isPunctuation . reverse . dropWhile isPunctuation

-- Sprawdza czy słowo jest palindromem
isPalindrome :: String -> Bool
isPalindrome s = s_lower == reverse s_lower
  where
    s_lower = map toLower s

-- Znajduje wszystkie palindromy w zdaniu
main :: IO ()
main = do
  zdanie <- getLine
  let slowa = map stripPunctuation $ words zdanie
  let palindromy = filter (\w -> not (null w) && isPalindrome w) slowa
  mapM_ putStrLn palindromy
