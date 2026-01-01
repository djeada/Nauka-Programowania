{-
ZAD-06 — Najmniejsza wspólna wielokrotność (NWW)

**Poziom:** ★☆☆
**Tagi:** `nww`, `nwd`, `arytmetyka`

### Treść

Napisz funkcję `nww(a, b)`, która zwraca najmniejszą wspólną wielokrotność liczb `a` i `b`.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a > 0`)
* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWW(a, b)`.

### Przykład

**Wywołanie funkcji:**

```python
print(nww(7, 9))
```

**Wyjście:**

```
63
```

### Ograniczenia / gwarancje

* Możesz użyć zależności: `NWW(a, b) = (a * b) // NWD(a, b)`.

-}
main :: IO ()
main = pure ()
