-- ZAD-06A — Kilogramy → gramy
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `konwersje`

--
-- ### Treść
--
-- Wczytaj wartość w kilogramach `kg` i przelicz na gramy.
--
-- ### Wejście
--

-- * 1 linia: `kg`

--
-- ### Wyjście
--

-- * 1 linia: `g` jako **liczba całkowita**, gdzie:

--   `g = kg * 1000`
--
-- ### Gwarancje
--

-- * `kg` jest liczbą całkowitą **lub** taką, że wynik w gramach jest całkowity.

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 2.5
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 2500
-- ```
--
-- ZAD-06B — Cale → centymetry
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `konwersje`, `float`

--
-- ### Treść
--
-- Wczytaj liczbę cali `inch` i przelicz na centymetry.
--
-- ### Wejście
--

-- * 1 linia: `inch`

--
-- ### Wyjście
--

-- * 1 linia: `cm = inch * 2.54` wypisane do **2 miejsc po przecinku**

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 10
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 25.40
-- ```
--
-- ZAD-06C — Sekundy → pełne godziny
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `dzielenie całkowite`

--
-- ### Treść
--
-- Wczytaj liczbę sekund `s` i wypisz liczbę **pełnych godzin**.
--
-- ### Wejście
--

-- * 1 linia: `s` (liczba całkowita, `s ≥ 0`)

--
-- ### Wyjście
--

-- * 1 linia: `s // 3600`

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 8639
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 2
-- ```
--
-- ZAD-06D — Euro → złotówki (kurs stały)
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `konwersje`, `float`

--
-- ### Treść
--
-- Wczytaj kwotę w euro `eur` i przelicz na złotówki przy stałym kursie.
--
-- ### Wejście
--

-- * 1 linia: `eur`

--
-- ### Wyjście
--

-- * 1 linia: `pln = eur * 4.4` do **2 miejsc po przecinku**

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 3
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 13.20
-- ```
--
-- ZAD-06E — Stopnie → radiany
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `pi`, `float`

--
-- ### Treść
--
-- Wczytaj kąt w stopniach `deg` i przelicz na radiany.
--
-- ### Wejście
--

-- * 1 linia: `deg`

--
-- ### Wyjście
--

-- * 1 linia: `rad = deg * π / 180` do **3 miejsc po przecinku**

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 180
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 3.142
-- ```
--
-- ZAD-06F — Fahrenheit → Celsius i Kelviny
--

-- ** Poziom:** ★☆☆

-- ** Tagi:** `konwersje`, `float`

--
-- ### Treść
--
-- Wczytaj temperaturę w stopniach Fahrenheita `F`. Oblicz temperaturę w Celsjuszach oraz Kelvinach.
--
-- ### Wejście
--

-- * 1 linia: `F`

--
-- ### Wyjście
--
-- Dwie linie:
--
-- 1. `C = (5/9) * (F - 32)` do **3 miejsc**
-- 2. `K = C + 273.15` do **3 miejsc**
--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 32
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 0.000
-- 273.150
-- ```
{-
Tytul: Konwersja jednostek.

Tresc zadania: Napisz program, ktory bedzie konwertowac jednostki zgodnie z nastepujacymi instrukcjami:

a) Pobierz wielkosc w kilogramach i wypisz, ile gramow odpowiada.

b) Pobierz wielkosc w calach i wypisz, ile centymetrow odpowiada.

c) Pobierz liczbe sekund i przelicz na godziny.

d) Pobierz liczbe w euro i wypisz, ile zlotowek odpowiada.

e) Pobierz miare kata w stopniach i wypisz, ile radianow odpowiada.

f) Pobierz temperature w stopniach Fahrenheita i wypisz ile stopni Celsjusza oraz ile stopni Kelvina odpowiada.

Dane wejsciowe: Liczba naturalna we wszystkich podpunktach.

Dane wyjsciowe:

\* Liczba naturalna dla podpunktow 1 i 3.
\* Liczba zmiennoprzecinkowa dla pozostalych podpunktow.

Przyklad:

a) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 2000.

b) Dla pobranej liczby: 12, powinna zostac wypisana liczba: 4.724.

c) Dla pobranej liczby: 3600, powinna zostac wypisana liczba: 1.

d) Dla pobranej liczby: 4, powinna zostac wypisana liczba: 17.6.

e) Dla pobranej liczby: 120, powinna zostac wypisana liczba:  2.094.

f) Dla pobranej liczby: 100, powinny zostac wypisane liczby: 37.777 i -235.222.
-}

main :: IO ()
main = do
  putStrLn "a) Podaj wielkosc w kilogramach:"
  kg <- readLn :: IO Double
  let grams = kg * 1000
  putStrLn $ "Liczba gramow: " ++ show grams

  putStrLn "b) Podaj wielkosc w calach:"
  inches <- readLn :: IO Double
  let centimeters = inches * 2.54
  putStrLn $ "Liczba centymetrow: " ++ show centimeters

  putStrLn "c) Podaj liczbe sekund:"
  seconds <- readLn :: IO Int
  let hours = div seconds 3600
  putStrLn $ "Liczba godzin: " ++ show hours

  putStrLn "d) Podaj liczbe w euro:"
  euro <- readLn :: IO Double
  let exchangeRate = 4.4
  let zloty = euro * exchangeRate
  putStrLn $ "Liczba zlotowek: " ++ show zloty

  putStrLn "e) Podaj miare kata w stopniach:"
  degrees <- readLn :: IO Double
  let radians = degrees * (pi / 180)
  putStrLn $ "Liczba radianow: " ++ show radians

  putStrLn "f) Podaj temperature w stopniach Fahrenheita:"
  fahrenheit <- readLn :: IO Double
  let celsius = (fahrenheit - 32) * (5 / 9)
  let kelvin = celsius + 273.15
  putStrLn $ "Liczba stopni Celsjusza: " ++ show celsius
  putStrLn $ "Liczba stopni Kelvina: " ++ show kelvin
