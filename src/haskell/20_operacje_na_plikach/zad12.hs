-- ZAD-12 — Przenieś wszystkie pliki CSV do jednego folderu (rekurencyjnie)
--

-- ** Poziom:** ★★☆

-- ** Tagi:** `files`, `move`, `csv`, `recursive`

--
-- ### Treść
--
-- Otrzymujesz ścieżkę folderu źródłowego i docelowego. Przenieś wszystkie pliki `.csv` z folderu źródłowego **i wszystkich jego podfolderów** do folderu docelowego.
--
-- ### Wejście
--

-- * 1 linia: `src_folder`

-- * 2 linia: `dst_folder`

--
-- ### Wyjście
--
-- Brak.
--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- C:\Users\Username\Projekty
-- D:\Dane\CSV
-- ```
--

-- ** Wyjście:**

-- * (brak)*

--
-- ### Uwagi
--

-- * Jeśli w folderze docelowym istnieje już plik o tej samej nazwie, zadanie wymaga zdefiniowania zachowania (np. zmiana nazwy / pominięcie) — jeśli sprawdzarka tego nie doprecyzowuje, przyjmij jedną spójną strategię w całym rozwiązaniu.

main :: IO ()
main = pure ()
