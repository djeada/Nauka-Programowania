{-
ZAD-04A — Minimum z dwóch liczb

\**Poziom:** ★☆☆
\**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_dwoch(a, b)`, która zwraca mniejszą z dwóch liczb naturalnych.

### Wejście

Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)

### Wyjście

Funkcja zwraca:

\* `min(a, b)`

### Przykład

\**Wywołanie funkcji:**

```python
print(min_z_dwoch(3, 1))
```

\**Wyjście:**

```
1
```

ZAD-04B — Maksimum z dwóch liczb

\**Poziom:** ★☆☆
\**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_dwoch(a, b)`, która zwraca większą z dwóch liczb naturalnych.

### Wejście

Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)

### Wyjście

Funkcja zwraca:

\* `max(a, b)`

### Przykład

\**Wywołanie funkcji:**

```python
print(max_z_dwoch(3, 1))
```

\**Wyjście:**

```
3
```

ZAD-04C — Minimum z trzech liczb

\**Poziom:** ★☆☆
\**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_trzech(a, b, c)`, która zwraca najmniejszą z trzech liczb naturalnych.

### Wejście

Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)

### Wyjście

Funkcja zwraca:

\* `min(a, b, c)`

### Przykład

\**Wywołanie funkcji:**

```python
print(min_z_trzech(3, 2, 1))
```

\**Wyjście:**

```
1
```

ZAD-04D — Maksimum z trzech liczb

\**Poziom:** ★☆☆
\**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_trzech(a, b, c)`, która zwraca największą z trzech liczb naturalnych.

### Wejście

Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)

### Wyjście

Funkcja zwraca:

\* `max(a, b, c)`

### Przykład

\**Wywołanie funkcji:**

```python
print(max_z_trzech(3, 2, 1))
```

\**Wyjście:**

```
3
```

-}
minZDwoch :: Int -> Int -> Int
minZDwoch = min

-- ZAD-04B: Maksimum z dwóch liczb
maxZDwoch :: Int -> Int -> Int
maxZDwoch = max

-- ZAD-04C: Minimum z trzech liczb
minZTrzech :: Int -> Int -> Int -> Int
minZTrzech a b c = minimum [a, b, c]

-- ZAD-04D: Maksimum z trzech liczb
maxZTrzech :: Int -> Int -> Int -> Int
maxZTrzech a b c = maximum [a, b, c]

main :: IO ()
main = do
  print $ minZDwoch 3 1
  print $ maxZDwoch 3 1
  print $ minZTrzech 3 2 1
  print $ maxZTrzech 3 2 1
