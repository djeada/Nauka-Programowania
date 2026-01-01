/*
ZAD-02A — Suma dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `suma(a, b)`, która zwraca sumę dwóch liczb całkowitych.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita)
* `b` (liczba całkowita)

### Wyjście

Funkcja zwraca:

* `a + b`

### Przykład

**Wywołanie funkcji:**

```python
print(suma(3, 5))
```

**Wyjście:**

```
8
```

ZAD-02B — Różnica: b − a

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `roznica(a, b)`, która zwraca różnicę: `b - a`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Wyjście

Funkcja zwraca:

* `b - a`

### Przykład

**Wywołanie funkcji:**

```python
print(roznica(3, 5))
```

**Wyjście:**

```
2
```

ZAD-02C — Iloczyn dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `iloczyn(a, b)`, która zwraca iloczyn `a * b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Wyjście

Funkcja zwraca:

* `a * b`

### Przykład

**Wywołanie funkcji:**

```python
print(iloczyn(3, 5))
```

**Wyjście:**

```
15
```

ZAD-02D — Iloraz całkowity: a // b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `dzielenie`, `//`

### Treść

Napisz funkcję `iloraz(a, b)`, która zwraca iloraz całkowity `a // b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Ograniczenia / gwarancje

* `b ≠ 0`

### Wyjście

Funkcja zwraca:

* `a // b`

### Przykład

**Wywołanie funkcji:**

```python
print(iloraz(3, 5))
```

**Wyjście:**

```
0
```

ZAD-02E — Reszta z dzielenia: a % b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `modulo`, `%`

### Treść

Napisz funkcję `reszta(a, b)`, która zwraca resztę z dzielenia `a % b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Ograniczenia / gwarancje

* `b ≠ 0`

### Wyjście

Funkcja zwraca:

* `a % b`

### Przykład

**Wywołanie funkcji:**

```python
print(reszta(3, 5))
```

**Wyjście:**

```
3
```

*/
#include <cassert>
#include <string>

int suma(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba + drugaLiczba;
}

int roznica(int pierwszaLiczba, int drugaLiczba) {
  return drugaLiczba - pierwszaLiczba;
}

int iloczyn(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba * drugaLiczba;
}

int reszta(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba % drugaLiczba;
}

void testSuma() {
  assert(suma(1, 2) == 3);
  assert(suma(2, 2) == 4);
}

void testRoznica() {
  assert(roznica(1, 2) == -1);
  assert(roznica(2, 2) == 0);
}

void testIloczyn() {
  assert(iloczyn(1, 2) == 2);
  assert(iloczyn(2, 2) == 4);
}

void testReszta() {
  assert(reszta(1, 2) == 1);
  assert(reszta(2, 2) == 0);
}

int main() {
  testSuma();
  testRoznica();
  testIloczyn();
  testReszta();

  return 0;
}
