{-
ZAD-03 — Sumowanie cyfr liczby

\**Poziom:** ★☆☆
\**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr. Następnie wypisz wynik.

### Wejście

Jedna liczba naturalna:

\* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba naturalna — suma cyfr liczby `n`.

### Przykład

\**Wejście:**

```
129
```

\**Wyjście:**

```
12
```

### Uwagi o formatowaniu

\* Dla `n = 0` suma cyfr wynosi `0`.

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  let sumDigits num = sum $ map (\c -> read [c] :: Int) $ show num
  print $ sumDigits n
