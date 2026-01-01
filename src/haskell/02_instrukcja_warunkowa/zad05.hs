{-
ZAD-05 — Sortowanie trzech liczb

\**Poziom:** ★★☆
\**Tagi:** `sort`, `warunki`, `porządkowanie`

### Treść

Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności rosnącej.

### Wejście

\* 1 linia: `a` (całkowita, `a ≥ 0`)
\* 2 linia: `b` (całkowita, `b ≥ 0`)
\* 3 linia: `c` (całkowita, `c ≥ 0`)

### Wyjście

Jedna linia: trzy liczby rosnąco, oddzielone pojedynczymi spacjami.

### Przykład

\**Wejście:**

```
2
1
4
```

\**Wyjście:**

```
1 2 4
```

### Uwagi

\* Możesz użyć wbudowanego sortowania, ale da się też rozwiązać czystymi warunkami.

-}
import Data.List (sort)

main :: IO ()
main = do
  aInput <- getLine
  bInput <- getLine
  cInput <- getLine
  let a = read aInput :: Int
  let b = read bInput :: Int
  let c = read cInput :: Int
  let sorted = sort [a, b, c]
  putStrLn $ unwords (map show sorted)
