{-
ZAD-01 — Obliczanie średniej z n liczb

\**Poziom:** ★☆☆
\**Tagi:** `pętle`, `suma`, `średnia`, `float`

### Treść

Napisz funkcję `oblicz_srednia()`, która:

1. Wczytuje liczbę naturalną `n` (`n ≥ 1`).
2. Wczytuje następnie `n` liczb (całkowitych lub zmiennoprzecinkowych).
3. Zwraca ich średnią arytmetyczną.

### Wejście

\* 1. linia: `n` (`n ≥ 1`)
\* kolejne `n` linii: liczby (int lub float)

### Wyjście

Funkcja zwraca jedną liczbę zmiennoprzecinkową — średnią arytmetyczną.

### Przykład

\**Wejście:**

```
2
4
6
```

\**Wywołanie funkcji:**

```python
wynik = oblicz_srednia()
print(wynik)
```

\**Wyjście:**

```
5.0
```

### Uwagi o formatowaniu

\* Nie narzucamy liczby miejsc po przecinku — wypisz wynik w domyślnym formacie języka (lub jako `float`).

-}
obliczSrednia :: IO Double
obliczSrednia = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Double) [1 .. n]
  return $ sum nums / fromIntegral n

main :: IO ()
main = do
  wynik <- obliczSrednia
  print wynik
