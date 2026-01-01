{-
ZAD-03 — Rok przestępny

\**Poziom:** ★☆☆
\**Tagi:** `modulo`, `if`, `kalendarz`

### Treść

Wczytaj rok `y` i sprawdź, czy jest przestępny w kalendarzu gregoriańskim.

Wypisz:

\* `Rok jest przestępny.`
\* `Rok nie jest przestępny.`

### Wejście

\* 1 linia: `y` (liczba całkowita, `y ≥ 0`)

### Wyjście

Jedna linia — odpowiedni komunikat.

### Definicja

Rok jest przestępny, gdy:

\* jest podzielny przez 400 **lub**
\* jest podzielny przez 4 i **nie** jest podzielny przez 100.

### Przykład

\**Wejście:**

```
2100
```

\**Wyjście:**

```
Rok nie jest przestępny.
```

-}
main :: IO ()
main = do
  y <- readLn :: IO Int
  let isLeap = (y `mod` 400 == 0) || (y `mod` 4 == 0 && y `mod` 100 /= 0)
  if isLeap
    then putStrLn "Rok jest przestępny."
    else putStrLn "Rok nie jest przestępny."
