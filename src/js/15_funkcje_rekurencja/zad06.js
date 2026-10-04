/*
ZAD-06 — N-ty wyraz ciągu danego wzorem rekurencyjnym

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `ciągi`

### Treść

Ciąg jest zdefiniowany wzorem rekurencyjnym:

* $a_1 = 1$,
* $a_n = 1 + 2 \cdot a_{n-1}$ dla $n \ge 2$.

Napisz rekurencyjną funkcję `wyraz_ciagu(n)`, która zwraca $a_n$. Program wczytuje $N$ i wypisuje $a_N$.

### Wejście

Jedna liczba naturalna `N` (`N ≥ 1`).

### Wyjście

Jedna liczba naturalna — wartość $a_N$.

### Ograniczenia

* `1 ≤ N ≤ 30`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
31
```

Kolejne wyrazy: $a_1 = 1$, $a_2 = 3$, $a_3 = 7$, $a_4 = 15$, $a_5 = 31$.

### Kod startowy

```python
def wyraz_ciagu(n):
    pass


n = int(input())
print(wyraz_ciagu(n))
```

*/

function ciag(n) {
  if (n === 1) {
    return 1;
  }
  return 1 + 2 * ciag(n - 1);
}

function test() {
  console.assert(ciag(1) === 1, "Test 1 failed");
  console.assert(ciag(2) === 3, "Test 2 failed");
  console.assert(ciag(3) === 7, "Test 3 failed");
  console.assert(ciag(4) === 15, "Test 4 failed");
  console.assert(ciag(5) === 31, "Test 5 failed");
  console.assert(ciag(6) === 63, "Test 6 failed");
  console.assert(ciag(7) === 127, "Test 7 failed");
  console.assert(ciag(8) === 255, "Test 8 failed");
  console.assert(ciag(9) === 511, "Test 9 failed");
  console.assert(ciag(10) === 1023, "Test 10 failed");
  console.assert(ciag(11) === 2047, "Test 11 failed");
}

test();

