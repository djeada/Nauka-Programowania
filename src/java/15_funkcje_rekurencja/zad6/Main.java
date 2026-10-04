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

public class Main {

  // Zlozonosc Czasowa: O(n)
  // Zlozonosc Pamieciowa: O(n) - rekurencja uzywa stosu
  public static long wyrazCiagu(int n) {
    // a_1 = 1, a_n = 1 + 2 * a_(n-1)
    if (n == 1) {
      return 1;
    }

    return 1 + 2 * wyrazCiagu(n - 1);
  }

  public static void test1() {
    assert wyrazCiagu(1) == 1;
    assert wyrazCiagu(5) == 31;
    assert wyrazCiagu(10) == 1023;
    assert wyrazCiagu(30) == 1073741823L;
  }

  public static void main(String[] args) {

    test1();
  }
}
