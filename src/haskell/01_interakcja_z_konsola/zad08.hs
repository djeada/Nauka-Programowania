{-
Tytul: Obliczenie ceny podlogi.

Tresc: Otrzymasz cene pojedynczej plytki, wymiary plytki w postaci kwadratu oraz wymiary podlogi w postaci prostokata. Oblicz, ile kosztowac bedzie podloga o podanych wymiarach.

Jednostki sa umowne.

Dane wejsciowe: Cztery liczby naturalne: cena plytki, dlugosc boku plytki, dlugosc podlogi oraz szerokosc podlogi.

Dane wyjsciowe: Liczba naturalna oznaczajaca cene podlogi.

Przyklad:

Dla pobranych liczb: 2 (cena plytki), 3 (dlugosc boku plytki), 20 (dlugosc podlogi) oraz 40 (szerokosc podlogi), powinna zostac wypisana liczba: 196.
-}

main :: IO ()
main = do
  putStrLn "Podaj cene pojedynczej plytki:"
  tilePrice <- readLn :: IO Double
  putStrLn "Podaj dlugosc boku plytki:"
  tileSideLength <- readLn :: IO Double
  putStrLn "Podaj dlugosc podlogi:"
  floorLength <- readLn :: IO Double
  putStrLn "Podaj szerokosc podlogi:"
  floorWidth <- readLn :: IO Double

  let tileArea = tileSideLength * tileSideLength
  let floorArea = floorLength * floorWidth
  let numberOfTiles = ceiling (floorArea / tileArea)
  let totalCost = fromIntegral numberOfTiles * tilePrice

  putStrLn $ "Cena podlogi: " ++ show totalCost

