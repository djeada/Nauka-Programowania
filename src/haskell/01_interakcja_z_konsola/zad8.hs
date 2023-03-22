{-
Tytuł: Obliczenie ceny podłogi.

Treść: Otrzymasz cenę pojedynczej płytki, wymiary płytki w postaci kwadratu oraz wymiary podłogi w postaci prostokąta. Oblicz, ile kosztować będzie podłoga o podanych wymiarach.

Jednostki są umowne.

Dane wejściowe: Cztery liczby naturalne: cena płytki, długość boku płytki, długość podłogi oraz szerokość podłogi.

Dane wyjściowe: Liczba naturalna oznaczająca cenę podłogi.

Przykład:

Dla pobranych liczb: 2 (cena płytki), 3 (długość boku płytki), 20 (długość podłogi) oraz 40 (szerokość podłogi), powinna zostać wypisana liczba: 196.
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
