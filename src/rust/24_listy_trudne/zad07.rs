/*
ZAD-07 — Pojemność wody między słupkami

**Poziom:** ★★★
**Tagi:** `two pointers`, `prefix`, `trapping rain water`

### Treść

Otrzymujesz listę liczb naturalnych — wysokości słupków. Oblicz, ile jednostek wody może się zatrzymać pomiędzy słupkami po deszczu.

### Wejście

* 1 linia: lista wysokości `H`

### Wyjście

* 1 linia: jedna liczba naturalna — ilość wody

### Przykład

**Wejście:**

```
[3, 0, 1, 0, 2]
```

**Wyjście:**

```
5
```

*/

use std::io;

// Funkcja obliczająca pojemność wody między słupkami
// Złożoność czasowa: O(n), gdzie n to liczba słupków
// Złożoność pamięciowa: O(n)
fn pojemnosc_wody(wysokosci: &[i32]) -> i32 {
    let n = wysokosci.len();
    if n == 0 {
        return 0;
    }
    
    // Dla każdej pozycji znajdujemy maksimum z lewej i z prawej
    let mut max_lewo = vec![0; n];
    let mut max_prawo = vec![0; n];
    
    max_lewo[0] = wysokosci[0];
    for i in 1..n {
        max_lewo[i] = max_lewo[i - 1].max(wysokosci[i]);
    }
    
    max_prawo[n - 1] = wysokosci[n - 1];
    for i in (0..n - 1).rev() {
        max_prawo[i] = max_prawo[i + 1].max(wysokosci[i]);
    }
    
    // Oblicz wodę
    let mut woda = 0;
    for i in 0..n {
        let poziom = max_lewo[i].min(max_prawo[i]);
        woda += (poziom - wysokosci[i]).max(0);
    }
    
    woda
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    
    let lista_str = input.trim()
        .trim_start_matches('[')
        .trim_end_matches(']');
    
    let wysokosci: Vec<i32> = lista_str
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect();
    
    println!("{}", pojemnosc_wody(&wysokosci));
}
