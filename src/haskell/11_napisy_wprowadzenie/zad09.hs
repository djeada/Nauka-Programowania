{-
ZAD-09 — Rozdziel informacje o pracowniku

\**Poziom:** ★☆☆
\**Tagi:** `split`, `formatowanie`

### Treść

Wczytaj linię z danymi pracownika rozdzielonymi średnikami `;`:

1. Imię, 2) Nazwisko, 3) Miejsce urodzenia, 4) Stanowisko, 5) Zarobki

Wypisz każdą informację w osobnej linii z etykietą.

### Wejście

\* 1. linia: dane w formacie `Imię; Nazwisko; Miasto; Zawód; Zarobki;`

### Wyjście

Pięć linii w formacie:

\* `Imię: ...`
\* `Nazwisko: ...`
\* `Miejsce urodzenia: ...`
\* `Zawód: ...`
\* `Zarobki: ...`

### Przykład

\**Wejście:**

```
Jan; Kowalski; Warszawa; Programista; 1000;
```

\**Wyjście:**

```
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Warszawa
Zawód: Programista
Zarobki: 1000
```

### Uwagi

\* Po `split(';')` usuń ewentualne spacje z brzegów pól (np. `strip()`).
\* Ostatni średnik może powodować pusty element na końcu — zignoruj go.

-}

-- Dzieli napis po podanym znaku
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(n)
splitOn :: Char -> String -> [String]
splitOn delimiter str = case dropWhile (== delimiter) str of
    "" -> []
    s' -> w : splitOn delimiter s''
        where (w, s'') = break (== delimiter) s'

-- Usuwa białe znaki z początku i końca napisu
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(n)
strip :: String -> String
strip = reverse . dropWhile (== ' ') . reverse . dropWhile (== ' ')

-- Przetwarza dane pracownika rozdzielone średnikami
-- Złożoność czasowa: O(n), gdzie n to długość wejścia
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    linia <- getLine
    let pola = map strip $ splitOn ';' linia
    let dane = filter (not . null) pola
    let etykiety = ["Imię", "Nazwisko", "Miejsce urodzenia", "Zawód", "Zarobki"]
    mapM_ putStrLn $ zipWith (\e d -> e ++ ": " ++ d) etykiety dane
