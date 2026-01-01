{-
ZAD-06 — Sprawdzanie poprawności daty

\**Poziom:** ★★☆
\**Tagi:** `walidacja`, `przestępny`, `if`

### Treść

Wczytaj `d, m, y` i sprawdź, czy jest to poprawna data w kalendarzu gregoriańskim.

Wypisz:

\* `Data jest poprawna.`
\* `Data jest niepoprawna.`

### Wejście

3 liczby całkowite (w osobnych liniach):

1. `d` — dzień
2. `m` — miesiąc
3. `y` — rok

### Wyjście

Jedna linia — komunikat.

### Ograniczenia / gwarancje

\* `y ≥ 0` (lub `y ≥ 1`, jeśli tak chcesz przyjąć — ważne, by było spójnie w całym zbiorze)

### Reguły walidacji

1. `m` musi być w zakresie 1–12
2. Ustal liczbę dni w miesiącu:

   * 31: 1,3,5,7,8,10,12
   * 30: 4,6,9,11
   * luty: 28 lub 29 (zależnie od przestępności roku)
3. `d` musi być w zakresie 1–dni_w_miesiącu

### Przykład

\**Wejście:**

```
31
4
2021
```

\**Wyjście:**

```
Data jest niepoprawna.
```

-}
main :: IO ()
main = do
  d <- readLn :: IO Int
  m <- readLn :: IO Int
  y <- readLn :: IO Int
  
  let isLeap = (y `mod` 400 == 0) || (y `mod` 4 == 0 && y `mod` 100 /= 0)
  let daysInMonth = case m of
        1 -> 31
        2 -> if isLeap then 29 else 28
        3 -> 31
        4 -> 30
        5 -> 31
        6 -> 30
        7 -> 31
        8 -> 31
        9 -> 30
        10 -> 31
        11 -> 30
        12 -> 31
        _ -> 0
  
  let isValid = m >= 1 && m <= 12 && d >= 1 && d <= daysInMonth
  
  if isValid
    then putStrLn "Data jest poprawna."
    else putStrLn "Data jest niepoprawna."
