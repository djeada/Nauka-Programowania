/*
ZAD-06 — Konwersja między dowolnymi systemami (2..36)

**Poziom:** ★★☆
**Tagi:** `konwersja`, `base`, `string`

### Treść

Wczytaj:

1. liczbę `X` zapisaną w systemie o podstawie `p`
2. podstawę `p` (2..36)
3. podstawę docelową `q` (2..36)

i wypisz reprezentację `X` w systemie o podstawie `q`.

### Wejście

Trzy linie:

1. `X` (zapis liczby; dla podstaw >10 może zawierać litery `A-Z`)
2. `p` (2..36)
3. `q` (2..36)

### Wyjście

Jedna linia: zapis liczby w systemie o podstawie `q` (używaj `0–9` i `A–Z`).

### Przykład

**Wejście:**

```
4301
10
4
```

**Wyjście:**

```
1003031
```

### Uwagi o formacie

* `X` może być duże — traktuj jako napis, a nie typ int „na wejściu”.
* Dla wartości 10..35 stosuj `A..Z`.

*/

use std::io;

// Funkcja konwertująca liczbę między podstawami liczbowymi
// Złożoność czasowa: O(n), gdzie n to długość reprezentacji
// Złożoność pamięciowa: O(n)
fn konwertuj_podstawe(x_str: &str, p: u32, q: u32) -> String {
    // Konwertuj z podstawy p do dziesiętnej
    let mut dziesietna: u64 = 0;
    
    for c in x_str.chars() {
        let cyfra = if c.is_digit(10) {
            c.to_digit(10).unwrap()
        } else {
            c.to_uppercase().next().unwrap() as u32 - 'A' as u32 + 10
        };
        
        dziesietna = dziesietna * p as u64 + cyfra as u64;
    }
    
    // Konwertuj z dziesiętnej do podstawy q
    if dziesietna == 0 {
        return "0".to_string();
    }
    
    let mut wynik = String::new();
    let mut n = dziesietna;
    
    while n > 0 {
        let reszta = (n % q as u64) as u32;
        let znak = if reszta < 10 {
            char::from_digit(reszta, 10).unwrap()
        } else {
            (('A' as u8) + (reszta - 10) as u8) as char
        };
        wynik.insert(0, znak);
        n /= q as u64;
    }
    
    wynik
}

fn main() {
    let mut x_str = String::new();
    let mut p_str = String::new();
    let mut q_str = String::new();
    
    io::stdin().read_line(&mut x_str).expect("Błąd wczytywania");
    io::stdin().read_line(&mut p_str).expect("Błąd wczytywania");
    io::stdin().read_line(&mut q_str).expect("Błąd wczytywania");
    
    let x = x_str.trim();
    let p: u32 = p_str.trim().parse().unwrap_or(10);
    let q: u32 = q_str.trim().parse().unwrap_or(10);
    
    println!("{}", konwertuj_podstawe(x, p, q));
}
