{-
ZAD-05 — Litera „X”

\**Poziom:** ★★☆
\**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj `n` (`n ≥ 3`) i wypisz literę `X` o wysokości `n`, zbudowaną z `*` na obu przekątnych.

W wierszu `i` i kolumnie `j` (indeksy od 0):

\* wypisz `*`, gdy `j == i` **lub** `j == n - 1 - i`,
\* w przeciwnym razie wypisz spację.

### Wejście

\* 1. linia: `n` (`n ≥ 3`)

### Wyjście

`n` linii po `n` znaków (`*` lub spacja).

### Przykład

\**Wejście:**

```
5
```

\**Wyjście:**

```
\*   *
 * *
  *
 * *
\*   *
```

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  mapM_ (\i -> putStrLn [if j == i || j == n - 1 - i then '*' else ' ' | j <- [0 .. n - 1]]) [0 .. n - 1]
