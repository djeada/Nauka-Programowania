{-
ZAD-13 — Brakujący element w ciągu arytmetycznym

\**Poziom:** ★★☆
\**Tagi:** `sortowanie`, `ciąg arytmetyczny`, `listy`

### Treść

Wczytaj `N` liczb naturalnych. Lista jest fragmentem ciągu arytmetycznego z **jednym brakującym elementem**. Znajdź i wypisz brakującą wartość.

### Wejście

\* 1. linia: `N` (`N ≥ 2`)
\* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — brakujący element.

### Przykład

\**Wejście:**

```
4
5
2
1
3
```

\**Wyjście:**

```
4
```

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1..n]
  
  let sorted = sort nums
  let diff = if length sorted >= 2 then sorted !! 1 - sorted !! 0 else 0
  let expected = [sorted !! 0, sorted !! 0 + diff .. sorted !! 0 + diff * n]
  let missing = head [x | x <- expected, x `notElem` nums]
  
  print missing
  where
    sort [] = []
    sort (x:xs) = sort smaller ++ [x] ++ sort larger
      where
        smaller = [a | a <- xs, a <= x]
        larger = [a | a <- xs, a > x]
