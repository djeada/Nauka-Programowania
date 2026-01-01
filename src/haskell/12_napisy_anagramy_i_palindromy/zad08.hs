{-
ZAD-08 — Wyjątkowe palindromy (podciągi bez zmiany kolejności)

\**Poziom:** ★★★
\**Tagi:** `substring`, `palindrom`, `unikalność`

### Treść

Wczytaj słowo i znajdź wszystkie **unikalne** palindromy, które można z niego utworzyć jako **spójne podciągi** (substringi), bez zmiany kolejności znaków, spełniające warunek „wyjątkowości”:

1. wszystkie znaki są identyczne (np. `aaa`), **albo**
2. wszystkie znaki poza środkowym są identyczne (np. `cbc`).

Pojedynczy znak też jest wyjątkowym palindromem.

### Wejście

\* 1. linia: słowo (litery)

### Wyjście

Każdy unikalny wyjątkowy palindrom w osobnej linii.
Jeśli nic poza pojedynczymi znakami nie pasuje, wypisz tylko te unikalne znaki (po jednej linii na znak).

### Przykład

\**Wejście:**

```
xxyxx
```

\**Wyjście:**

```
x
xx
xxx
xxyxx
y
yxy
```

### Uwagi o formatowaniu

\* Usuń duplikaty w wyniku (np. ten sam palindrom znaleziony w kilku miejscach wypisz raz).
\* Kolejność wypisywania może być zgodna z pierwszym pojawieniem się w tekście (łatwe i czytelne): wypisuj przy pierwszym znalezieniu danego palindromu.

-}

import Data.Set (Set)
import qualified Data.Set as Set

substrings :: String -> [String]
substrings s = [take len (drop i s) | i <- [0..length s - 1], len <- [1..length s - i]]

isExceptionalPalindrome :: String -> Bool
isExceptionalPalindrome s
    | s /= reverse s = False
    | length s == 1 = True
    | length s == 2 = s !! 0 == s !! 1
    | otherwise = allSame s || allSameExceptMiddle s
    where
        allSame str = null str || all (== head str) str
        allSameExceptMiddle str = 
            let mid = length str `div` 2
                beforeMid = take mid str
                afterMid = drop (mid + 1) str
            in (not (null beforeMid)) && allSame beforeMid && allSame afterMid && 
               head beforeMid == head afterMid

main :: IO ()
main = do
    slowo <- getLine
    let subs = substrings slowo
    let seen = Set.empty :: Set String
    let (palindromy, _) = foldl (\(acc, s) sub -> 
            if isExceptionalPalindrome sub && not (Set.member sub s)
            then (acc ++ [sub], Set.insert sub s)
            else (acc, s)) ([], seen) subs
    mapM_ putStrLn palindromy
