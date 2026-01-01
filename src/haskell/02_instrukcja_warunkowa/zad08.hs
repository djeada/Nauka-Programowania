{-
ZAD-08 — Czy można zbudować trójkąt?

\**Poziom:** ★☆☆
\**Tagi:** `if`, `geometria`, `warunek trójkąta`

### Treść

Wczytaj trzy dodatnie długości odcinków `a`, `b`, `c`.
Sprawdź, czy można z nich zbudować trójkąt.

Wypisz:

\* jeśli tak: `Trójkąt można zbudować z podanych boków.`
\* jeśli nie: `Trójkąta nie można zbudować z podanych boków.`

### Wejście

\* 1 linia: `a` (całkowita, `a > 0`)
\* 2 linia: `b` (całkowita, `b > 0`)
\* 3 linia: `c` (całkowita, `c > 0`)

### Wyjście

Jedna linia — dokładnie jeden z komunikatów.

### Ograniczenia / warunek

Trójkąt istnieje wtedy i tylko wtedy, gdy spełnione są wszystkie:

\* `a + b > c`
\* `a + c > b`
\* `b + c > a`

### Przykład

\**Wejście:**

```
3
4
5
```

\**Wyjście:**

```
Trójkąt można zbudować z podanych boków.
```

-}
main :: IO ()
main = do
  aInput <- getLine
  bInput <- getLine
  cInput <- getLine
  let a = read aInput :: Int
  let b = read bInput :: Int
  let c = read cInput :: Int
  if (a + b > c) && (a + c > b) && (b + c > a)
    then putStrLn "Trójkąt można zbudować z podanych boków."
    else putStrLn "Trójkąta nie można zbudować z podanych boków."
