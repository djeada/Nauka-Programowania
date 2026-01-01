{-
ZAD-05 — Zamiana wartości miejscami

\**Poziom:** ★☆☆
\**Tagi:** `funkcje`, `krotka`, `zmienne`

### Treść

Napisz funkcję `zamien_wartosci(a, b)`, która zamienia wartości miejscami i zwraca je jako parę `(b, a)`.

### Wejście

Dwa argumenty: `a`, `b` (liczby naturalne)

### Wyjście

Dwie liczby naturalne zwrócone jako krotka / para:

\* najpierw nowa wartość `a` (czyli stare `b`)
\* potem nowa wartość `b` (czyli stare `a`)

### Przykład

\**Wywołanie funkcji:**

```python
a, b = zamien_wartosci(8, 5)
print("a =", a)
print("b =", b)
```

\**Wyjście:**

```
a = 5
b = 8
```

-}
zamienWartosci :: Int -> Int -> (Int, Int)
zamienWartosci a b = (b, a)

main :: IO ()
main = do
  let (a, b) = zamienWartosci 8 5
  putStrLn $ "a = " ++ show a
  putStrLn $ "b = " ++ show b
