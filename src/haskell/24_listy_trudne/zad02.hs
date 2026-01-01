-- ZAD-02 — Przesuń zera na koniec listy
--

-- ** Poziom:** ★★☆

-- ** Tagi:** `list`, `stabilność`, `przekształcenie`

--
-- ### Treść
--
-- Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, **zachowując kolejność** pozostałych elementów.
--
-- ### Wejście
--

-- * 1 linia: lista liczb całkowitych `A`

--
-- ### Wyjście
--

-- * 1 linia: lista po przekształceniu

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
-- ```
--

-- ** Wyjście:**

--
-- ```
-- [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]
-- ```
main :: IO ()
main = pure ()
