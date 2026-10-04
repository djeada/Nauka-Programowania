/*
ZAD-05 — Liczba Fibonacciego

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `Fibonacci`

### Treść

Napisz rekurencyjną funkcję `fibonacci(n)`, która zwraca $n$-ty wyraz ciągu Fibonacciego, zdefiniowanego następująco:

* $F_0 = 0$,
* $F_1 = 1$,
* $F_n = F_{n-1} + F_{n-2}$ dla $n \ge 2$.

Program wczytuje $N$ i wypisuje $F_N$.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — wartość $F_N$.

### Ograniczenia

* `0 ≤ N ≤ 25`

### Przykład

**Wejście:**

```
7
```

**Wyjście:**

```
13
```

Kolejne wyrazy ciągu to `0, 1, 1, 2, 3, 5, 8, 13, …`, a wyraz o numerze `7` (licząc od zera) to `13`.

### Uwagi

* Funkcja ma dwa przypadki bazowe ($n = 0$ i $n = 1$) i wywołuje samą siebie dwa razy.
* Ta prosta wersja wykonuje bardzo dużo powtórzonych obliczeń (liczba wywołań rośnie wykładniczo), ale dla $N \le 25$ działa wystarczająco szybko.

### Kod startowy

```python
def fibonacci(n):
    pass


n = int(input())
print(fibonacci(n))
```

*/

function fib(n) {
  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }
  return fib(n - 1) + fib(n - 2);
}

function test() {
  console.assert(fib(0) === 0, "Test 1 failed");
  console.assert(fib(1) === 1, "Test 2 failed");
  console.assert(fib(2) === 1, "Test 3 failed");
  console.assert(fib(3) === 2, "Test 4 failed");
  console.assert(fib(4) === 3, "Test 5 failed");
  console.assert(fib(5) === 5, "Test 6 failed");
  console.assert(fib(6) === 8, "Test 7 failed");
  console.assert(fib(7) === 13, "Test 8 failed");
  console.assert(fib(8) === 21, "Test 9 failed");
  console.assert(fib(9) === 34, "Test 10 failed");
  console.assert(fib(10) === 55, "Test 11 failed");
}

test();

