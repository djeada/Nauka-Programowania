-- ZAD-01 — Wypisywanie tekstu na ekran
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `I/O`, `print`, `string`

--
-- ### Treść
--
-- Napisz program, który wypisze dokładnie:
-- `Witaj, świecie!`
--
-- ### Wejście
--
-- Brak.
--
-- ### Wyjście
--
-- Jedna linia:
--

-- * `Witaj, świecie!`

--
-- ### Przykład
--

-- ** Wyjście:**

--
-- ```
-- Witaj, świecie!
-- ```
--
-- ### Uwagi o formatowaniu
--

-- * Tekst musi być identyczny (łącznie z przecinkiem, spacją i wykrzyknikiem).

{-
Tytul: Wypisywanie na standardowe wyjscie.

Tresc zadania: Napisz program, ktory wypisze dowolny ciag znakow na standardowe wyjscie.

Dane wejsciowe: Brak.

Dane wyjsciowe: Komunikat.

Przyklad:

Program moze wypisac twoje inicjaly lub komunikat "Witaj swiecie!".
-}

main :: IO ()
main = putStrLn "Witaj swiecie!"
