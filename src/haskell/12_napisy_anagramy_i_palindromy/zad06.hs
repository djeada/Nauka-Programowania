{-
ZAD-06 — Permutacje słowa, które są palindromami

\**Poziom:** ★★☆
\**Tagi:** `palindrom`, `permutacje`, `multiset`

### Treść

Wczytaj słowo i wypisz wszystkie **unikalne** palindromy, które są jego permutacjami.

### Wejście

\* 1. linia: słowo (litery mogą się powtarzać)

### Wyjście

Każdy unikalny palindrom w osobnej linii. Jeśli nie istnieje żaden — puste wyjście.

### Przykład

\**Wejście:**

```
aabb
```

\**Wyjście:**

```
abba
baab
```

### Uwagi

\* Najpierw sprawdź warunek istnienia palindromu z liter: co najwyżej jeden znak może mieć nieparzystą liczbę wystąpień.
\* Generuj palindromy z połówek (bez wypisywania duplikatów).

-}

import Data.List (group, sort, nub, permutations)

countChars :: String -> [(Char, Int)]
countChars s = [(head g, length g) | g <- group (sort s)]

canMakePalindrome :: [(Char, Int)] -> Bool
canMakePalindrome counts = length (filter (odd . snd) counts) <= 1

generatePalindromes :: String -> [String]
generatePalindromes s
    | not (canMakePalindrome counts) = []
    | otherwise = nub $ filter isPalindrome $ permutations s
    where
        counts = countChars s
        isPalindrome str = str == reverse str

main :: IO ()
main = do
    slowo <- getLine
    let palindromy = generatePalindromes slowo
    mapM_ putStrLn palindromy
