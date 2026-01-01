{-
ZAD-08 — Trójkąt Pascala

\**Poziom:** ★★☆
\**Tagi:** `pętle zagnieżdżone`, `listy`, `kombinatoryka`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz trójkąt Pascala o wysokości `n`.

Wiersz 1: `1`
Wiersz 2: `1 1`
Wiersz 3: `1 2 1`
itd.

Liczby w wierszu oddzielaj pojedynczą spacją.

### Wejście

\* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii, w `i`-tej linii jest `i` liczb.

### Przykład

\**Wejście:**

```
3
```

\**Wyjście:**

```
1
1 1
1 2 1
```

### Uwagi o formatowaniu

\* Nie dodawaj spacji na końcu wiersza.

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  let pascal = iterate (\row -> zipWith (+) (0:row) (row ++ [0])) [1]
  mapM_ (putStrLn . unwords . map show) $ take n pascal
