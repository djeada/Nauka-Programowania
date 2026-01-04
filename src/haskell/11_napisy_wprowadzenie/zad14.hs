{-
ZAD-14 — Napis z liczb od 1 do n

\**Poziom:** ★☆☆
\**Tagi:** `pętle`, `string`

### Treść

Wczytaj `n` i wypisz napis złożony z kolejnych liczb od 1 do `n`, bez separatorów.

### Wejście

\* 1. linia: liczba naturalna `n` (n ≥ 1)

### Wyjście

\* 1. linia: ciąg `1..n` bez spacji

### Przykład

\**Wejście:**

```
3
```

\**Wyjście:**

```
123
```

-}

main :: IO ()
main = do
  n <- readLn :: IO Int
  let wynik = concatMap show [1 .. n]
  putStrLn wynik
