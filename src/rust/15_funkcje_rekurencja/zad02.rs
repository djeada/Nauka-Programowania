/*
ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `listy`, `I/O`

### Treść

Wczytaj współczynniki wielomianu oraz liczbę `k`. Wypisz współczynniki wielomianu powstałego przez pomnożenie każdego współczynnika przez `k`.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych: `a_n ... a_0`
* 3. linia: `k` — liczba całkowita (skalar)

### Wyjście

Jedna linia: `n+1` liczb całkowitych (współczynniki po mnożeniu), oddzielonych spacją.

### Przykład

**Wejście:**

```
2
4 -3 2
-2
```

**Wyjście:**

```
-8 6 -4
```

*/

use std::io;

// Funkcja mnożąca wielomian przez skalar
// Złożoność czasowa: O(n), gdzie n to liczba współczynników
// Złożoność pamięciowa: O(n)
fn mnoz_przez_skalar(wspolczynniki: &[i32], k: i32) -> Vec<i32> {
    wspolczynniki.iter().map(|&w| w * k).collect()
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");

    let mut wspolczynniki_str = String::new();
    io::stdin()
        .read_line(&mut wspolczynniki_str)
        .expect("Błąd wczytywania");
    let wspolczynniki: Vec<i32> = wspolczynniki_str
        .trim()
        .split_whitespace()
        .map(|s| s.parse().expect("Nieprawidłowa liczba"))
        .collect();

    let mut k_str = String::new();
    io::stdin().read_line(&mut k_str).expect("Błąd wczytywania");
    let k: i32 = k_str.trim().parse().expect("Nieprawidłowa liczba");

    let wynik = mnoz_przez_skalar(&wspolczynniki, k);

    for (i, &w) in wynik.iter().enumerate() {
        if i > 0 {
            print!(" ");
        }
        print!("{}", w);
    }
    println!();
}
