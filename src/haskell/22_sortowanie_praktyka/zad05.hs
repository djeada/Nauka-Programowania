{-
ZAD-05 — Sortowanie listy miast

\**Poziom:** ★☆☆
\**Tagi:** `class`, `sort`, `obiekty`

### Treść

Masz klasę `Miasto` z polami:

\* `nazwa` (napis),
\* `liczba_mieszkancow` (liczba naturalna).

Otrzymujesz listę miast.

a) Posortuj miasta alfabetycznie po nazwie.
b) Posortuj miasta rosnąco po liczbie mieszkańców.

Wypisz wyniki w dwóch liniach jako listy w formacie jak w przykładzie.

### Wejście

\* 1 linia: liczba naturalna `N`
\* następnie `N` linii: `nazwa liczba_mieszkancow` (nazwa bez spacji)

### Wyjście

\* 1 linia: lista miast po sortowaniu a)
\* 2 linia: lista miast po sortowaniu b)

### Przykład

\**Wejście:**

```
3
Paris 2150000
Berlin 3800000
New_York 8400000
```

\**Wyjście:**

```
[Miasto("Berlin", 3800000), Miasto("New_York", 8400000), Miasto("Paris", 2150000)]
[Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New_York", 8400000)]
```

### Uwagi o formatowaniu

\* Wydruk obiektów ma mieć dokładnie format: `Miasto("NAZWA", LICZBA)`.

-}

import Data.List (sortBy, intercalate)
import Data.Ord (comparing)

-- Sortowanie listy miast
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)

-- Typ danych reprezentujący miasto
data Miasto = Miasto String Int deriving (Eq)

-- Funkcja do formatowania Miasto
instance Show Miasto where
    show (Miasto nazwa pop) = "Miasto(\"" ++ nazwa ++ "\", " ++ show pop ++ ")"

-- Funkcja do formatowania listy miast
formatList :: [Miasto] -> String
formatList xs = "[" ++ intercalate ", " (map show xs) ++ "]"

main :: IO ()
main = do
    nStr <- getLine
    let n = read nStr :: Int
    miasta <- readCities n
    -- a) Sortowanie alfabetycznie po nazwie
    let sortedByName = sortBy (comparing (\(Miasto nazwa _) -> nazwa)) miasta
    putStrLn $ formatList sortedByName
    -- b) Sortowanie rosnąco po liczbie mieszkańców
    let sortedByPop = sortBy (comparing (\(Miasto _ pop) -> pop)) miasta
    putStrLn $ formatList sortedByPop

-- Funkcja pomocnicza do wczytania N miast
readCities :: Int -> IO [Miasto]
readCities 0 = return []
readCities n = do
    line <- getLine
    let [nazwa, popStr] = words line
    let pop = read popStr :: Int
    rest <- readCities (n - 1)
    return (Miasto nazwa pop : rest)
