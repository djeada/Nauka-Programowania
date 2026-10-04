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

fn potega(a: i64, b: u32) -> i64 {
    // Zwraca a^b.
    // Złożoność czasowa: O(b)
    // Złożoność pamięciowa: O(b) - przez stos rekurencji
    if b == 0 {
        return 1;
    }

    a * potega(a, b - 1)
}

fn test_potega() {
    assert_eq!(potega(2, 3), 8);
    assert_eq!(potega(5, 0), 1);
    assert_eq!(potega(0, 5), 0);
    assert_eq!(potega(-2, 5), -32);
    assert_eq!(potega(10, 18), 1_000_000_000_000_000_000);
}

fn main() {
    test_potega();
}
