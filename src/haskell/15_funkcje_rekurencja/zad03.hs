{-
ZAD-03 — Potęga

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `potęgowanie`

### Treść

Napisz rekurencyjną funkcję `potega(a, b)`, która zwraca $a^b$, korzystając z zależności $a^0 = 1$ oraz $a^b = a \cdot a^{b-1}$ dla $b \ge 1$.

Program wczytuje $a$ i $b$, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba całkowita (podstawa)
* 2. linia: `b` — liczba naturalna (wykładnik)

### Wyjście

Jedna liczba całkowita — wartość $a^b$. Przyjmujemy, że $0^0 = 1$.

### Ograniczenia

* `-10 ≤ a ≤ 10`
* `0 ≤ b ≤ 18`

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
8
```

### Uwagi

* Nie używaj operatora `**` ani funkcji `pow()` — potęgę ma obliczyć Twoja funkcja.

### Kod startowy

```python
def potega(a, b):
    pass


a = int(input())
b = int(input())
print(potega(a, b))
```

-}

import Control.Monad (unless)

-- Zwraca a^b dla b >= 0.
-- Złożoność czasowa: O(b)
-- Złożoność pamięciowa: O(b) - przez stos rekurencji
potega :: Integer -> Int -> Integer
potega _ 0 = 1
potega a b = a * potega a (b - 1)

main :: IO ()
main = do
  let testy =
        [ potega 2 3 == 8,
          potega 5 0 == 1,
          potega 0 5 == 0,
          potega (-2) 5 == (-32)
        ]
  unless (and testy) $ error "Test nie przeszedl"
  putStrLn "Wszystkie testy zakonczone sukcesem"
