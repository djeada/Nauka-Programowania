/*
ZAD-03 — Sortowanie listy par względem kryterium

**Poziom:** ★☆☆
**Tagi:** `sort`, `tuple`, `list`

### Treść

Otrzymujesz listę par `(napis, liczba)`.

a) Posortuj pary rosnąco po liczbie.
b) Posortuj pary rosnąco po długości napisu.

Wypisz wyniki dla a) i b) w osobnych liniach.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: `napis liczba` (napis bez spacji)

### Wyjście

* 1 linia: lista par posortowana jak w podpunkcie a)
* 2 linia: lista par posortowana jak w podpunkcie b)

### Przykład

**Wejście:**

```
3
ab 3
bca 1
c 2
```

**Wyjście:**

```
[('bca', 1), ('c', 2), ('ab', 3)]
[('c', 2), ('ab', 3), ('bca', 1)]
```

*/

use std::io;

// Funkcja sortująca pary według różnych kryteriów
// Złożoność czasowa: O(n log n)
// Złożoność pamięciowa: O(n)
fn sortuj_pary_po_liczbie(pary: &mut Vec<(String, i32)>) {
    pary.sort_by_key(|p| p.1);
}

fn sortuj_pary_po_dlugosci(pary: &mut Vec<(String, i32)>) {
    pary.sort_by_key(|p| p.0.len());
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    let n: usize = n_str.trim().parse().unwrap_or(0);
    
    let mut pary = Vec::new();
    
    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let czesci: Vec<&str> = input.trim().split_whitespace().collect();
        
        if czesci.len() >= 2 {
            let napis = czesci[0].to_string();
            let liczba: i32 = czesci[1].parse().unwrap_or(0);
            pary.push((napis, liczba));
        }
    }
    
    // Sortowanie po liczbie
    let mut pary_a = pary.clone();
    sortuj_pary_po_liczbie(&mut pary_a);
    
    print!("[");
    for (i, (napis, liczba)) in pary_a.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("('{}', {})", napis, liczba);
    }
    println!("]");
    
    // Sortowanie po długości napisu
    let mut pary_b = pary.clone();
    sortuj_pary_po_dlugosci(&mut pary_b);
    
    print!("[");
    for (i, (napis, liczba)) in pary_b.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("('{}', {})", napis, liczba);
    }
    println!("]");
}
