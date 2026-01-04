/*
ZAD-01 — Macierz z identycznymi wierszami 0..b

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle`, `print`

### Treść

Wczytaj `a` i `b`. Wypisz macierz składającą się z `a` identycznych wierszy, gdzie każdy wiersz to liczby od `0` do `b` włącznie.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

* `a` wierszy, w każdym: `0 1 2 ... b`

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
0 1 2
0 1 2
0 1 2
```

*/

use std::io;

// Funkcja generująca macierz z identycznymi wierszami
// Złożoność czasowa: O(a * b), gdzie a to liczba wierszy, b to zakres liczb
// Złożoność pamięciowa: O(a * b)
fn generuj_macierz(a: usize, b: usize) {
    for _ in 0..a {
        for j in 0..=b {
            if j > 0 {
                print!(" ");
            }
            print!("{}", j);
        }
        println!();
    }
}

fn main() {
    let mut a_str = String::new();
    let mut b_str = String::new();

    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");
    io::stdin().read_line(&mut b_str).expect("Błąd wczytywania");

    let a: usize = a_str.trim().parse().expect("Nieprawidłowa liczba");
    let b: usize = b_str.trim().parse().expect("Nieprawidłowa liczba");

    generuj_macierz(a, b);
}
