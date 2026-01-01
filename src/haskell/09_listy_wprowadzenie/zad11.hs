{-
ZAD-11 — Samochody jadące w przeciwnych kierunkach

\**Poziom:** ★★☆
\**Tagi:** `listy`, `zliczanie`, `string`

### Treść

Wczytaj `N` oraz napis długości `N` złożony z liter `A` i `B`:

\* `A` oznacza samochód jadący na wschód,
\* `B` oznacza samochód jadący na zachód.

Policz, ile par samochodów minie się, gdy uznamy, że para mija się wtedy, gdy `A` stoi **przed** `B` w ciągu.

### Wejście

\* 1. linia: `N` (`N ≥ 1`)
\* 2. linia: napis długości `N`, tylko `A` i `B` (bez spacji)

### Wyjście

Jedna liczba naturalna — liczba mijających się par.

### Przykład

\**Wejście:**

```
5
ABABB
```

\**Wyjście:**

```
5
```

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  str <- getLine
  
  let countPairs = go 0 0 str
        where
          go count aCount [] = count
          go count aCount (c:cs)
            | c == 'A' = go count (aCount + 1) cs
            | c == 'B' = go (count + aCount) aCount cs
            | otherwise = go count aCount cs
  
  print countPairs
