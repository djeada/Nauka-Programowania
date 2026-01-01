{-
ZAD-06 — Litera „Z”

\**Poziom:** ★★☆
\**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj `n` (`n ≥ 3`) i wypisz literę `Z` o wysokości `n`:

\* pierwszy wiersz: `n` gwiazdek,
\* ostatni wiersz: `n` gwiazdek,
\* w środku: jedna gwiazdka na przekątnej od prawej do lewej.

W wierszu `i` (0..n-1) i kolumnie `j`:

\* jeśli `i == 0` lub `i == n-1` → `*`
\* else jeśli `j == n-1-i` → `*`
\* else → spacja

### Wejście

\* 1. linia: `n` (`n ≥ 3`)

### Wyjście

`n` linii po `n` znaków.

### Przykład

\**Wejście:**

```
5
```

\**Wyjście:**

```
\*****
   *
  *
 *
\*****
```

-}
main :: IO ()
main = pure ()
