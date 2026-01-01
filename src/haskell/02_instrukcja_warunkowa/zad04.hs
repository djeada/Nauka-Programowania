{-
ZAD-04 — Maksimum i minimum z dwóch liczb

\**Poziom:** ★☆☆
\**Tagi:** `max`, `min`, `if`, `formatowanie`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Wypisz je w jednej linii w kolejności: **większa, potem mniejsza**, oddzielone pojedynczą spacją.
Jeśli `a = b`, wypisz `a b` (czyli dwie takie same liczby).

### Wejście

\* 1 linia: `a` (całkowita, `a ≥ 0`)
\* 2 linia: `b` (całkowita, `b ≥ 0`)

### Wyjście

Jedna linia:
`max(a, b) min(a, b)`

### Przykłady

\**Wejście:**

```
1
4
```

\**Wyjście:**

```
4 1
```

\**Wejście:**

```
5
5
```

\**Wyjście:**

```
5 5
```

-}
main :: IO ()
main = do
  aInput <- getLine
  bInput <- getLine
  let a = read aInput :: Int
  let b = read bInput :: Int
  let maxVal = max a b
  let minVal = min a b
  putStrLn $ show maxVal ++ " " ++ show minVal
