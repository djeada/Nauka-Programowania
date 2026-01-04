/*
ZAD-04A — Minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_dwoch(a, b)`, która zwraca mniejszą z dwóch liczb
naturalnych.

### Wejście

Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)

### Wyjście

Funkcja zwraca:

* `min(a, b)`

### Przykład

**Wywołanie funkcji:**

```python
print(min_z_dwoch(3, 1))
```

**Wyjście:**

```
1
```

ZAD-04B — Maksimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_dwoch(a, b)`, która zwraca większą z dwóch liczb
naturalnych.

### Wejście

Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)

### Wyjście

Funkcja zwraca:

* `max(a, b)`

### Przykład

**Wywołanie funkcji:**

```python
print(max_z_dwoch(3, 1))
```

**Wyjście:**

```
3
```

ZAD-04C — Minimum z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_trzech(a, b, c)`, która zwraca najmniejszą z trzech liczb
naturalnych.

### Wejście

Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)

### Wyjście

Funkcja zwraca:

* `min(a, b, c)`

### Przykład

**Wywołanie funkcji:**

```python
print(min_z_trzech(3, 2, 1))
```

**Wyjście:**

```
1
```

ZAD-04D — Maksimum z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_trzech(a, b, c)`, która zwraca największą z trzech liczb
naturalnych.

### Wejście

Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)

### Wyjście

Funkcja zwraca:

* `max(a, b, c)`

### Przykład

**Wywołanie funkcji:**

```python
print(max_z_trzech(3, 2, 1))
```

**Wyjście:**

```
3
```

*/
#include <iostream>

// ZAD-04A
int min2(int a, int b) { return a < b ? a : b; }

// ZAD-04B
int maks2(int a, int b) { return a > b ? a : b; }

// ZAD-04C
int min3(int a, int b, int c) {
  int minAB = a < b ? a : b;
  return minAB < c ? minAB : c;
}

// ZAD-04D
int maks3(int a, int b, int c) {
  int maksAB = a > b ? a : b;
  return maksAB > c ? maksAB : c;
}

int main() {
  int a, b;
  std::cin >> a >> b;

  std::cout << min2(a, b) << std::endl;
  std::cout << maks2(a, b) << std::endl;

  int c;
  std::cin >> c;
  std::cout << min3(a, b, c) << std::endl;
  std::cout << maks3(a, b, c) << std::endl;

  return 0;
}
