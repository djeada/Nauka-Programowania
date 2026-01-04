/*
ZAD-02 — Macierz n×n: iloczyn indeksów

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle zagnieżdżone`

### Treść

Wczytaj `n`. Utwórz i wypisz macierz `n×n`, gdzie element `[i][j]` (indeksy od 0) ma wartość `i*j`.

### Wejście

* 1. linia: `n`

### Wyjście

* `n` wierszy po `n` liczb

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0 0 0
0 1 2
0 2 4
```

*/

use std::io;

// Funkcja generująca macierz n×n z iloczynami indeksów
// Złożoność czasowa: O(n^2)
// Złożoność pamięciowa: O(1) - wypisywanie bez przechowywania
fn generuj_macierz_iloczynow(n: usize) {
    for i in 0..n {
        for j in 0..n {
            if j > 0 {
                print!(" ");
            }
            print!("{}", i * j);
        }
        println!();
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: usize = input.trim().parse().expect("Nieprawidłowa liczba");

    generuj_macierz_iloczynow(n);
}
