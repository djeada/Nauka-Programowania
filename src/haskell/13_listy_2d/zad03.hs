{-
ZAD-03 — Macierz 2-kolumnowa z dwóch list

\**Poziom:** ★☆☆
\**Tagi:** `listy`, `macierze`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, wypisz macierz 2-kolumnową: wiersz `i` to `(lista1[i], lista2[i])`.
Jeśli długości są różne, wypisz: `Pusta macierz`

### Wejście

\* 1. linia: `n`
\* 2. linia: `m`
\* następnie `n` liczb (pierwsza lista)
\* następnie `m` liczb (druga lista)

### Wyjście

\* Jeśli `n = m`: `n` wierszy `x y`
\* Jeśli `n ≠ m`: jedna linia `Pusta macierz`

### Przykład

\**Wejście:**

```
3
3
3
5
2
2
8
1
```

\**Wyjście:**

```
3 2
5 8
2 1
```

-}

main :: IO ()
main = do
    n <- readLn :: IO Int
    m <- readLn :: IO Int
    lista1 <- sequence [readLn :: IO Int | _ <- [1..n]]
    lista2 <- sequence [readLn :: IO Int | _ <- [1..m]]
    if n /= m
        then putStrLn "Pusta macierz"
        else mapM_ (\(x, y) -> putStrLn $ show x ++ " " ++ show y) $ zip lista1 lista2
