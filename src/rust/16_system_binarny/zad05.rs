/*
ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, `?:`) i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `min(a, b)`.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
2
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe.

ZAD-05B — Maksimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj `a` i `b`. Wypisz większą z nich **bez użycia instrukcji warunkowych** i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `max(a, b)`.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
3
```

*/

use std::io;

// Funkcja znajdująca minimum bez instrukcji warunkowych
// Złożoność czasowa: O(1)
// Złożoność pamięciowa: O(1)
fn min_bez_if(a: u32, b: u32) -> u32 {
    // Używamy różnicy i operacji bitowych
    let diff = a as i32 - b as i32;
    let znak = diff >> 31; // -1 jeśli a < b, 0 w przeciwnym razie
    (a as i32 & znak | b as i32 & !znak) as u32
}

// Funkcja znajdująca maksimum bez instrukcji warunkowych
// Złożoność czasowa: O(1)
// Złożoność pamięciowa: O(1)
fn max_bez_if(a: u32, b: u32) -> u32 {
    let diff = a as i32 - b as i32;
    let znak = diff >> 31;
    (b as i32 & znak | a as i32 & !znak) as u32
}

fn main() {
    // ZAD-05A: Minimum bez instrukcji warunkowych
    let mut a_str = String::new();
    let mut b_str = String::new();
    
    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");
    io::stdin().read_line(&mut b_str).expect("Błąd wczytywania");
    
    let a: u32 = a_str.trim().parse().unwrap_or(0);
    let b: u32 = b_str.trim().parse().unwrap_or(0);
    
    println!("{}", min_bez_if(a, b));
    
    // ZAD-05B: Maksimum bez instrukcji warunkowych (opcjonalnie)
    // println!("{}", max_bez_if(a, b));
}
