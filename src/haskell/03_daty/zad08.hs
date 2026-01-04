{-
ZAD-08 — Dzień tygodnia dla daty (Zeller)

\**Poziom:** ★★☆
\**Tagi:** `algorytmy`, `Zeller`, `mapowanie`, `daty`

### Treść

Wczytaj datę `d, m, y` i wyznacz nazwę dnia tygodnia, używając **kongruencji Zellera** dla kalendarza gregoriańskiego.

Kroki:

1. Jeśli `m <= 2`, to:

\* `m = m + 12`
\* `y = y - 1`

2. Oblicz:

\* `K = y % 100`
\* `J = y // 100`
\* `h = (d + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7`

3. Zmapuj `h` na dzień tygodnia:

\* 0 → `Sobota`
\* 1 → `Niedziela`
\* 2 → `Poniedziałek`
\* 3 → `Wtorek`
\* 4 → `Środa`
\* 5 → `Czwartek`
\* 6 → `Piątek`

### Wejście

3 liczby całkowite (w osobnych liniach): `d`, `m`, `y`

### Wyjście

Jedna linia: nazwa dnia tygodnia (dokładnie jedna z: Poniedziałek, Wtorek, Środa, Czwartek, Piątek, Sobota, Niedziela).

### Ograniczenia / gwarancje

\* Data wejściowa jest poprawna (zalecane; inaczej dopisz, co robić dla błędnej).
\* Kalendarz gregoriański.

### Przykład

\**Wejście:**

```
9
10
2020
```

\**Wyjście:**

```
Piątek
```

-}
main :: IO ()
main = do
  d <- readLn :: IO Int
  m <- readLn :: IO Int
  y <- readLn :: IO Int

  let (m', y') = if m <= 2 then (m + 12, y - 1) else (m, y)
  let k = y' `mod` 100
  let j = y' `div` 100
  let h = (d + (13 * (m' + 1)) `div` 5 + k + k `div` 4 + j `div` 4 + 5 * j) `mod` 7

  let dayName = case h of
        0 -> "Sobota"
        1 -> "Niedziela"
        2 -> "Poniedziałek"
        3 -> "Wtorek"
        4 -> "Środa"
        5 -> "Czwartek"
        6 -> "Piątek"
        _ -> error "Invalid h value"

  putStrLn dayName
