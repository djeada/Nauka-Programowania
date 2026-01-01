-- ZAD-04 — Podstawowe operacje arytmetyczne
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `arytmetyka`, `I/O`

--
-- ### Treść
--
-- Wczytaj dwie liczby naturalne `a` i `b` i wypisz kolejno:
--
-- 1. `a + b`
-- 2. `a - b`
-- 3. `a * b`
-- 4. `a // b` (dzielenie całkowite)
-- 5. `a % b`
-- 6. `a^b`
--
-- ### Wejście
--

-- * 1. linia: `a` (liczba całkowita)

-- * 2. linia: `b` (liczba całkowita)

--
-- ### Wyjście
--
-- 6 linii — wyniki działań w kolejności 1–6.
--
-- ### Ograniczenia / gwarancje
--

-- * `a ≥ 0`

-- * `b > 0` (żeby dzielenie i modulo były poprawne)

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 3
-- 2
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 5
-- 1
-- 6
-- 1
-- 1
-- 9
-- ```
{-
Tytul: Obliczanie wynikow operacji arytmetycznych.

Tresc zadania: Napisz program, ktory pobierze od uzytkownika dwie liczby naturalne i wypisze wyniki nastepujacych operacji arytmetycznych:

a) suma tych liczb

b) roznica pierwszej i drugiej liczby

c) iloczyn tych liczb

d) iloraz pierwszej liczby przez druga

e) reszta z dzielenia pierwszej liczby przez druga

f) pierwsza liczba podniesiona do potegi rownej drugiej liczbie

Dane wejsciowe: Dwie liczby naturalne dla wszystkich podpunktow.

Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.

Przyklad:

    Jesli uzytkownik poda liczby 9 oraz 1, program powinien wypisac liczby: 10, 1, 9, 9, 0, 9.
    Jesli uzytkownik poda liczby 3 oraz 2, program powinien wypisac liczby: 5, 1, 6, 1, 1, 9.
-}

main :: IO ()
main = do
  putStrLn "Podaj pierwsza liczbe:"
  a <- readLn :: IO Int
  putStrLn "Podaj druga liczbe:"
  b <- readLn :: IO Int
  let wyniki = (a + b, a - b, a * b, a `div` b, a `mod` b, a ^ b)
  putStrLn $ "Wyniki operacji arytmetycznych: " ++ show wyniki
