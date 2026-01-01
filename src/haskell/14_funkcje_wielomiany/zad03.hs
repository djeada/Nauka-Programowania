{-
ZAD-03 — Suma wielomianów

\**Poziom:** ★☆☆
\**Tagi:** `funkcje`, `wielomiany`, `listy`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` (mogą mieć różne stopnie) i zwraca współczynniki wielomianu będącego ich sumą.

### Wejście (argumenty funkcji)

\* `a` — lista `[a_n, ..., a_0]`
\* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

\* lista współczynników `a + b` w tej samej konwencji

### Przykład

Dla `a = [3, 5, 2]` i `b = [2, -8, 1]` funkcja zwraca:
`[5, -3, 3]`

### Uwagi

\* Jeśli listy mają różne długości, wyrównaj je od końca (od wyrazu wolnego).

-}

addPolynomials :: [Int] -> [Int] -> [Int]
addPolynomials a b = zipWith (+) a' b'
    where
        maxLen = max (length a) (length b)
        a' = replicate (maxLen - length a) 0 ++ a
        b' = replicate (maxLen - length b) 0 ++ b

main :: IO ()
main = do
    let a = [3, 5, 2]
    let b = [2, -8, 1]
    print $ addPolynomials a b
