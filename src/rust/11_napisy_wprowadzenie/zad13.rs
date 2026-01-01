/*
ZAD-13 — Znaki na indeksach będących liczbami pierwszymi

**Poziom:** ★☆☆
**Tagi:** `liczby pierwsze`, `indeksy`, `string`

### Treść

Wczytaj napis. Zbierz znaki, których **indeksy (od 0)** są liczbami pierwszymi (2, 3, 5, 7, ...). Wypisz wynik jako listę w stylu Pythona.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: lista znaków, np. `['o', 'ń']`

### Przykład

**Wejście:**

```
Słoń
```

**Wyjście:**

```
['o', 'ń']
```

### Uwagi

* Indeksy: `S(0) ł(1) o(2) ń(3)` → bierz 2 i 3.

*/

use std::io;

// Funkcja sprawdzająca czy liczba jest pierwsza
// Złożoność czasowa: O(sqrt(n))
// Złożoność pamięciowa: O(1)
fn czy_pierwsza(n: usize) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    let mut i = 3;
    while i * i <= n {
        if n % i == 0 {
            return false;
        }
        i += 2;
    }
    true
}

// Funkcja zbierająca znaki na indeksach będących liczbami pierwszymi
// Złożoność czasowa: O(n*sqrt(n)), gdzie n to długość napisu
// Złożoność pamięciowa: O(k), gdzie k to liczba indeksów pierwszych
fn znaki_na_indeksach_pierwszych(napis: &str) -> Vec<char> {
    napis
        .chars()
        .enumerate()
        .filter(|(i, _)| czy_pierwsza(*i))
        .map(|(_, c)| c)
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();
    
    let wynik = znaki_na_indeksach_pierwszych(napis);
    
    // Formatowanie jako lista w stylu Pythona
    print!("[");
    for (i, c) in wynik.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("'{}'", c);
    }
    println!("]");
}
