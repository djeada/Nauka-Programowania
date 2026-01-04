/*
ZAD-03A — Mnożenie przy pomocy dodawania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `dodawanie`, `mnożenie`

### Treść

Napisz funkcję `iloczyn(a, b)`, która oblicza `a * b` używając **tylko
dodawania** i pętli.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `a * b`.

### Przykład

**Wywołanie funkcji:**

```python
print(iloczyn(3, 2))
```

**Wyjście:**

```
6
```

ZAD-03B — Dzielenie całkowite przy pomocy odejmowania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `odejmowanie`, `dzielenie`

### Treść

Napisz funkcję `iloraz(a, b)`, która oblicza `a // b` używając **tylko
odejmowania** i pętli.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna)

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `a // b`.

### Przykład

**Wywołanie funkcji:**

```python
print(iloraz(3, 2))
```

**Wyjście:**

```
1
```

*/
#include <iostream>

// ZAD-03A
int iloczyn(int a, int b) {
  int wynik = 0;
  for (int i = 0; i < b; i++) {
    wynik += a;
  }
  return wynik;
}

// ZAD-03B
int iloraz(int a, int b) {
  int wynik = 0;
  while (a >= b) {
    a -= b;
    wynik++;
  }
  return wynik;
}

int main() {
  int a, b;
  std::cin >> a >> b;

  std::cout << iloczyn(a, b) << std::endl;
  std::cout << iloraz(a, b) << std::endl;

  return 0;
}
