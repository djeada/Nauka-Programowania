-- ZAD-04 — Dziedziczenie wielopoziomowe: Człowiek → Student → StudentFizyki
--

-- ** Poziom:** ★★☆

-- ** Tagi:** `dziedziczenie`, `konstruktory`, `super`

--
-- ### Treść
--
-- Zaprojektuj hierarchię klas:
--
-- 1. **Człowiek** — pola:
--
--    * imię
--    * nazwisko
--    * miejsce urodzenia
--    * zawód
--
-- 2. **Student** (dziedziczy po `Człowiek`) — dodatkowo:
--
--    * numer albumu
--    * kierunek studiów
--
-- 3. **StudentFizyki** (dziedziczy po `Student`) — dodatkowo:
--
--    * średnia z laboratoriów
--    * średnia z wykładów
--
-- Program:
--

-- * wczytuje dane dla trzech obiektów (Człowiek, Student, StudentFizyki),

-- * tworzy obiekty,

-- * wypisuje je w formacie jak w przykładzie.

--

-- ** Uwaga do wejścia:** wszystko w osobnych liniach, w podanej kolejności.

--
-- ### Wejście
--

-- ** Dane dla Człowiek:**

--
-- 1. imię
-- 2. nazwisko
-- 3. miejsce urodzenia
-- 4. zawód
--

-- ** Dane dla Student:**

-- 5. imię
-- 6. nazwisko
-- 7. miejsce urodzenia
-- 8. zawód
-- 9. numer albumu (int)
-- 10. kierunek studiów
--

-- ** Dane dla StudentFizyki:**

-- 11. imię
-- 12. nazwisko
-- 13. miejsce urodzenia
-- 14. zawód
-- 15. numer albumu (int)
-- 16. kierunek studiów
-- 17. średnia z laboratoriów (float)
-- 18. średnia z wykładów (float)
--
-- ### Wyjście
--
-- Trzy bloki jak w przykładzie, oddzielone pustą linią.
--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- Jan
-- Kowalski
-- Kraków
-- Inżynier
-- Anna
-- Nowak
-- Warszawa
-- Student
-- 12345
-- Informatyka
-- Piotr
-- Wiśniewski
-- Gdańsk
-- Student
-- 54321
-- Fizyka
-- 4.5
-- 4.0
-- ```
--

-- ** Wyjście:**

--
-- ```
-- Człowiek:
-- Imię: Jan
-- Nazwisko: Kowalski
-- Miejsce urodzenia: Kraków
-- Zawód: Inżynier
--
-- Student:
-- Imię: Anna
-- Nazwisko: Nowak
-- Miejsce urodzenia: Warszawa
-- Zawód: Student
-- Numer albumu: 12345
-- Kierunek studiów: Informatyka
--
-- Student Fizyki:
-- Imię: Piotr
-- Nazwisko: Wiśniewski
-- Miejsce urodzenia: Gdańsk
-- Zawód: Student
-- Numer albumu: 54321
-- Kierunek studiów: Fizyka
-- Średnia z laboratoriów: 4.5
-- Średnia z wykładów: 4.0
-- ```
main :: IO ()
main = pure ()
