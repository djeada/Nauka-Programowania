/*
ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `wyrównanie stopni`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich sumą.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki sumy od najwyższej potęgi, oddzielone spacją.

### Przykład

**Wejście:**

```
2
3 5 2
2
2 -8 1
```

**Wyjście:**

```
5 -3 3
```

### Uwagi o formatowaniu

* Jeśli stopnie są różne, wyrównaj listy „od końca” (od wyrazu wolnego), dopisując zera na początku krótszej.

*/

use std::io;

// Funkcja dodająca dwa wielomiany
// Złożoność czasowa: O(max(n, m)), gdzie n i m to stopnie wielomianów
// Złożoność pamięciowa: O(max(n, m))
fn dodaj_wielomiany(a: &[i32], b: &[i32]) -> Vec<i32> {
    let max_len = a.len().max(b.len());
    let mut wynik = vec![0; max_len];
    
    let offset_a = max_len - a.len();
    for (i, &val) in a.iter().enumerate() {
        wynik[offset_a + i] += val;
    }
    
    let offset_b = max_len - b.len();
    for (i, &val) in b.iter().enumerate() {
        wynik[offset_b + i] += val;
    }
    
    // Usuń wiodące zera
    while wynik.len() > 1 && wynik[0] == 0 {
        wynik.remove(0);
    }
    
    wynik
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    
    let mut a_str = String::new();
    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");
    let a: Vec<i32> = a_str
        .trim()
        .split_whitespace()
        .map(|s| s.parse().expect("Nieprawidłowa liczba"))
        .collect();
    
    let mut m_str = String::new();
    io::stdin().read_line(&mut m_str).expect("Błąd wczytywania");
    
    let mut b_str = String::new();
    io::stdin().read_line(&mut b_str).expect("Błąd wczytywania");
    let b: Vec<i32> = b_str
        .trim()
        .split_whitespace()
        .map(|s| s.parse().expect("Nieprawidłowa liczba"))
        .collect();
    
    let wynik = dodaj_wielomiany(&a, &b);
    
    for (i, &w) in wynik.iter().enumerate() {
        if i > 0 {
            print!(" ");
        }
        print!("{}", w);
    }
    println!();
}
