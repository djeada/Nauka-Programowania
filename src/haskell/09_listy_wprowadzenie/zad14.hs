{-
ZAD-14 — Element bez pary

\**Poziom:** ★★☆
\**Tagi:** `XOR`, `listy`, `zliczanie`

### Treść

Wczytaj listę liczb całkowitych o nieparzystej długości: wszystkie liczby poza jedną występują dokładnie dwa razy. Znajdź liczbę bez pary.

### Wejście

\* 1. linia: `N` (nieparzyste, `N ≥ 1`)
\* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna liczba całkowita — element bez pary.

### Przykład

\**Wejście:**

```
7
1
3
1
7
3
1
1
```

\**Wyjście:**

```
7
```

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1..n]
  
  -- Znajdź element, który występuje tylko raz
  let findSingle [] = 0
      findSingle [x] = x
      findSingle (x:xs) = if count x nums == 1 then x else findSingle xs
      count x = length . filter (== x)
  
  print $ findSingle nums
