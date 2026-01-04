{-
ZAD-13 — Znaki na indeksach będących liczbami pierwszymi

\**Poziom:** ★☆☆
\**Tagi:** `liczby pierwsze`, `indeksy`, `string`

### Treść

Wczytaj napis. Zbierz znaki, których **indeksy (od 0)** są liczbami pierwszymi (2, 3, 5, 7, ...). Wypisz wynik jako listę w stylu Pythona.

### Wejście

\* 1. linia: napis

### Wyjście

\* 1. linia: lista znaków, np. `['o', 'ń']`

### Przykład

\**Wejście:**

```
Słoń
```

\**Wyjście:**

```
['o', 'ń']
```

### Uwagi

\* Indeksy: `S(0) ł(1) o(2) ń(3)` → bierz 2 i 3.

-}

czyPierwsza :: Int -> Bool
czyPierwsza n
  | n < 2 = False
  | n == 2 = True
  | even n = False
  | otherwise = not $ any (\x -> n `mod` x == 0) [3, 5 .. floor (sqrt (fromIntegral n))]

-- Pobiera znaki z indeksów będących liczbami pierwszymi
-- Złożoność czasowa: O(n * sqrt(n)), gdzie n to długość napisu
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  napis <- getLine
  let znaki = [napis !! i | (i, _) <- zip [0 ..] napis, czyPierwsza i]
  putStrLn $ "[" ++ concat [if i == 0 then "'" ++ [c] ++ "'" else ", '" ++ [c] ++ "'" | (c, i) <- zip znaki [0 ..]] ++ "]"
