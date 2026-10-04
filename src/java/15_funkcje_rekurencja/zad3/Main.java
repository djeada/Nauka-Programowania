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

public class Main {

  // Zlozonosc Czasowa: O(b)
  // Zlozonosc Pamieciowa: O(b) - rekurencja uzywa stosu
  public static long potega(long a, int b) {
    // Zwraca a^b dla b >= 0.
    if (b == 0) {
      return 1;
    }

    return a * potega(a, b - 1);
  }

  public static void test1() {
    assert potega(2, 3) == 8;
    assert potega(3, 2) == 9;
    assert potega(5, 0) == 1;
    assert potega(-2, 5) == -32;
  }

  public static void main(String[] args) {

    test1();
  }
}
