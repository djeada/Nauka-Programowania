{-
ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

\**Poziom:** ★★☆
\**Tagi:** `delta`, `pierwiastki`, `I/O`

### Treść

Wczytaj współczynniki równania kwadratowego ( ax^2 + bx + c = 0 ). Wypisz wszystkie **rzeczywiste** miejsca zerowe w kolejności rosnącej.

### Wejście

\* 1. linia: trzy liczby całkowite: `a b c` (oddzielone spacją)

### Wyjście

\* Jeśli brak rzeczywistych pierwiastków: wypisz `[]`
\* Jeśli jeden pierwiastek (delta = 0): wypisz go raz w formacie listy: `[x]`
\* Jeśli dwa pierwiastki: wypisz w formacie listy: `[x1, x2]` gdzie `x1 ≤ x2`

\**Format liczb:**

\* wypisuj jako liczby zmiennoprzecinkowe (np. `-1.0`, `2.5`)

### Przykład

\**Wejście:**

```
1 2 1
```

\**Wyjście:**

```
[-1.0]
```

### Uwagi o formatowaniu

\* Licz deltę: `Δ = b*b - 4*a*c`.
\* Dla `Δ > 0`: policz oba pierwiastki i posortuj rosnąco.
\* Zakładamy `a ≠ 0`.

-}

import Data.List (sort)

-- Znajduje rzeczywiste miejsca zerowe równania kwadratowego
-- Złożoność czasowa: O(1)
-- Złożoność pamięciowa: O(1)
quadraticRoots :: Double -> Double -> Double -> [Double]
quadraticRoots a b c =
  let delta = b * b - 4 * a * c
   in if delta < 0
        then []
        else
          if delta == 0
            then [-b / (2 * a)]
            else
              let sqrtDelta = sqrt delta
                  x1 = (-b + sqrtDelta) / (2 * a)
                  x2 = (-b - sqrtDelta) / (2 * a)
               in sort [x1, x2]

-- Formatuje listę pierwiastków
formatRoots :: [Double] -> String
formatRoots [] = "[]"
formatRoots [x] = "[" ++ show x ++ "]"
formatRoots xs = "[" ++ concatMap (\(i, x) -> if i == 0 then show x else ", " ++ show x) (zip [0 ..] xs) ++ "]"

-- Miejsca zerowe równania kwadratowego (z I/O)
main :: IO ()
main = do
  line <- getLine
  let [a, b, c] = map (read :: String -> Double) $ words line
  putStrLn $ formatRoots $ quadraticRoots a b c
