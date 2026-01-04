{-
ZAD-05 — k-ta pochodna wielomianu

\**Poziom:** ★★☆
\**Tagi:** `funkcje`, `pochodna`, `wielomiany`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę naturalną `k` i zwraca współczynniki wielomianu będącego **k-tą pochodną**.

### Wejście (argumenty funkcji)

\* `a` — lista `[a_n, ..., a_0]`
\* `k` — liczba naturalna

### Wyjście (zwracana wartość)

\* lista współczynników wielomianu po zróżniczkowaniu `k` razy

### Przykład

Dla `a = [4, -3, 2]` oraz `k = 1` funkcja zwraca:
`[8, -3]`

### Uwagi

\* Jeśli `k` jest większe niż stopień wielomianu, wynikiem jest wielomian zerowy: `[0]`.

-}

kthDerivative :: [Int] -> Int -> [Int]
kthDerivative coeffs 0 = coeffs
kthDerivative [] _ = [0]
kthDerivative coeffs k
  | k < 0 = coeffs
  | k >= length coeffs = [0]
  | otherwise = kthDerivative (derivative coeffs) (k - 1)
  where
    derivative [] = []
    derivative [_] = [0]
    derivative cs = zipWith (*) [length cs - 1, length cs - 2 .. 1] (init cs)

main :: IO ()
main = do
  let coeffs = [4, -3, 2]
  let k = 1
  print $ kthDerivative coeffs k
