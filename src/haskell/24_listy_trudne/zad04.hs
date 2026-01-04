{-
ZAD-04 — Wspólny podciąg o największej długości (równe sumy)

\**Poziom:** ★★★
\**Tagi:** `list`, `prefix`, `hashmap`, `podciąg`

### Treść

Otrzymujesz dwie listy binarne `A` i `B` (zera i jedynki) o tej samej długości. Znajdź **maksymalną długość** podciągu (ciągłych elementów), dla którego suma elementów w podciągu z `A` jest równa sumie elementów w odpowiadającym podciągu z `B` (ten sam zakres indeksów).

### Wejście

\* 1 linia: lista binarna `A`
\* 2 linia: lista binarna `B` (tej samej długości)

### Wyjście

\* 1 linia: maksymalna długość (liczba naturalna)

### Przykład

\**Wejście:**

```
[0, 0, 1, 1, 1, 1]
[0, 1, 1, 0, 1, 0]
```

\**Wyjście:**

```
5
```

-}
import Text.Read (readMaybe)

-- Wspólny podciąg o największej długości (równe sumy)
-- Złożoność czasowa: O(n^2)
-- Złożoność pamięciowa: O(1)
maxLengthEqualSum :: [Int] -> [Int] -> Int
maxLengthEqualSum a b = maximum [len | i <- [0 .. length a - 1], j <- [i .. length a - 1], let len = j - i + 1, sum (take len (drop i a)) == sum (take len (drop i b))]

main :: IO ()
main = do
  inputA <- getLine
  inputB <- getLine
  case (readMaybe inputA :: Maybe [Int], readMaybe inputB :: Maybe [Int]) of
    (Just a, Just b) -> print $ maxLengthEqualSum a b
    _ -> print (0 :: Int)
