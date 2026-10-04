/*
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

*/

function potega(a, b) {
  if (b === 0) {
    return 1;
  }
  return a * potega(a, b - 1);
}

function test() {
  console.assert(potega(2, 0) === 1, "Test 1 failed");
  console.assert(potega(2, 1) === 2, "Test 2 failed");
  console.assert(potega(2, 2) === 4, "Test 3 failed");
  console.assert(potega(2, 3) === 8, "Test 4 failed");
  console.assert(potega(2, 4) === 16, "Test 5 failed");
  console.assert(potega(2, 5) === 32, "Test 6 failed");
  console.assert(potega(2, 6) === 64, "Test 7 failed");
  console.assert(potega(2, 7) === 128, "Test 8 failed");
  console.assert(potega(2, 8) === 256, "Test 9 failed");
  console.assert(potega(2, 9) === 512, "Test 10 failed");
  console.assert(potega(2, 10) === 1024, "Test 11 failed");
}

test();

