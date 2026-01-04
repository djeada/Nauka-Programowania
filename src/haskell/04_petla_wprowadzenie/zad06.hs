{-
ZAD-06 — Sumowanie elementów ciągu

\**Poziom:** ★☆☆
\**Tagi:** `ciągi`, `sumowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`) i oblicz:

a) ( \sum_{k=1}^{n} (k^2 + k + 1) )

b) ( \sum_{k=1}^{n} (k^2 + 5k) )

c) ( \sum_{k=1}^{n} (k + 2k) )  (czyli ( \sum_{k=1}^{n} 3k ))

Wypisz trzy sumy w kolejności a), b), c).

### Wejście

Jedna liczba naturalna:

\* 1. linia: `n` (`n ≥ 1`)

### Wyjście

Trzy liczby naturalne — każda w oddzielnej linii:

1. suma dla (a)
2. suma dla (b)
3. suma dla (c)

### Przykład

\**Wejście:**

```
2
```

\**Wyjście:**

```
10
16
9
```

### Uwagi o formatowaniu

\* Wyniki są liczbami całkowitymi — nie stosuj żadnego dodatkowego zaokrąglania.

-}
main :: IO ()
main = do
  n <- readLn :: IO Int

  -- a) sum of (k^2 + k + 1) for k from 1 to n
  let sumA = sum [k * k + k + 1 | k <- [1 .. n]]

  -- b) sum of (k^2 + 5k) for k from 1 to n
  let sumB = sum [k * k + 5 * k | k <- [1 .. n]]

  -- c) sum of (k + 2k) = sum of 3k for k from 1 to n
  let sumC = sum [3 * k | k <- [1 .. n]]

  print sumA
  print sumB
  print sumC
