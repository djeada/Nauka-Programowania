{-
ZAD-05 — Zmodyfikuj elementy spełniające warunek

\**Poziom:** ★☆☆
\**Tagi:** `listy`, `warunki`, `liczby pierwsze`

### Treść

Wczytaj listę liczb całkowitych. Dla każdego podpunktu utwórz **nową listę** na podstawie listy z poprzedniego podpunktu i wypisz ją w jednej linii (przecinki bez spacji):

a) Zwiększ o 1 elementy o **parzystych indeksach** (0,2,4,...).
b) Ustaw na `0` elementy będące **wielokrotnością 3**.
c) Podnieś do kwadratu elementy **mniejsze niż 10**.
d) Oblicz sumę wszystkich elementów listy i wstaw tę sumę na indeksy, które są **liczbami pierwszymi** (2,3,5,7,11,...) — tylko te, które mieszczą się w zakresie listy.
e) Zamień każdy element na **iloczyn wszystkich pozostałych elementów** listy.

### Wejście

\* 1. linia: `N` (`N ≥ 1`)
\* kolejne `N` linii: liczby całkowite

### Wyjście

Pięć linii (po kolei: a, b, c, d, e), w każdej lista oddzielona przecinkami.

### Przykład

\**Wejście:**

```
5
5
7
9
4
2
```

\**Wyjście:**

```
6,7,10,4,3
6,7,0,4,3
36,49,0,16,9
36,49,36,36,9
0,0,0,0,0
```

### Uwagi o formatowaniu

\* W podpunkcie (d) indeks 0 i 1 nie są pierwsze.
\* W podpunkcie (e) jeśli w liście jest `0`, to wiele wyników będzie `0` — to normalne.
\* Nie dodawaj przecinków na końcu linii.

-}
main :: IO ()
main = do
  n <- readLn :: IO Int
  nums <- mapM (\_ -> readLn :: IO Int) [1 .. n]

  let isPrime x = x > 1 && null [d | d <- [2 .. floor (sqrt (fromIntegral x))], x `mod` d == 0]
  let intercalate sep [] = ""
      intercalate sep [x] = x
      intercalate sep (x : xs) = x ++ sep ++ intercalate sep xs

  -- a) Zwiększ o 1 elementy o parzystych indeksach
  let resA = zipWith (\i x -> if even i then x + 1 else x) [0 ..] nums
  putStrLn $ intercalate "," $ map show resA

  -- b) Ustaw na 0 elementy będące wielokrotnością 3
  let resB = map (\x -> if x `mod` 3 == 0 && x /= 0 then 0 else x) resA
  putStrLn $ intercalate "," $ map show resB

  -- c) Podnieś do kwadratu elementy mniejsze niż 10
  let resC = map (\x -> if x < 10 then x * x else x) resB
  putStrLn $ intercalate "," $ map show resC

  -- d) Wstaw sumę na indeksy będące liczbami pierwszymi
  let s = sum resC
  let resD = zipWith (\i x -> if isPrime i then s else x) [0 ..] resC
  putStrLn $ intercalate "," $ map show resD

  -- e) Zamień każdy element na iloczyn wszystkich pozostałych
  let totalProduct = product resD
  let resE = map (\x -> if x == 0 then 0 else totalProduct `div` x) resD
  putStrLn $ intercalate "," $ map show resE
