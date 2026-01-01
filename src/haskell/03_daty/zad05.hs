{-
ZAD-05 — Liczba dni w miesiącu (rok nieprzestępny)

\**Poziom:** ★☆☆
\**Tagi:** `if`, `tablice`, `walidacja`

### Treść

Wczytaj numer miesiąca `m`. Zakładając rok **nieprzestępny**, wypisz liczbę dni w tym miesiącu.
Jeśli `m` nie jest w zakresie 1–12, wypisz:
`Niepoprawny numer miesiąca.`

### Wejście

\* 1 linia: `m` (liczba całkowita, `m ≥ 0`)

### Wyjście

\* liczba dni (jedna linia) **albo**
\* komunikat o błędzie (jedna linia)

### Przykład

\**Wejście:**

```
2
```

\**Wyjście:**

```
28
```

-}
main :: IO ()
main = do
  m <- readLn :: IO Int
  let daysInMonth = case m of
        1 -> 31
        2 -> 28  -- non-leap year
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
        _ -> -1
  if daysInMonth == -1
    then putStrLn "Niepoprawny numer miesiąca."
    else print daysInMonth
