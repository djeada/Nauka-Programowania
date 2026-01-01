-- ZAD-05 — k-ta pochodna wielomianu
--

-- ** Poziom:** ★★☆

-- ** Tagi:** `funkcje`, `pochodna`, `wielomiany`

--
-- ### Treść
--
-- Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę naturalną `k` i zwraca współczynniki wielomianu będącego **k-tą pochodną**.
--
-- ### Wejście (argumenty funkcji)
--

-- * `a` — lista `[a_n, ..., a_0]`

-- * `k` — liczba naturalna

--
-- ### Wyjście (zwracana wartość)
--

-- * lista współczynników wielomianu po zróżniczkowaniu `k` razy

--
-- ### Przykład
--
-- Dla `a = [4, -3, 2]` oraz `k = 1` funkcja zwraca:
-- `[8, -3]`
--
-- ### Uwagi
--

-- * Jeśli `k` jest większe niż stopień wielomianu, wynikiem jest wielomian zerowy: `[0]`.

main :: IO ()
main = pure ()
