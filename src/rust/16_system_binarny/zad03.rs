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

use std::io;

// Funkcja dodawania bitowego
// Złożoność czasowa: O(log(max(a,b)))
// Złożoność pamięciowa: O(1)
fn dodawanie_bitowe(mut a: u32, mut b: u32) -> u32 {
    while b != 0 {
        let przeniesienie = a & b;
        a = a ^ b;
        b = przeniesienie << 1;
    }
    a
}

// Funkcja odejmowania bitowego
// Złożoność czasowa: O(log(max(a,b)))
// Złożoność pamięciowa: O(1)
fn odejmowanie_bitowe(mut a: u32, mut b: u32) -> u32 {
    while b != 0 {
        let pozyczka = (!a) & b;
        a = a ^ b;
        b = pozyczka << 1;
    }
    a
}

fn main() {
    // ZAD-03A: Dodawanie bitowe
    let mut a_str = String::new();
    let mut b_str = String::new();
    
    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");
    io::stdin().read_line(&mut b_str).expect("Błąd wczytywania");
    
    let a: u32 = a_str.trim().parse().unwrap_or(0);
    let b: u32 = b_str.trim().parse().unwrap_or(0);
    
    println!("{}", dodawanie_bitowe(a, b));
    
    // ZAD-03B: Odejmowanie bitowe (opcjonalnie)
    // println!("{}", odejmowanie_bitowe(a, b));
}
