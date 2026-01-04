{-
ZAD-04 — Klasy Wektor2D i Wektor3D

\**Poziom:** ★★☆
\**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasy **Wektor2D** i **Wektor3D**:

Wspólne:

\* konstruktor z domyślnymi współrzędnymi 0,
\* dodawanie, odejmowanie,
\* iloczyn skalarny,
\* porównania `==` i `!=`,
\* moduł (długość),
\* metoda wypisująca wektor.

Dodatkowo dla **Wektor3D**:

\* iloczyn wektorowy.

Program tworzy:

\* A = (-3, -3, -3)
\* B = (5, 5, 5)

Wypisuje A, B oraz:

\* A + B
\* A - B
\* A · B
\* A × B

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

\**Wyjście:**

```
Wektor A: (-3, -3, -3)
Wektor B: (5, 5, 5)
Suma wektorów: (2, 2, 2)
Różnica wektorów A - B: (-8, -8, -8)
Iloczyn skalarny: -45
Iloczyn wektorowy: (0, 0, 0)
```

-}

import Text.Printf (printf)

-- Typ danych reprezentujący wektor 2D
-- Złożoność pamięciowa: O(1)
data Wektor2D = Wektor2D {x2 :: Double, y2 :: Double} deriving (Eq)

-- Typ danych reprezentujący wektor 3D
-- Złożoność pamięciowa: O(1)
data Wektor3D = Wektor3D {x3 :: Double, y3 :: Double, z3 :: Double} deriving (Eq)

-- Operacje na wektorach 2D
dodaj2D :: Wektor2D -> Wektor2D -> Wektor2D
dodaj2D (Wektor2D x1 y1) (Wektor2D x2 y2) = Wektor2D (x1 + x2) (y1 + y2)

modul2D :: Wektor2D -> Double
modul2D (Wektor2D x y) = sqrt (x ^ 2 + y ^ 2)

-- Operacje na wektorach 3D
dodaj3D :: Wektor3D -> Wektor3D -> Wektor3D
dodaj3D (Wektor3D x1 y1 z1) (Wektor3D x2 y2 z2) = Wektor3D (x1 + x2) (y1 + y2) (z1 + z2)

modul3D :: Wektor3D -> Double
modul3D (Wektor3D x y z) = sqrt (x ^ 2 + y ^ 2 + z ^ 2)

main :: IO ()
main = do
  let v2 = Wektor2D 3 4
  let v3 = Wektor3D 1 2 2
  printf "Wektor 2D: (%.1f, %.1f), moduł: %.2f\n" (x2 v2) (y2 v2) (modul2D v2)
  printf "Wektor 3D: (%.1f, %.1f, %.1f), moduł: %.2f\n" (x3 v3) (y3 v3) (z3 v3) (modul3D v3)
