-- ZAD-07 — Zerowanie macierzy
--

-- ** Poziom:** ★★☆

-- ** Tagi:** `macierze`, `indeksy`

--
-- ### Treść
--
-- Wczytaj macierz `n×m`. Jeśli w macierzy występuje `0`, to **cały wiersz i cała kolumna** tego zera mają zostać ustawione na `0` (dla wszystkich zer naraz).
--
-- ### Wejście
--

-- * 1. linia: `n m`

-- * następnie `n` wierszy po `m` liczb

--
-- ### Wyjście
--

-- * `n` wierszy zmodyfikowanej macierzy

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 3 3
-- 1 2 3
-- 4 0 6
-- 7 8 9
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 1 0 3
-- 0 0 0
-- 7 0 9
-- ```
main :: IO ()
main = pure ()
