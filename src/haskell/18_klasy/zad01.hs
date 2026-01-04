{-
ZAD-01 — Klasa Koło

\**Poziom:** ★★☆
\**Tagi:** `class`, `metody`, `float`, `math`

### Treść

Zaprojektuj klasę **Koło**:

1. Konstruktor przyjmuje promień `r` (domyślnie 1).
2. Metoda licząca **obwód**: ( 2\pi r )
3. Metoda licząca **pole**: ( \pi r^2 )
4. Metoda wypisująca informacje: promień, obwód i pole.

Program ma utworzyć koło o promieniu wczytanym z wejścia (np. 3) i wypisać informacje.

### Wejście

\* 1 linia: `r` (liczba rzeczywista)

### Wyjście

Trzy linie jak w przykładzie (obwód i pole do 4 miejsc po przecinku).

### Przykład

\**Wejście:**

```
3
```

\**Wyjście:**

```
Koło o promieniu: 3
Obwód koła: 18.8496
Pole koła: 28.2743
```

-}

import Text.Printf (printf)

-- Typ danych reprezentujący koło
-- Złożoność pamięciowa: O(1)
data Kolo = Kolo {promien :: Double}

-- Oblicza obwód koła
-- Złożoność czasowa: O(1)
obwod :: Kolo -> Double
obwod (Kolo r) = 2 * pi * r

-- Oblicza pole koła
-- Złożoność czasowa: O(1)
pole :: Kolo -> Double
pole (Kolo r) = pi * r * r

-- Wypisuje informacje o kole
wypisz :: Kolo -> IO ()
wypisz k@(Kolo r) = do
  printf "Koło o promieniu: %.0f\n" r
  printf "Obwód koła: %.4f\n" (obwod k)
  printf "Pole koła: %.4f\n" (pole k)

main :: IO ()
main = do
  r <- readLn :: IO Double
  let kolo = Kolo r
  wypisz kolo
