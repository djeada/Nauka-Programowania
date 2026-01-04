{-
ZAD-09 — N pierwszych liczb pierwszych

\**Poziom:** ★★☆
\**Tagi:** `pętle`, `pierwszość`, `wydajność`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`) i wypisz pierwsze `N` liczb pierwszych w **jednej linii**, oddzielone pojedynczą spacją.

### Wejście

\* 1. linia: `N` (`N ≥ 1`)

### Wyjście

Jedna linia: `N` liczb pierwszych oddzielonych spacjami.

### Przykład

\**Wejście:**

```
5
```

\**Wyjście:**

```
2 3 5 7 11
```

### Uwagi o formatowaniu

\* Nie dodawaj spacji na końcu linii.
\* Do sprawdzania pierwszości wystarczy test dzielnikami do `⌊sqrt(x)⌋`.

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  let isPrime x = x > 1 && null [d | d <- [2 .. floor (sqrt (fromIntegral x))], x `mod` d == 0]
  let primes = filter isPrime [2 ..]
  putStrLn $ unwords $ map show $ take n primes
