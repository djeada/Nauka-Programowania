{-
ZAD-03 — Wypisywanie liczby π z określoną dokładnością

\**Poziom:** ★☆☆
\**Tagi:** `math.pi`, `formatowanie`, `pętle`

### Treść

1. Wczytaj liczbę naturalną `n` (`n > 0`).
2. Wypisz liczbę π dokładnie `n` razy.
3. Każda wypisana wartość ma mieć **dokładnie `n` miejsc po przecinku**.

### Wejście

Jedna liczba naturalna:

\* 1. linia: `n` (`n > 0`)

### Wyjście

`n` wierszy, w każdym liczba π z dokładnością do `n` miejsc po przecinku.

### Przykład

\**Wejście:**

```
2
```

\**Wyjście:**

```
3.14
3.14
```

### Uwagi o formatowaniu

\* Liczba miejsc po przecinku ma być **dokładnie** równa `n` (np. dla `n=1` wypisz `3.1`).
\* Stosuj standardowe zaokrąglanie przy formatowaniu.

-}
import Text.Printf

main :: IO ()
main = do
  n <- readLn :: IO Int
  let pi_val = pi :: Double
  let formatStr = "%." ++ show n ++ "f\n"
  mapM_ (\_ -> printf formatStr pi_val) [1..n]
