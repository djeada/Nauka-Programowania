{-
Tytuł: Pole powierzchni i objętość figur geometrycznych.

Treść zadania: Napisz program, który będzie obliczał pola powierzchni i objętości figur geometrycznych zgodnie z następującymi instrukcjami:

a) Pobierz długości podstawy i wysokości trójkąta i wypisz jego pole.

b) Pobierz długości boków prostokąta i wypisz jego pole.

c) Pobierz długości przekątnych rombu i wypisz jego pole.

d) Pobierz promień kuli i wypisz jej objętość.

e) Pobierz promień podstawy i wysokość stożka i wypisz jego objętość.

f) Pobierz długość, szerokość i wysokość graniastosłupa i wypisz jego objętość.

Jednostki są dowolne.

Dane wejściowe:

* Dwie liczby naturalne dla podpunktów a, b i c.
* Liczba naturalna dla podpunktu d.
* Dwie liczby naturalne dla podpunktu e.
* Trzy liczby naturalne dla podpunktu f.

Dane wyjściowe: Liczba naturalna dla wszystkich podpunktów.

Przykład:

a) Dla pobranych liczb: 5 i 2, powinna zostać wypisana liczba: 5.

b) Dla pobranych liczb: 3 i 3, powinna zostać wypisana liczba: 4.

c) Dla pobranych liczb: 2 i 4, powinna zostać wypisana liczba: 1.

d) Dla pobranej liczby: 2, powinna zostać wypisana liczba: 33.493.

e) Dla pobranych liczb: 3 i 2, powinna zostać wypisana liczba: 18.84.

f) Dla pobranych liczb: 2, 2 i 2, powinny zostać wypisana liczba: 8.
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
