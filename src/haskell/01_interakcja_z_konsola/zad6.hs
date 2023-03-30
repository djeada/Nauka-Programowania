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

* Liczba naturalna dla podpunktow 1 i 3.
* Liczba zmiennoprzecinkowa dla pozostalych podpunktow.

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

