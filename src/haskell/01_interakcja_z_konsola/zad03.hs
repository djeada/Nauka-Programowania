-- ZAD-03 — Rysowanie kształtów znakami
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `print`, `formatowanie`, `pętle`, `string`

--
-- ### Treść
--
-- Wypisz na wyjście trzy kształty:
--
-- 1. **Kwadrat 2×2** z liter `x`
-- 2. **Trójkąt liczbowy** z 3 linii: w linii `i` wypisz `i` razy cyfrę `i` (dla i=1..3)
-- 3. **Romb z jedynek** o maksymalnej szerokości 5 znaków
--
-- Każdy kształt ma być oddzielony **jedną pustą linią**.
--
-- ### Wejście
--
-- Brak.
--
-- ### Wyjście
--
-- Dokładnie:
--

-- * 2 linie kwadratu,

-- * pusta linia,

-- * 3 linie trójkąta,

-- * pusta linia,

-- * 5 linii rombu.

--
-- ### Przykład (oczekiwane wyjście)
--
-- ```
-- xx
-- xx
--
-- 1
-- 22
-- 333
--
--   1
--  111
-- 11111
--  111
--   1
-- ```
--
-- ### Uwagi o formatowaniu
--

-- * W rombie spacje na początku linii są istotne.

-- * Nie dodawaj dodatkowych pustych linii na początku; jedna na końcu jest zwykle akceptowalna, ale trzymaj się przykładu.

{-
Tytul: Rysowanie ksztaltow za pomoca znakow.

Tresc zadania: Napisz program, ktory wypisze na standardowe wyjscie ciagi znakow tworzace kwadrat, trojkat oraz romb z jedynek. Pamietaj o dodawaniu odpowiednich spacji i przejsciach do nowej linii.

Przyklady:

Kwadrat:

xx
xx

Trojkat:

1
22
333

Romb z jedynek:

1
111
11111
111
1

Dane wejsciowe: Brak.

Dane wyjsciowe: Komunikat.
-}

main :: IO ()
main = do
  putStrLn "Kwadrat:"
  putStrLn "xx"
  putStrLn "xx"

  putStrLn "\nTrojkat:"
  putStrLn " 1"
  putStrLn "22"
  putStrLn "333"

  putStrLn "\nRomb z jedynek:"
  putStrLn "  1"
  putStrLn " 111"
  putStrLn "11111"
  putStrLn " 111"
  putStrLn "  1"
