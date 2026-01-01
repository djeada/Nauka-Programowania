{-
ZAD-05A — Funkcja liniowa: y = 3x + 10

**Poziom:** ★★☆
**Tagi:** `arytmetyka`, `float`, `formatowanie`

### Wejście

1 liczba: `x` (może być całkowita lub zmiennoprzecinkowa)

### Wyjście

1 liczba: `y` wypisana z dokładnością do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
19.000
```

ZAD-05B — Funkcja liniowa: y = ax + b

**Poziom:** ★★☆
**Tagi:** `arytmetyka`, `float`

### Wejście

3 liczby (każda w osobnej linii): `a`, `b`, `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Przykład

**Wejście:**

```
1
2
3
```

**Wyjście:**

```
5.000
```

ZAD-05C — Funkcja sześcienna: y = x³ + 2

**Poziom:** ★★☆
**Tagi:** `potęgi`, `float`

### Treść

Oblicz: `y = x^3 + 22 - 20`, czyli równoważnie `y = x^3 + 2`.

### Wejście

1 liczba: `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
127.000
```

ZAD-05D — Wielomian z potęgami: y = a·x^m + b·x^n + c − a

**Poziom:** ★★☆
**Tagi:** `potęgi`, `float`

### Wejście

6 liczb (w osobnych liniach): `a`, `b`, `c`, `m`, `n`, `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Ograniczenia / gwarancje

* `m` i `n` są liczbami całkowitymi (np. nieujemnymi), aby potęgowanie było jednoznaczne w typowych językach.

### Przykład

**Wejście:**

```
1
1
1
1
1
1
```

**Wyjście:**

```
2.000
```

ZAD-05E — Funkcja z trygonometrią, wykładniczą i logarytmem

**Poziom:** ★★★☆
**Tagi:** `math`, `trygonometria`, `log`, `exp`, `float`

### Treść

Dla `x` (w radianach) oblicz:
[
y=\sin^3(x)\cdot\cos^2(x)+e^{x^2}+\ln(x^3+2x^2-x-3)
]

### Wejście

1 liczba zmiennoprzecinkowa: `x` (w radianach)

### Wyjście

`y` do 3 miejsc po przecinku.

### Ograniczenia / gwarancje

* Dane testowe spełniają warunek dziedziny logarytmu:

  * (x^3+2x^2-x-3 > 0)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
57.179
```

-}
import Text.Printf (printf)

main :: IO ()
main = do
  x1 <- readLn :: IO Double
  printf "%.3f\n" (3 * x1 + 10)

  a1 <- readLn :: IO Double
  b1 <- readLn :: IO Double
  x2 <- readLn :: IO Double
  printf "%.3f\n" (a1 * x2 + b1)

  x3 <- readLn :: IO Double
  printf "%.3f\n" (x3 ** 3 + 2)

  a2 <- readLn :: IO Double
  b2 <- readLn :: IO Double
  c2 <- readLn :: IO Double
  m <- readLn :: IO Int
  n <- readLn :: IO Int
  x4 <- readLn :: IO Double
  printf "%.3f\n" (a2 * (x4 ** fromIntegral m) + b2 * (x4 ** fromIntegral n) + c2 - a2)

  x5 <- readLn :: IO Double
  let y = (sin x5 ** 3) * (cos x5 ** 2) + exp (x5 ** 2) + log (x5 ** 3 + 2 * x5 ** 2 - x5 - 3)
  printf "%.3f\n" y
