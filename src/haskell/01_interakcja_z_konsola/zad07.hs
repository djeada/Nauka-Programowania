{-
Tytul: Pole powierzchni i objetosc figur geometrycznych.

Tresc zadania: Napisz program, ktory bedzie obliczal pola powierzchni i objetosci figur geometrycznych zgodnie z nastepujacymi instrukcjami:

a) Pobierz dlugosci podstawy i wysokosci trojkata i wypisz jego pole.

b) Pobierz dlugosci bokow prostokata i wypisz jego pole.

c) Pobierz dlugosci przekatnych rombu i wypisz jego pole.

d) Pobierz promien kuli i wypisz jej objetosc.

e) Pobierz promien podstawy i wysokosc stozka i wypisz jego objetosc.

f) Pobierz dlugosc, szerokosc i wysokosc graniastoslupa i wypisz jego objetosc.

Jednostki sa dowolne.

Dane wejsciowe:

* Dwie liczby naturalne dla podpunktow a, b i c.
* Liczba naturalna dla podpunktu d.
* Dwie liczby naturalne dla podpunktu e.
* Trzy liczby naturalne dla podpunktu f.

Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.

Przyklad:

a) Dla pobranych liczb: 5 i 2, powinna zostac wypisana liczba: 5.

b) Dla pobranych liczb: 3 i 3, powinna zostac wypisana liczba: 4.

c) Dla pobranych liczb: 2 i 4, powinna zostac wypisana liczba: 1.

d) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 33.493.

e) Dla pobranych liczb: 3 i 2, powinna zostac wypisana liczba: 18.84.

f) Dla pobranych liczb: 2, 2 i 2, powinny zostac wypisana liczba: 8.
-}

main :: IO ()
main = do
  putStrLn "a) Podaj dlugosci podstawy i wysokosci trojkata:"
  base <- readLn :: IO Double
  height <- readLn :: IO Double
  let triangleArea = 0.5 * base * height
  putStrLn $ "Pole trojkata: " ++ show triangleArea

  putStrLn "b) Podaj dlugosci bokow prostokata:"
  length1 <- readLn :: IO Double
  width1 <- readLn :: IO Double
  let rectangleArea = length1 * width1
  putStrLn $ "Pole prostokata: " ++ show rectangleArea

  putStrLn "c) Podaj dlugosci przekatnych rombu:"
  diagonal1 <- readLn :: IO Double
  diagonal2 <- readLn :: IO Double
  let rhombusArea = 0.5 * diagonal1 * diagonal2
  putStrLn $ "Pole rombu: " ++ show rhombusArea

  putStrLn "d) Podaj promien kuli:"
  radius <- readLn :: IO Double
  let sphereVolume = (4 / 3) * pi * (radius ^ 3)
  putStrLn $ "Objetosc kuli: " ++ show sphereVolume

  putStrLn "e) Podaj promien podstawy i wysokosc stozka:"
  baseRadius <- readLn :: IO Double
  coneHeight <- readLn :: IO Double
  let coneVolume = (1 / 3) * pi * (baseRadius ^ 2) * coneHeight
  putStrLn $ "Objetosc stozka: " ++ show coneVolume

  putStrLn "f) Podaj dlugosc, szerokosc i wysokosc graniastoslupa:"
  length2 <- readLn :: IO Double
  width2 <- readLn :: IO Double
  height2 <- readLn :: IO Double
  let prismVolume = length2 * width2 * height2
  putStrLn $ "Objetosc graniastoslupa: " ++ show prismVolume

