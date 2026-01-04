/*
ZAD-02 — Potęgowanie liczby przy pomocy pętli

**Poziom:** ★☆☆
**Tagi:** `pętle`, `potęgowanie`, `mnożenie`

### Treść

Napisz funkcję `potega(a, b)`, która oblicza `a^b` przy użyciu pętli (bez
operatora potęgowania).

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — wartość `a^b`.

### Przykład

**Wywołanie funkcji:**

```python
print(potega(3, 5))
```

**Wyjście:**

```
243
```

### Uwagi o formatowaniu

* Dla `b = 0` wynik ma wynosić `1`.

*/
#include <iostream>

int potega(int a, int b) {
  int wynik = 1;
  for (int i = 0; i < b; i++) {
    wynik *= a;
  }
  return wynik;
}

int main() {
  int a, b;
  std::cin >> a >> b;

  std::cout << potega(a, b) << std::endl;

  return 0;
}
