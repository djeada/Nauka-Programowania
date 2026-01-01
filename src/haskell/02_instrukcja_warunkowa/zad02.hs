{-
ZAD-02 — Porównanie dwóch liczb

\**Poziom:** ★☆☆
\**Tagi:** `if-else`, `równość`, `string`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Jeśli są równe, wypisz:
`Liczby są identyczne.`
W przeciwnym razie wypisz:
`Liczby są różne.`

### Wejście

\* 1 linia: `a` (całkowita, `a ≥ 0`)
\* 2 linia: `b` (całkowita, `b ≥ 0`)

### Wyjście

Jedna linia — dokładnie jeden z komunikatów.

### Przykład 1

\**Wejście:**

```
7
4
```

\**Wyjście:**

```
Liczby są różne.
```

### Przykład 2

\**Wejście:**

```
5
5
```

\**Wyjście:**

```
Liczby są identyczne.
```

-}
main :: IO ()
main = do
  aInput <- getLine
  bInput <- getLine
  let a = read aInput :: Int
  let b = read bInput :: Int
  if a == b
    then putStrLn "Liczby są identyczne."
    else putStrLn "Liczby są różne."
