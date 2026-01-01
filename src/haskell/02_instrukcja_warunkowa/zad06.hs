{-
ZAD-06 — Maksimum z czterech liczb

\**Poziom:** ★☆☆
\**Tagi:** `max`, `if`, `porównania`

### Treść

Wczytaj cztery liczby naturalne i wypisz największą z nich.

### Wejście

4 linie: `a`, `b`, `c`, `d` (całkowite, każda `≥ 0`)

### Wyjście

Jedna linia: największa liczba.

### Przykład

\**Wejście:**

```
2
5
1
4
```

\**Wyjście:**

```
5
```

-}
main :: IO ()
main = do
  aInput <- getLine
  bInput <- getLine
  cInput <- getLine
  dInput <- getLine
  let a = read aInput :: Int
  let b = read bInput :: Int
  let c = read cInput :: Int
  let d = read dInput :: Int
  let maxVal = maximum [a, b, c, d]
  print maxVal
