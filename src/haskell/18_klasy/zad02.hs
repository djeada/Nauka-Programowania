{-
ZAD-02 — Klasa Punkt

\**Poziom:** ★★☆
\**Tagi:** `class`, `static`, `porównania`, `math`

### Treść

Zaprojektuj klasę **Punkt**:

1. Konstruktor `(x=0, y=0)`.
2. Metoda statyczna `odleglosc(p1, p2)` licząca odległość.
3. Metoda wypisująca współrzędne.
4. Porównania `==` i `!=` (równe, gdy oba współrzędne identyczne).

Program tworzy:

\* A = (5, 5)
\* B = (-3, -3)

Wypisuje oba punkty i odległość między nimi (4 miejsca po przecinku).

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

\**Wyjście:**

```
Punkt A: (5, 5)
Punkt B: (-3, -3)
Odległość między punktami A i B: 11.3137
```

-}

import Text.Printf (printf)

-- Typ danych reprezentujący punkt
-- Złożoność pamięciowa: O(1)
data Punkt = Punkt { x :: Double, y :: Double } deriving (Eq)

-- Oblicza odległość między dwoma punktami
-- Złożoność czasowa: O(1)
odleglosc :: Punkt -> Punkt -> Double
odleglosc (Punkt x1 y1) (Punkt x2 y2) = sqrt ((x2 - x1)^2 + (y2 - y1)^2)

-- Wypisuje współrzędne punktu
wypisz :: String -> Punkt -> IO ()
wypisz nazwa (Punkt x y) = printf "Punkt %s: (%.0f, %.0f)\n" nazwa x y

main :: IO ()
main = do
    let a = Punkt 5 5
    let b = Punkt (-3) (-3)
    wypisz "A" a
    wypisz "B" b
    printf "Odległość między punktami A i B: %.4f\n" (odleglosc a b)
