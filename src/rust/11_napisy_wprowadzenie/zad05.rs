/*
ZAD-05 — Co k-ty znak poziomo i pionowo

**Poziom:** ★☆☆
**Tagi:** `string`, `slicing`, `pętle`

### Treść

Wczytaj napis i liczbę `k`.

a) Wypisz co `k`-ty znak w jednym wierszu, oddzielając znaki spacjami.
b) Wypisz co `k`-ty znak pionowo (każdy w osobnej linii).

### Wejście

* 1. linia: napis
* 2. linia: liczba naturalna `k` (k ≥ 1)

### Wyjście

* (a) 1 linia: znaki oddzielone spacjami
* (b) wiele linii: każdy znak osobno

### Przykład

**Wejście:**

```
Grzechotnik
3
```

**Wyjście:**

```
z h n
z
h
n
```

### Uwagi o formatowaniu

* Dokładnie jedna spacja między znakami w punkcie (a), bez spacji na końcu linii.

*/

use std::io;

// Funkcja wypisująca co k-ty znak poziomo i pionowo
// Złożoność czasowa: O(n/k), gdzie n to długość napisu
// Złożoność pamięciowa: O(n/k)
fn co_k_ty_znak(napis: &str, k: usize) {
    let chars: Vec<char> = napis.chars().collect();
    let mut wynik: Vec<char> = Vec::new();
    
    // Zbierz co k-ty znak (indeksowanie od 0, więc bierzemy k-1, 2k-1, 3k-1...)
    for i in (k-1..chars.len()).step_by(k) {
        wynik.push(chars[i]);
    }
    
    // a) Wypisz poziomo z spacjami
    if !wynik.is_empty() {
        for (i, c) in wynik.iter().enumerate() {
            if i > 0 {
                print!(" ");
            }
            print!("{}", c);
        }
        println!();
    }
    
    // b) Wypisz pionowo
    for c in wynik.iter() {
        println!("{}", c);
    }
}

fn main() {
    let mut napis = String::new();
    let mut k_str = String::new();
    
    io::stdin().read_line(&mut napis).expect("Błąd wczytywania");
    io::stdin().read_line(&mut k_str).expect("Błąd wczytywania");
    
    let napis = napis.trim();
    let k: usize = k_str.trim().parse().expect("Nieprawidłowa liczba");
    
    co_k_ty_znak(napis, k);
}
