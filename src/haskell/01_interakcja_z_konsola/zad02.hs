-- ZAD-02 — Zamiana kolejności liczb
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `I/O`, `zmienne`

--
-- ### Treść
--
-- Wczytaj dwie liczby całkowite i wypisz je w odwrotnej kolejności (każda w osobnej linii).
--
-- ### Wejście
--
-- Dwie liczby całkowite:
--

-- * 1. linia: `a`

-- * 2. linia: `b`

--
-- ### Wyjście
--
-- Dwie linie:
--

-- * 1. linia: `b`

-- * 2. linia: `a`

--
-- ### Ograniczenia / gwarancje
--

-- * `a`, `b` mieszczą się w typowym zakresie int (np. 32-bit).

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- -7
-- 4
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 4
-- -7
-- ```
{-
Tytul: Zamiana kolejnosci liczb.

Tresc zadania: Napisz program, ktory pobierze od uzytkownika dwie liczby naturalne i wypisze je w odwroconej kolejnosci.

Dane wejsciowe: Dwie liczby naturalne.

Dane wyjsciowe: Dwie liczby naturalne.

Przyklad:

Jesli uzytkownik poda liczby -7 oraz 4, program powinien wypisac liczby: 4 i -7.
-}

main :: IO ()
main = do
  putStrLn "Podaj pierwsza liczbe:"
  a <- readLn :: IO Int
  putStrLn "Podaj druga liczbe:"
  b <- readLn :: IO Int
  putStrLn $ "Liczby w odwrotnej kolejnosci: " ++ show b ++ " " ++ show a
