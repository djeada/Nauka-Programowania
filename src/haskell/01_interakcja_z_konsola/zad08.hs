-- ZAD-08 — Koszt pokrycia podłogi płytkami
--

-- ** Poziom:** ★★☆

-- ** Tagi:** `ceil`, `arytmetyka`, `formatowanie`, `geometria`

--
-- ### Treść
--
-- Dane są:
--

-- * cena jednej płytki `p`,

-- * bok płytki `t` (płytka kwadratowa),

-- * długość podłogi `L`,

-- * szerokość podłogi `W`.

--
-- Oblicz liczbę płytek potrzebnych do pokrycia całej podłogi, zakładając układ bez docinania „na styk” (czyli wzdłuż każdego wymiaru zaokrąglasz w górę), a następnie podaj koszt całkowity.
--
-- ### Wejście
--
-- 4 liczby (każda w osobnej linii): `p`, `t`, `L`, `W`
--
-- ### Wyjście
--
-- Jedna liczba: całkowity koszt do **2 miejsc po przecinku**.
--
-- ### Ograniczenia / gwarancje
--

-- * `p > 0`, `t > 0`, `L > 0`, `W > 0`

-- * Liczba płytek:

--
--   * `nL = ceil(L / t)`
--   * `nW = ceil(W / t)`
--   * `n = nL * nW`

-- * Koszt: `n * p`

--
-- ### Przykład
--

-- ** Wejście:**

--
-- ```
-- 2
-- 3
-- 20
-- 40
-- ```
--

-- ** Wyjście:**

--
-- ```
-- 196.00
-- ```
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
