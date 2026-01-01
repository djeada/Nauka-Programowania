-- ZAD-17 — Wszystkie pary o sumie x (wartości)
--

-- ** Poziom:** ★★☆

-- ** Tagi:** `listy`, `2-sum`, `pary`

--
-- ### Treść
--
-- Wczytaj listę liczb całkowitych oraz `x`. Wypisz wszystkie pary **wartości** `(a, b)` z listy (nie indeksy), takie że `a + b == x`. Każdą parę wypisz w osobnej linii jako:
-- `a b`
--
-- Każdą parę wypisz tylko raz (nie dubluj `(a,b)` i `(b,a)`).
--
-- ### Wejście
--

-- * 1. linia: `N` (`N ≥ 2`)

-- * kolejne `N` linii: liczby całkowite

-- * ostatnia linia: `x` (liczba całkowita)

--
-- ### Wyjście
--
-- Wiele linii — po jednej parze na linię.
-- Jeśli brak par — brak wyjścia.
--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 5
-- 1
-- 2
-- 4
-- 3
-- 7
-- 5
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 1 4
-- 2 3
-- ```
main :: IO ()
main = pure ()
