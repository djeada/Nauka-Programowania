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

public class Main {

  // Zlozonosc Czasowa: O(2^n) - bez memoizacji
  // Zlozonosc Pamieciowa: O(n) - rekurencja uzywa stosu
  public static int fibonacciV1(int n) {

    if (n == 0 || n == 1) {
      return n;
    }

    return fibonacciV1(n - 1) + fibonacciV1(n - 2);
  }

  public static int[] fibonacciV2Pom = new int[256];

  // Zlozonosc Czasowa: O(n) - z memoizacja
  // Zlozonosc Pamieciowa: O(n)
  public static int fibonacciV2(int n) {

    if (n == 0 || n == 1) {
      return n;
    }

    if (fibonacciV2Pom[n] != 0) {
      return fibonacciV2Pom[n];
    }

    fibonacciV2Pom[n] = fibonacciV2(n - 1) + fibonacciV2(n - 2);

    return fibonacciV2Pom[n];
  }

  public static void test1() {
    assert fibonacciV1(0) == 0;
    assert fibonacciV1(1) == 1;
    assert fibonacciV1(7) == 13;
    assert fibonacciV1(20) == 6765;

    assert fibonacciV2(7) == 13;
    assert fibonacciV2(25) == 75025;
  }

  public static void main(String[] args) {

    test1();
  }
}
