{-
ZAD-02 — Pełnoletność (18 lat)

\**Poziom:** ★☆☆
\**Tagi:** `daty`, `porównywanie`, `if`

### Treść

Wczytaj datę urodzenia oraz datę „dzisiaj” i sprawdź, czy osoba ma **ukończone 18 lat** w dniu daty aktualnej.

Wypisz:

\* `Osoba jest pełnoletnia.` — jeśli ma ≥ 18 lat,
\* `Osoba nie jest pełnoletnia.` — w przeciwnym razie.

### Wejście

6 liczb całkowitych (każda w osobnej linii):

1. `d1` — dzień urodzenia
2. `m1` — miesiąc urodzenia
3. `y1` — rok urodzenia
4. `d2` — aktualny dzień
5. `m2` — aktualny miesiąc
6. `y2` — aktualny rok

### Wyjście

Jedna linia — jeden z komunikatów.

### Ograniczenia / gwarancje

\* Obie daty są poprawne (nie musisz walidować).
\* Pełnoletność jest osiągana **dokładnie w dniu 18. urodzin**.

### Uwagi (jak to porównać)

Osoba jest pełnoletnia wtedy, gdy data `y1+18, m1, d1` jest **nie późniejsza** niż data aktualna.

### Przykład

\**Wejście:**

```
5
12
1999
20
11
2020
```

\**Wyjście:**

```
Osoba jest pełnoletnia.
```

-}
main :: IO ()
main = do
  d1 <- readLn :: IO Int
  m1 <- readLn :: IO Int
  y1 <- readLn :: IO Int
  d2 <- readLn :: IO Int
  m2 <- readLn :: IO Int
  y2 <- readLn :: IO Int

  let age18Year = y1 + 18
  let isAdult =
        (y2 > age18Year)
          || (y2 == age18Year && m2 > m1)
          || (y2 == age18Year && m2 == m1 && d2 >= d1)

  if isAdult
    then putStrLn "Osoba jest pełnoletnia."
    else putStrLn "Osoba nie jest pełnoletnia."
