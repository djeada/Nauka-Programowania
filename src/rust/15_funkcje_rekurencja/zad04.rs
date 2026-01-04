/*
ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `wielomiany`, `konwolucja`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich iloczynem.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki iloczynu (długość `n+m+1`), oddzielone spacją.

### Przykład

**Wejście:**

```
3
5 0 10 6
2
1 2 4
```

**Wyjście:**

```
5 10 30 26 52 24
```

*/

use std::io;

// Funkcja mnożąca dwa wielomiany
// Złożoność czasowa: O(n * m), gdzie n i m to liczby współczynników
// Złożoność pamięciowa: O(n + m)
fn mnoz_wielomiany(a: &[i32], b: &[i32]) -> Vec<i32> {
    if a.is_empty() || b.is_empty() {
        return vec![0];
    }

    let mut wynik = vec![0; a.len() + b.len() - 1];

    for (i, &a_val) in a.iter().enumerate() {
        for (j, &b_val) in b.iter().enumerate() {
            wynik[i + j] += a_val * b_val;
        }
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

    let wynik = mnoz_wielomiany(&a, &b);

    for (i, &w) in wynik.iter().enumerate() {
        if i > 0 {
            print!(" ");
        }
        print!("{}", w);
    }
    println!();
}
