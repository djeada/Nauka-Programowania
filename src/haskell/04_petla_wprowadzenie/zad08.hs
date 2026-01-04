{-
ZAD-08 — Obliczanie liczby kur i owiec na farmie

\**Poziom:** ★★☆
\**Tagi:** `układ równań`, `arytmetyka`

### Treść

Na farmie są kury i owce. Wiadomo, że:

\* łączna liczba głów wynosi `a`,
\* łączna liczba nóg wynosi `b`,
\* kura ma 2 nogi, owca ma 4 nogi,
\* każda ma dokładnie 1 głowę.

Oblicz liczbę kur oraz liczbę owiec.

### Wejście

Dwie liczby naturalne:

\* 1. linia: `a` — liczba głów (`a ≥ 0`)
\* 2. linia: `b` — liczba nóg (`b ≥ 0`)

### Ograniczenia / gwarancje

\* Istnieje rozwiązanie w liczbach całkowitych nieujemnych.

### Wyjście

Dwie liczby naturalne, każda w oddzielnej linii:

1. liczba kur
2. liczba owiec

### Przykład

\**Wejście:**

```
40
100
```

\**Wyjście:**

```
30
10
```

### Uwagi o formatowaniu

\* Nie wypisuj dodatkowych opisów — tylko liczby.

-}
main :: IO ()
main = do
  a <- readLn :: IO Int -- total heads
  b <- readLn :: IO Int -- total legs

  -- System of equations:
  -- chickens + sheep = a
  -- 2*chickens + 4*sheep = b
  -- Solving: chickens = 2*a - b/2, sheep = b/2 - a

  let sheep = (b - 2 * a) `div` 2
  let chickens = a - sheep

  print chickens
  print sheep
