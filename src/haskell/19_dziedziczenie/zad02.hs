{-
ZAD-02 — Klasa Kształt oraz klasy Koło i Kwadrat

\**Poziom:** ★★☆
\**Tagi:** `dziedziczenie`, `polimorfizm`, `math`

### Treść

Zaprojektuj hierarchię klas:

\* **Kształt** — klasa bazowa (ogólna) dla kształtów.
\* **Koło** — dziedziczy po `Kształt`.
\* **Kwadrat** — dziedziczy po `Kształt`.

Każda klasa ma mieć:

\* metodę obliczającą **pole**,
\* metodę wypisującą informacje o obiekcie: typ, parametry i pole.

Program:

\* wczytuje promień `r` koła oraz bok `a` kwadratu,
\* tworzy obiekty `Koło(r)` i `Kwadrat(a)`,
\* wypisuje informacje o obu.

\**Uwaga do formatowania:**
\*Pole koła wypisz do 4 miejsc po przecinku.*
\*Pole kwadratu wypisz bez wymuszania miejsc po przecinku (jak w przykładzie).*

### Wejście

\* 1 linia: `r` (liczba rzeczywista)
\* 2 linia: `a` (liczba rzeczywista)

### Wyjście

Blok informacji o kole, pusta linia, blok informacji o kwadracie.

### Przykład

\**Wejście:**

```
5
4
```

\**Wyjście:**

```
Kształt: Koło
Promień: 5
Pole powierzchni: 78.5398

Kształt: Kwadrat
Długość boku: 4
Pole powierzchni: 16
```

-}

import Text.Printf (printf)

-- Type class dla kształtów
-- Złożoność pamięciowa: O(1)
class Ksztalt a where
  pole :: a -> Double
  wypisz :: a -> IO ()

data Kolo = Kolo {promienK :: Double}

instance Ksztalt Kolo where
  pole (Kolo r) = pi * r * r
  wypisz k@(Kolo r) = do
    printf "Koło o promieniu %.1f\n" r
    printf "Pole: %.2f\n" (pole k)

data Kwadrat = Kwadrat {bok :: Double}

instance Ksztalt Kwadrat where
  pole (Kwadrat a) = a * a
  wypisz k@(Kwadrat a) = do
    printf "Kwadrat o boku %.1f\n" a
    printf "Pole: %.2f\n" (pole k)

main :: IO ()
main = do
  r <- readLn :: IO Double
  a <- readLn :: IO Double
  let kolo = Kolo r
  let kwadrat = Kwadrat a
  wypisz kolo
  wypisz kwadrat
