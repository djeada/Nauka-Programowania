/*
ZAD-03 — Czy dwa słowa są anagramami?

**Poziom:** ★☆☆
**Tagi:** `anagram`, `sortowanie`, `zliczanie`

### Treść

Wczytaj dwa słowa i sprawdź, czy są anagramami (czy da się utworzyć jedno przez przestawienie liter drugiego).

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

Jedna linia:

* `Prawda` — jeśli anagramy
* `Fałsz` — jeśli nie

### Przykład

**Wejście:**

```
ula
lua
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Najprościej: porównaj posortowane litery albo słowniki zliczeń znaków.

*/

use std::io;

// Funkcja sprawdzająca czy dwa słowa są anagramami
// Złożoność czasowa: O(n log n), gdzie n to długość słowa (przez sortowanie)
// Złożoność pamięciowa: O(n)
fn czy_anagramy(s1: &str, s2: &str) -> bool {
    let mut chars1: Vec<char> = s1.to_lowercase().chars().collect();
    let mut chars2: Vec<char> = s2.to_lowercase().chars().collect();
    
    chars1.sort();
    chars2.sort();
    
    chars1 == chars2
}

fn main() {
    let mut s1 = String::new();
    let mut s2 = String::new();
    
    io::stdin().read_line(&mut s1).expect("Błąd wczytywania");
    io::stdin().read_line(&mut s2).expect("Błąd wczytywania");
    
    let s1 = s1.trim();
    let s2 = s2.trim();
    
    if czy_anagramy(s1, s2) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
