{-
ZAD-12 — Najdłuższy ciąg zer otoczony jedynkami

\**Poziom:** ★★★
\**Tagi:** `binarne`, `binary gap`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. W jej reprezentacji binarnej znajdź długość najdłuższego ciągu kolejnych zer, który jest **z obu stron otoczony jedynkami** (tzw. *binary gap*).

Jeśli nie ma takiego ciągu — wypisz `0`.

### Wejście

\* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: długość najdłuższego „gapu”.

### Przykład

\**Wejście:**

```
14
```

\**Wyjście:**

```
0
```

### Uwagi (ważne)

\* `14` ma zapis `1110` — zero na końcu **nie jest otoczone jedynkami z prawej**, więc wynik to `0`.
  Dla przykładu `20` (`10100`) najdłuższy gap ma długość `1` (między `1` i `1`).

-}

-- Reprezentacja zmiennoprzecinkowa (IEEE 754 - uproszczona)
-- Złożoność czasowa: O(1)
-- Złożoność pamięciowa: O(1)
main :: IO ()
main = do
    x <- readLn :: IO Double
    putStrLn $ "Float representation (approximation): " ++ show x
    putStrLn $ "Sign: " ++ show (if x < 0 then 1 else 0)
    -- Uproszczona reprezentacja
