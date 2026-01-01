{-
ZAD-01 — Wartość wielomianu w punkcie

\**Poziom:** ★☆☆
\**Tagi:** `funkcje`, `wielomiany`, `Horner`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `x`, a następnie zwraca wartość wielomianu w punkcie `x`.

### Wejście (argumenty funkcji)

\* `a` — lista współczynników `[a_n, ..., a_0]`
\* `x` — liczba naturalna (lub całkowita)

### Wyjście (zwracana wartość)

\* jedna liczba (całkowita)

### Przykład

Dla `a = [3, 2, 1]` i `x = 1` funkcja zwraca:
`6`

### Uwagi

\* Najprościej użyć schematu Hornera.

-}

-- Oblicza wartość wielomianu w punkcie x używając schematu Hornera
evaluatePolynomial :: [Int] -> Int -> Int
evaluatePolynomial [] _ = 0
evaluatePolynomial coeffs x = foldl (\acc c -> acc * x + c) 0 coeffs

main :: IO ()
main = do
    let coeffs = [3, 2, 1]
    let x = 1
    print $ evaluatePolynomial coeffs x
