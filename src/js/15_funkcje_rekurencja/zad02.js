/*
ZAD-02 — Suma liczb naturalnych mniejszych od N

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `suma`

### Treść

Napisz rekurencyjną funkcję `suma_mniejszych(n)`, która zwraca sumę wszystkich liczb naturalnych mniejszych od $n$, czyli $0 + 1 + 2 + \dots + (n-1)$.

Program wczytuje $N$ i wypisuje wynik funkcji.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — suma liczb naturalnych mniejszych od `N`. Dla `N = 0` nie ma takich liczb, więc suma wynosi `0`.

### Ograniczenia

* `0 ≤ N ≤ 100`

### Przykład

**Wejście:**

```
10
```

**Wyjście:**

```
45
```

$0 + 1 + 2 + \dots + 9 = 45$ (liczba `10` nie jest mniejsza od `10`).

### Uwagi

* Suma liczb mniejszych od $n$ to $(n-1)$ plus suma liczb mniejszych od $n-1$.

### Kod startowy

```python
def suma_mniejszych(n):
    pass


n = int(input())
print(suma_mniejszych(n))
```

*/

function sumaLiczbMniejszychOdN(n) {
  // Zwraca 0 + 1 + ... + (n - 1).
  if (n <= 1) {
    return 0;
  }
  return n - 1 + sumaLiczbMniejszychOdN(n - 1);
}

function test() {
  console.assert(sumaLiczbMniejszychOdN(0) === 0, "Test 1 failed");
  console.assert(sumaLiczbMniejszychOdN(1) === 0, "Test 2 failed");
  console.assert(sumaLiczbMniejszychOdN(2) === 1, "Test 3 failed");
  console.assert(sumaLiczbMniejszychOdN(5) === 10, "Test 4 failed");
  console.assert(sumaLiczbMniejszychOdN(10) === 45, "Test 5 failed");
  console.assert(sumaLiczbMniejszychOdN(100) === 4950, "Test 6 failed");
}

test();
