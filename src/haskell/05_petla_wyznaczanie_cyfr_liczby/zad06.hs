{-
ZAD-06A — Liczby mniejsze od n o sumie cyfr równej 10

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby naturalne `x` takie, że `x < n` i suma cyfr liczby `x` wynosi `10`.

### Wejście

\* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

\**Wejście:**

```
50
```

\**Wyjście:**

```
19
28
37
46
```

### Uwagi

\* Nierówność jest ostra: samej liczby `n` nie wypisujemy, nawet jeśli suma jej cyfr wynosi `10`.

ZAD-06B — Dwucyfrowe większe od n o różnych cyfrach

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `cyfry`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby dwucyfrowe `x` (od `10` do `99`) takie, że `x > n` i cyfra dziesiątek liczby `x` jest **różna** od jej cyfry jedności.

### Wejście

\* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

\**Wejście:**

```
90
```

\**Wyjście:**

```
91
92
93
94
95
96
97
98
```

Liczba `99` jest większa od `90`, ale ma dwie jednakowe cyfry, więc jej nie wypisujemy.

### Uwagi

\* Cyfrę jedności liczby `x` daje `x % 10`, a cyfrę dziesiątek liczby dwucyfrowej — `x // 10`.
\* Nierówność jest ostra: samej liczby `n` nie wypisujemy.
\* Dla `n ≥ 98` żadna liczba nie spełnia warunku.

ZAD-06C — Trzycyfrowe o sumie cyfr równej n

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby trzycyfrowe (od `100` do `999`), których suma cyfr jest równa `n`.

### Wejście

\* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby trzycyfrowe spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

\**Wejście:**

```
3
```

\**Wyjście:**

```
102
111
120
201
210
300
```

### Uwagi

\* Suma cyfr liczby trzycyfrowej wynosi od `1` do `27`, więc dla innych `n` wynik jest pusty.

ZAD-06D — Trzycyfrowe podzielne przez sumę cyfr liczby n

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `dzielenie`, `suma cyfr`

### Treść

Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr `s`. Następnie wypisz w kolejności rosnącej wszystkie liczby trzycyfrowe (od `100` do `999`), które są podzielne przez `s`.

### Wejście

\* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Liczby trzycyfrowe podzielne przez `s`, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Ograniczenia

\* `n ≥ 1`, więc `s ≥ 1` i dzielenie jest zawsze wykonalne.

### Przykład

\**Wejście:**

```
9999999
```

\**Wyjście:**

```
126
189
252
315
378
441
504
567
630
693
756
819
882
945
```

Suma cyfr to $s = 7 \cdot 9 = 63$, a wypisane liczby to kolejne trzycyfrowe wielokrotności `63`.

ZAD-06E — Mniejsze od n złożone wyłącznie z parzystych cyfr

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `warunki`, `cyfry`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby naturalne `x` takie, że `1 ≤ x < n` i **każda** cyfra liczby `x` jest parzysta.

### Wejście

\* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

\**Wejście:**

```
50
```

\**Wyjście:**

```
2
4
6
8
20
22
24
26
28
40
42
44
46
48
```

### Uwagi

\* `0` jest cyfrą parzystą, więc np. `20` i `40` spełniają warunek.
\* Samą liczbę `0` pomijamy (zaczynamy od `x = 1`).

-}
main :: IO ()
main = do
  n <- readLn :: IO Int

  let sumDigits num = sum $ map (\c -> read [c] :: Int) $ show num
  let allDigitsEven num = all even $ map (\c -> read [c] :: Int) $ show num

  -- ZAD-06A: liczby mniejsze od n o sumie cyfr równej 10
  mapM_ print [x | x <- [0 .. n - 1], sumDigits x == 10]

  -- ZAD-06B: dwucyfrowe większe od n o różnych cyfrach
  mapM_ print [x | x <- [10 .. 99], x > n, x `div` 10 /= x `mod` 10]

  -- ZAD-06C: trzycyfrowe o sumie cyfr równej n
  mapM_ print [x | x <- [100 .. 999], sumDigits x == n]

  -- ZAD-06D: trzycyfrowe podzielne przez sumę cyfr liczby n
  let s = sumDigits n
  if s > 0
    then mapM_ print [x | x <- [100 .. 999], x `mod` s == 0]
    else return ()

  -- ZAD-06E: mniejsze od n złożone wyłącznie z parzystych cyfr
  mapM_ print [x | x <- [2 .. n - 1], x > 0, allDigitsEven x]
