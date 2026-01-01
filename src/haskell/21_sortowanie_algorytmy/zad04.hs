-- ZAD-04 — Sortowanie przez scalanie
--

-- ** Poziom:** ★★☆

-- ** Tagi:** `sorting`, `merge-sort`, `recursion`

--
-- ### Treść
--
-- Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez scalanie**:
--
-- 1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
-- 2. Podziel listę na dwie (w miarę) równe części.
-- 3. Rekurencyjnie posortuj obie części.
-- 4. **Scal** dwie posortowane listy w jedną posortowaną.
--
-- ### Wejście
--

-- * 1 linia: lista liczb całkowitych

--
-- ### Wyjście
--

-- * 1 linia: posortowana lista rosnąco

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- [6, 2, 1, 4, 27]
-- ```
--

-- ** Wyjście:**

--
-- ```
-- [1, 2, 4, 6, 27]
-- ```
--
-- ### Uwagi o algorytmie
--

-- * Złożoność czasowa: `O(n log n)`.

main :: IO ()
main = pure ()
