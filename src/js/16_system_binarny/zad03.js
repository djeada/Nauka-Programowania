/*
ZAD-03A — Dodawanie bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `XOR`, `AND`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz `a + b` używając wyłącznie operatorów bitowych (i przesunięć).

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a + b`.

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
5
```

ZAD-03B — Odejmowanie bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `pożyczki`, `XOR`

### Treść

Wczytaj `a` i `b`. Oblicz `a - b` używając wyłącznie operatorów bitowych.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a - b`.

### Ograniczenia / gwarancje

* Zakładamy, że `a ≥ b` (wynik jest naturalny).

### Przykład

**Wejście:**

```
7
5
```

**Wyjście:**

```
2
```

ZAD-03C — Mnożenie bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `shift`, `pętle`

### Treść

Wczytaj `a` i `b`. Oblicz `a * b` używając wyłącznie operatorów bitowych (np. metoda „shift-and-add”).

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a * b`.

### Przykład

**Wejście:**

```
4
4
```

**Wyjście:**

```
16
```

ZAD-03D — Dzielenie całkowite bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `dzielenie`, `shift`

### Treść

Wczytaj `a` i `b`. Oblicz `a // b` używając wyłącznie operatorów bitowych.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Jedna liczba naturalna: `a // b`.

### Przykład

**Wejście:**

```
9
3
```

**Wyjście:**

```
3
```

*/

// Dodawanie
function dodaj(a, b) {
  while (b != 0) {
    let carry = a & b;
    a = a ^ b;
    b = carry << 1;
  }
  return a;
}

// Odejmowanie
function odejmij(a, b) {
  while (b != 0) {
    let borrow = ~a & b;
    a = a ^ b;
    b = borrow << 1;
  }
  return a;
}

// Mnozenie
function pomnoz(a, b) {
  let wynik = 0;
  while (b != 0) {
    if (b & 1) {
      wynik = dodaj(wynik, a);
    }
    a <<= 1;
    b >>= 1;
  }
  return wynik;
}

// Testy
function test() {
  let a = 2;
  let b = 3;
  console.assert(dodaj(a, b) === a + b, "Niepoprawny wynik dodawania");
  console.assert(odejmij(a, b) === a - b, "Niepoprawny wynik odejmowania");
  console.assert(pomnoz(a, b) === a * b, "Niepoprawny wynik mnozenia");
}

test();

