/*
ZAD-04A — Minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_dwoch(a, b)`, która zwraca mniejszą z dwóch liczb naturalnych.

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

Napisz funkcję `max_z_dwoch(a, b)`, która zwraca większą z dwóch liczb naturalnych.

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

Napisz funkcję `min_z_trzech(a, b, c)`, która zwraca najmniejszą z trzech liczb naturalnych.

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

Napisz funkcję `max_z_trzech(a, b, c)`, która zwraca największą z trzech liczb naturalnych.

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

// Funkcja zwracajaca mniejsza liczbe
function zwracajMniejszaLiczbe(liczba_a, liczba_b) {
  if (liczba_a < liczba_b) {
    return liczba_a;
  } else {
    return liczba_b;
  }
}

// Funkcja zwracajaca wieksza liczbe
function zwracajWiekszaLiczbe(liczba_a, liczba_b) {
  if (liczba_a > liczba_b) {
    return liczba_a;
  } else {
    return liczba_b;
  }
}

// Funkcja zwracajaca najmniejsza liczbe
function zwracajNajmniejszaLiczbe(liczba_a, liczba_b, liczba_c) {
  if (liczba_a < liczba_b && liczba_a < liczba_c) {
    return liczba_a;
  } else if (liczba_b < liczba_a && liczba_b < liczba_c) {
    return liczba_b;
  } else {
    return liczba_c;
  }
}

// Funkcja zwracajaca najwieksza liczbe
function zwracajNajwiekszaLiczbe(liczba_a, liczba_b, liczba_c) {
  if (liczba_a > liczba_b && liczba_a > liczba_c) {
    return liczba_a;
  } else if (liczba_b > liczba_a && liczba_b > liczba_c) {
    return liczba_b;
  } else {
    return liczba_c;
  }
}

// Pobieranie danych od uzytkownika
var liczba_a = parseInt(prompt("Podaj pierwsza liczbe: "));
var liczba_b = parseInt(prompt("Podaj druga liczbe: "));
var liczba_c = parseInt(prompt("Podaj trzecia liczbe: "));

// Wyswietlanie wynikow
console.log(zwracajMniejszaLiczbe(liczba_a, liczba_b));
console.log(zwracajWiekszaLiczbe(liczba_a, liczba_b));
console.log(zwracajNajmniejszaLiczbe(liczba_a, liczba_b, liczba_c));
console.log(zwracajNajwiekszaLiczbe(liczba_a, liczba_b, liczba_c));

