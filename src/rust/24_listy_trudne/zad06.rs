/*
ZAD-06 — Połączenie posortowanych list (unikalne)

**Poziom:** ★★★
**Tagi:** `merge`, `heap`, `unique`, `sorted`

### Treść

Otrzymujesz listę zawierającą `M` posortowanych list liczb naturalnych. Połącz je w jedną **posortowaną** listę zawierającą wszystkie elementy **bez powtórzeń**.

### Wejście

* 1 linia: lista list (każda wewnętrzna lista jest posortowana)

### Wyjście

* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

**Wejście:**

```
[[-6, 23, 29, 33], [6, 22, 35, 71], [5, 19, 21, 37], [-12, -7, -3, 28]]
```

**Wyjście:**

```
[-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71]
```

*/

use std::collections::BTreeSet;
use std::io;

// Funkcja łącząca posortowane listy w jedną bez duplikatów
// Złożoność czasowa: O(n log n), gdzie n to suma wszystkich elementów
// Złożoność pamięciowa: O(n)
fn polacz_listy(listy: &[Vec<i32>]) -> Vec<i32> {
    let mut zbior = BTreeSet::new();

    for lista in listy {
        for &element in lista {
            zbior.insert(element);
        }
    }

    zbior.into_iter().collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");

    // Parsuj listę list
    let dane = input.trim().trim_start_matches('[').trim_end_matches(']');

    let mut listy = Vec::new();
    let mut obecna_lista = Vec::new();
    let mut w_liscie = false;
    let mut buffer = String::new();

    for c in dane.chars() {
        if c == '[' {
            w_liscie = true;
            obecna_lista.clear();
        } else if c == ']' {
            if !buffer.is_empty() {
                if let Ok(num) = buffer.trim().parse() {
                    obecna_lista.push(num);
                }
                buffer.clear();
            }
            listy.push(obecna_lista.clone());
            w_liscie = false;
        } else if c == ',' && w_liscie {
            if !buffer.is_empty() {
                if let Ok(num) = buffer.trim().parse() {
                    obecna_lista.push(num);
                }
                buffer.clear();
            }
        } else if w_liscie && (c.is_digit(10) || c == '-' || c == ' ') {
            buffer.push(c);
        }
    }

    let wynik = polacz_listy(&listy);

    // Wypisz wynik
    print!("[");
    for (i, val) in wynik.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("{}", val);
    }
    println!("]");
}
