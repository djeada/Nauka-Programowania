{-
ZAD-03 — Pole nałożenia się dwóch prostokątów

\**Poziom:** ★★☆
\**Tagi:** `class`, `static`, `geometria`

### Treść

Zaprojektuj klasę **Prostokąt** opisaną przez dwa przeciwległe wierzchołki:

\* lewy dolny `(x1, y1)`
\* prawy górny `(x2, y2)`
  Boki równoległe do osi.

Klasa ma mieć:

1. Konstruktor `(x1, y1, x2, y2)`
2. Metodę statyczną `pole_wspolne(A, B)` zwracającą pole części wspólnej (albo 0).
3. Metodę wypisującą informacje o prostokącie.

Program tworzy:

\* A: (3, 4) i (9, 6)
\* B: (2, 2) i (7, 5)

Wypisuje oba i pole części wspólnej.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

\**Wyjście:**

```
Prostokąt A: lewy dolny (3, 4), prawy górny (9, 6)
Prostokąt B: lewy dolny (2, 2), prawy górny (7, 5)
Pole części wspólnej: 6
```

-}

import Text.Printf (printf)

-- Typ danych reprezentujący prostokąt
-- Złożoność pamięciowa: O(1)
data Prostokat = Prostokat { x1 :: Int, y1 :: Int, x2 :: Int, y2 :: Int }

-- Oblicza pole części wspólnej dwóch prostokątów
-- Złożoność czasowa: O(1)
poleWspolne :: Prostokat -> Prostokat -> Int
poleWspolne (Prostokat x1a y1a x2a y2a) (Prostokat x1b y1b x2b y2b) =
    let xLeft = max x1a x1b
        yBottom = max y1a y1b
        xRight = min x2a x2b
        yTop = min y2a y2b
        width = max 0 (xRight - xLeft)
        height = max 0 (yTop - yBottom)
    in width * height

-- Wypisuje informacje o prostokącie
wypisz :: String -> Prostokat -> IO ()
wypisz nazwa (Prostokat x1 y1 x2 y2) =
    printf "Prostokąt %s: lewy dolny (%d, %d), prawy górny (%d, %d)\n" nazwa x1 y1 x2 y2

main :: IO ()
main = do
    let a = Prostokat 3 4 9 6
    let b = Prostokat 2 2 7 5
    wypisz "A" a
    wypisz "B" b
    printf "Pole części wspólnej: %d\n" (poleWspolne a b)
