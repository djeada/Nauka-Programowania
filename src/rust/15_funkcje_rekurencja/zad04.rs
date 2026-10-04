/*
ZAD-04 — Silnia

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `silnia`

### Treść

Napisz rekurencyjną funkcję `silnia(n)`, która zwraca $n! = 1 \cdot 2 \cdot \ldots \cdot n$, korzystając z zależności $0! = 1$ oraz $n! = n \cdot (n-1)!$ dla $n \ge 1$.

Program wczytuje $N$ i wypisuje $N!$.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — wartość $N!$.

### Ograniczenia

* `0 ≤ N ≤ 20`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
6
```

$3! = 3 \cdot 2 \cdot 1 = 6$.

### Kod startowy

```python
def silnia(n):
    pass


n = int(input())
print(silnia(n))
```

*/

fn silnia(n: u64) -> u64 {
    // Zwraca n!.
    // Złożoność czasowa: O(n)
    // Złożoność pamięciowa: O(n) - przez stos rekurencji
    if n == 0 {
        return 1;
    }

    n * silnia(n - 1)
}

fn test_silnia() {
    assert_eq!(silnia(0), 1);
    assert_eq!(silnia(3), 6);
    assert_eq!(silnia(10), 3_628_800);
    assert_eq!(silnia(20), 2_432_902_008_176_640_000);
}

fn main() {
    test_silnia();
}
