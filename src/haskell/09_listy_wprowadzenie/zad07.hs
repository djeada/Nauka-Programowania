{-
ZAD-07 — Średnia dwóch największych liczb

\**Poziom:** ★☆☆
\**Tagi:** `listy`, `max`, `sortowanie`, `float`

### Treść

Wczytaj `N` liczb naturalnych (`N ≥ 2`). Znajdź największą i drugą największą wartość, a następnie wypisz ich średnią arytmetyczną jako liczbę zmiennoprzecinkową z dokładnością do **jednego** miejsca po przecinku.

### Wejście

\* 1. linia: `N` (`N ≥ 2`)
\* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba zmiennoprzecinkowa w formacie `%.1f`.

### Przykład

\**Wejście:**

```
6
9
2
3
2
1
7
```

\**Wyjście:**

```
8.0
```

-}
import Text.Printf

main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1..n]
  
  let sorted = reverse $ take 2 $ reverse $ map fromIntegral $ sort nums :: [Double]
  let avg = sum sorted / 2
  
  printf "%.1f\n" avg
  where
    sort [] = []
    sort (x:xs) = sort smaller ++ [x] ++ sort larger
      where
        smaller = [a | a <- xs, a <= x]
        larger = [a | a <- xs, a > x]
