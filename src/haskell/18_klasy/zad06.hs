{-
ZAD-06 — Klasa LiczbaZespolona

\**Poziom:** ★★☆
\**Tagi:** `class`, `operacje`, `math`

### Treść

Zaprojektuj klasę **LiczbaZespolona**:

\* konstruktor `(re=0, im=0)`,
\* dodawanie, odejmowanie, mnożenie, dzielenie,
\* porównania,
\* moduł,
\* wypisywanie w formacie `a + bi` lub `a - bi` (z zachowaniem znaku).

Program tworzy:

\* A = 9 + 12i
\* B = -3 - 3i

Wypisuje A, B oraz: sumę, różnicę A-B, iloczyn i iloraz A/B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

\**Wyjście:**

```
Liczba A: 9 + 12i
Liczba B: -3 - 3i

Suma: 6 + 9i
Różnica A - B: 12 + 15i
Iloczyn: 27 + 63i
Iloraz A / B: -3.5 + 0.5i
```

-}

import Text.Printf (printf)

-- Typ danych reprezentujący liczbę zespoloną
-- Złożoność pamięciowa: O(1)
data LiczbaZespolona = LiczbaZespolona { re :: Double, im :: Double } deriving (Eq)

-- Dodawanie liczb zespolonych
-- Złożoność czasowa: O(1)
dodajZ :: LiczbaZespolona -> LiczbaZespolona -> LiczbaZespolona
dodajZ (LiczbaZespolona r1 i1) (LiczbaZespolona r2 i2) = LiczbaZespolona (r1 + r2) (i1 + i2)

-- Mnożenie liczb zespolonych
-- Złożoność czasowa: O(1)
mnozZ :: LiczbaZespolona -> LiczbaZespolona -> LiczbaZespolona
mnozZ (LiczbaZespolona r1 i1) (LiczbaZespolona r2 i2) = 
    LiczbaZespolona (r1*r2 - i1*i2) (r1*i2 + i1*r2)

-- Moduł liczby zespolonej
-- Złożoność czasowa: O(1)
modulZ :: LiczbaZespolona -> Double
modulZ (LiczbaZespolona r i) = sqrt (r^2 + i^2)

-- Wypisuje liczbę zespoloną
wypiszZ :: LiczbaZespolona -> String
wypiszZ (LiczbaZespolona r i)
    | i >= 0 = printf "%.0f + %.0fi" r i
    | otherwise = printf "%.0f - %.0fi" r (abs i)

main :: IO ()
main = do
    let a = LiczbaZespolona 9 12
    let b = LiczbaZespolona (-3) (-3)
    putStrLn $ "A = " ++ wypiszZ a
    putStrLn $ "B = " ++ wypiszZ b
    printf "|A| = %.2f\n" (modulZ a)
    putStrLn $ "A + B = " ++ wypiszZ (dodajZ a b)
