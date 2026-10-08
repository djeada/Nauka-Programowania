{-
ZAD-05A — Minimum bez instrukcji warunkowych

\**Poziom:** ★★☆
\**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby całkowite `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `min`, `max`, `abs`, `sorted`.

### Wejście

\* 1. linia: `a`
\* 2. linia: `b`

### Wyjście

Jedna liczba całkowita: mniejsza z liczb `a` i `b` (gdy są równe — ich wspólna wartość).

### Ograniczenia

\* $-10^9 \le a, b \le 10^9$ — w tym zadaniu liczby **mogą być ujemne**

### Przykład

\**Wejście:**

```
3
2
```

\**Wyjście:**

```
2
```

### Uwagi

\* Dopuszczalne są operacje arytmetyczne i bitowe.
\* Wskazówka: dla `d = a - b` wyrażenie `d >> 63` daje `-1` (same jedynki w zapisie binarnym), gdy `d < 0`, oraz `0`, gdy `d ≥ 0`. Wtedy `d & (d >> 63)` jest równe `d` albo `0`.
\* Tą samą sztuczką otrzymasz maksimum: `a - (d & (d >> 63))`.

ZAD-05B — Wartość bezwzględna bez instrukcji warunkowych

\**Poziom:** ★★☆
\**Tagi:** `bit-trick`, `maski`, `bez if`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jej wartość bezwzględną $|x|$ **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `abs`, `min`, `max`, `sorted`.

### Wejście

\* 1. linia: `x`

### Wyjście

Jedna liczba naturalna: $|x|$.

### Ograniczenia

\* $-10^9 \le x \le 10^9$ — liczba **może być ujemna**

### Przykład

\**Wejście:**

```
-12
```

\**Wyjście:**

```
12
```

### Uwagi

\* Dopuszczalne są operacje arytmetyczne i bitowe; porównania (`<`, `>`) nie są potrzebne.
\* Tak jak w ZAD-05A, **maska znaku** `m = x >> 63` jest równa `-1` (same jedynki), gdy `x < 0`, oraz `0`, gdy `x ≥ 0`.
\* XOR z maską `0` nic nie zmienia, a XOR z maską `-1` odwraca wszystkie bity, czyli daje $-x - 1$ (tak liczby ujemne zapisuje kod uzupełnień do dwóch). Wystarczy więc obliczyć `(x ^ m) - m`.

-}
import Data.Bits (shiftR, xor, (.&.))
import System.Environment (getArgs)

-- ZAD-05A: minimum bez instrukcji warunkowych
-- maska = d >> 63 to -1 dla d < 0 i 0 dla d >= 0
minimumBezIf :: Int -> Int -> Int
minimumBezIf a b = b + (d .&. (d `shiftR` 63))
  where
    d = a - b

-- ZAD-05B: wartość bezwzględna bez instrukcji warunkowych
-- (x ^ maska) - maska to x dla maski 0 oraz -x dla maski -1
wartoscBezwzgledna :: Int -> Int
wartoscBezwzgledna x = (x `xor` maska) - maska
  where
    maska = x `shiftR` 63

-- Złożoność czasowa: O(1), pamięciowa: O(1)
-- Uruchomienie: runghc zad05.hs A|B < dane.txt (domyślnie A)
main :: IO ()
main = do
  args <- getArgs
  liczby <- map read . words <$> getContents :: IO [Int]
  print $ case (args, liczby) of
    ("B" : _, x : _) -> wartoscBezwzgledna x
    (_, a : b : _) -> minimumBezIf a b
    _ -> error "Za mało danych"
