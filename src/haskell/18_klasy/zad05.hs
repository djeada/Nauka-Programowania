{-
ZAD-05 — Klasa Macierz

\**Poziom:** ★★☆
\**Tagi:** `class`, `macierze`, `operacje`

### Treść

Zaprojektuj klasę **Macierz**:

1. Konstruktor przyjmuje listę list (domyślnie pusta).
2. Operacje: dodawanie, odejmowanie, mnożenie.
3. Metoda wypisująca macierz (wierszami).
4. Porównania `==` i `!=`.

(Operację odwracania możesz pominąć w tym zadaniu, jeśli nie jest wymagana w sprawdzarce; najczęściej w podstawowych zadaniach nie ma testów na odwracanie.)

Program tworzy:

\* A = [[1, 3], [4, 2]]
\* B = [[5, 0], [1, 3]]

Wypisuje A, B, a potem A+B, A-B, A*B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

\**Wyjście:**

```
Macierz A:
[1, 3]
[4, 2]

Macierz B:
[5, 0]
[1, 3]

Suma macierzy:
[6, 3]
[5, 5]

Różnica macierzy A - B:
[-4, 3]
[3, -1]

Iloczyn macierzy A * B:
[8, 9]
[22, 12]
```

-}

data Macierz = Macierz {dane :: [[Int]]} deriving (Eq)

-- Dodawanie macierzy
-- Złożoność czasowa: O(n*m)
dodajMacierz :: Macierz -> Macierz -> Macierz
dodajMacierz (Macierz a) (Macierz b) = Macierz $ zipWith (zipWith (+)) a b

-- Wypisuje macierz
wypiszMacierz :: Macierz -> IO ()
wypiszMacierz (Macierz rows) = mapM_ print rows

main :: IO ()
main = do
  let a = Macierz [[1, 3], [4, 2]]
  let b = Macierz [[2, 1], [0, 5]]
  putStrLn "Macierz A:"
  wypiszMacierz a
  putStrLn "Macierz B:"
  wypiszMacierz b
  putStrLn "Suma A + B:"
  wypiszMacierz (dodajMacierz a b)
