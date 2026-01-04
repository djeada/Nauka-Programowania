{-
ZAD-01 — Sortowanie znaków w napisie

\**Poziom:** ★☆☆
\**Tagi:** `sort`, `string`

### Treść

Otrzymujesz napis. Posortuj alfabetycznie wszystkie jego znaki i wypisz wynikowy napis.

### Wejście

\* 1 linia: napis `s`

### Wyjście

\* 1 linia: napis `s` po posortowaniu znaków rosnąco (porównanie znaków jak w Pythonie / Unicode)

### Przykład

\**Wejście:**

```
Ala ma kota
```

\**Wyjście:**

```
 Aaaaklmot
```

### Uwagi o formatowaniu

\* Spacje też są znakami i biorą udział w sortowaniu (dlatego w przykładzie wyjście zaczyna się od spacji).

-}

import Data.List (sort)

-- Sortowanie znaków w napisie
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  napis <- getLine
  putStrLn $ sort napis
