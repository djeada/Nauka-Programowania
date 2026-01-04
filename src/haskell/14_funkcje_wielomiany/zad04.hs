{-
ZAD-04 — Mnożenie wielomianów

\**Poziom:** ★★☆
\**Tagi:** `funkcje`, `wielomiany`, `konwolucja`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` i zwraca listę współczynników wielomianu będącego ich iloczynem.

### Wejście (argumenty funkcji)

\* `a` — lista `[a_n, ..., a_0]`
\* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

\* lista współczynników wielomianu `a * b` (długość `len(a)+len(b)-1`)

### Przykład

Dla `a = [5, 0, 10, 6]` oraz `b = [1, 2, 4]` funkcja zwraca:
`[5, 10, 30, 26, 52, 24]`

-}

multiplyPolynomials :: [Int] -> [Int] -> [Int]
multiplyPolynomials a b =
  [ sum
      [ a !! i * b !! j | i <- [0 .. length a - 1], j <- [0 .. length b - 1], i + j == k
      ]
    | k <- [0 .. length a + length b - 2]
  ]

main :: IO ()
main = do
  let a = [5, 0, 10, 6]
  let b = [1, 2, 4]
  print $ multiplyPolynomials a b
