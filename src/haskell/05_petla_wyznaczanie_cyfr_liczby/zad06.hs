{-
ZAD-06A — Liczby mniejsze od n o sumie cyfr równej 10

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby naturalne `x` takie, że `0 ≤ x < n` oraz suma cyfr liczby `x` wynosi `10`. Każdą liczbę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

\* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w nowej linii.
Jeśli brak — brak wyjścia.

ZAD-06B — Dwucyfrowe większe od n

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `przedziały`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby **dwucyfrowe** większe od `n` (czyli z zakresu 10–99), każdą w osobnej linii.

### Wejście

Jedna liczba naturalna:

\* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Liczby dwucyfrowe `x` takie, że `x > n`, każda w nowej linii.
Jeśli brak — brak wyjścia.

### Przykład (dla n = 95)

\**Wejście:**

```
95
```

\**Wyjście:**

```
96
97
98
99
```

ZAD-06C — Trzycyfrowe o sumie cyfr równej n

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby trzycyfrowe `x` (100–999), których suma cyfr jest równa `n`. Każdą liczbę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

\* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Liczby trzycyfrowe spełniające warunek, każda w nowej linii.
Jeśli brak — brak wyjścia.

ZAD-06D — Trzycyfrowe podzielne przez sumę cyfr liczby n

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `dzielenie`, `suma cyfr`

### Treść

Wczytaj liczbę naturalną `n`. Oblicz sumę cyfr liczby `n` i oznacz ją jako `s`. Następnie wypisz wszystkie liczby trzycyfrowe `x` (100–999), które są podzielne przez `s`. Każdą liczbę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

\* 1. linia: `n` (`n ≥ 0`)

### Ograniczenia / gwarancje

\* Suma cyfr `n` jest większa od zera (czyli `n ≠ 0`), aby dzielenie było poprawne.

### Wyjście

Liczby trzycyfrowe podzielne przez `s`, każda w nowej linii.

ZAD-06E — Mniejsze od n złożone wyłącznie z parzystych cyfr

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `warunki`, `cyfry`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby naturalne `x` takie, że `0 ≤ x < n` oraz każda cyfra w zapisie dziesiętnym `x` jest parzysta. Każdą liczbę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

\* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w nowej linii.
Jeśli brak — brak wyjścia.

### Przykład (dla n = 95)

\**Wejście:**

```
95
```

\**Wyjście:**

```
2
4
6
8
22
24
26
28
42
44
46
48
62
64
66
68
82
84
86
88
```

### Uwagi o formatowaniu

\* W tym zadaniu `0` też składa się wyłącznie z parzystych cyfr. Jeśli chcesz je uwzględniać, dopisz to jako regułę w treści (tu: pomijamy `0`, bo w przykładzie go nie ma).

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  
  let sumDigits num = sum $ map (\c -> read [c] :: Int) $ show num
  let allDigitsEven num = all even $ map (\c -> read [c] :: Int) $ show num
  
  -- ZAD-06A: liczby mniejsze od n o sumie cyfr równej 10
  mapM_ print [x | x <- [0..n-1], sumDigits x == 10]
  
  -- ZAD-06B: dwucyfrowe większe od n
  mapM_ print [x | x <- [10..99], x > n]
  
  -- ZAD-06C: trzycyfrowe o sumie cyfr równej n
  mapM_ print [x | x <- [100..999], sumDigits x == n]
  
  -- ZAD-06D: trzycyfrowe podzielne przez sumę cyfr liczby n
  let s = sumDigits n
  if s > 0
    then mapM_ print [x | x <- [100..999], x `mod` s == 0]
    else return ()
  
  -- ZAD-06E: mniejsze od n złożone wyłącznie z parzystych cyfr
  mapM_ print [x | x <- [2..n-1], x > 0, allDigitsEven x]
