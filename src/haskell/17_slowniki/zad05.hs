-- ZAD-05 — Pracownik z największym sumarycznym zyskiem
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `dict`, `sumowanie`

--
-- ### Treść
--
-- Wczytaj `n` wpisów: `pracownik zysk`. Zsumuj zyski per pracownik i wypisz nazwę pracownika z największą sumą.
-- (Jeśli remis, wybierz tego, który pierwszy osiągnął tę maksymalną sumę podczas przetwarzania.)
--
-- ### Wejście
--

-- * 1 linia: `n`

-- * następnie `n` linii: `imie_i_nazwisko zysk`

--
-- ### Wyjście
--

-- * Jedna linia: `imie_i_nazwisko`

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 5
-- Barnaba_Barabash 120
-- Jon_Snow 100
-- Kira_Summer 300
-- Barnaba_Barabash 200
-- Bob_Marley 110
-- ```
--

-- ** Wyjście:**

--
-- ```
-- Barnaba_Barabash
-- ```
main :: IO ()
main = pure ()
