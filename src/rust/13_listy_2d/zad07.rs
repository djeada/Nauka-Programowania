/*
ZAD-07 — Zerowanie macierzy

**Poziom:** ★★☆
**Tagi:** `macierze`, `indeksy`

### Treść

Wczytaj macierz `n×m`. Jeśli w macierzy występuje `0`, to **cały wiersz i cała kolumna** tego zera mają zostać ustawione na `0` (dla wszystkich zer naraz).

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb

### Wyjście

* `n` wierszy zmodyfikowanej macierzy

### Przykład

**Wejście:**

```
3 3
1 2 3
4 0 6
7 8 9
```

**Wyjście:**

```
1 0 3
0 0 0
7 0 9
```

*/

use std::collections::HashSet;
use std::io;

// Funkcja wczytująca macierz
fn wczytaj_macierz(n: usize, m: usize) -> Vec<Vec<i32>> {
    let mut macierz = Vec::new();

    for _ in 0..n {
        let mut wiersz = String::new();
        io::stdin()
            .read_line(&mut wiersz)
            .expect("Błąd wczytywania");
        let liczby: Vec<i32> = wiersz
            .trim()
            .split_whitespace()
            .map(|s| s.parse().expect("Nieprawidłowa liczba"))
            .collect();
        macierz.push(liczby);
    }

    macierz
}

// Funkcja zerująca wiersze i kolumny zawierające 0
// Złożoność czasowa: O(n * m)
// Złożoność pamięciowa: O(n + m)
fn zeruj_macierz(macierz: &mut Vec<Vec<i32>>) {
    let n = macierz.len();
    let m = macierz[0].len();

    let mut wiersze_do_wyzerowania = HashSet::new();
    let mut kolumny_do_wyzerowania = HashSet::new();

    // Znajdź pozycje zer
    for i in 0..n {
        for j in 0..m {
            if macierz[i][j] == 0 {
                wiersze_do_wyzerowania.insert(i);
                kolumny_do_wyzerowania.insert(j);
            }
        }
    }

    // Wyzeruj odpowiednie wiersze
    for &i in &wiersze_do_wyzerowania {
        for j in 0..m {
            macierz[i][j] = 0;
        }
    }

    // Wyzeruj odpowiednie kolumny
    for &j in &kolumny_do_wyzerowania {
        for i in 0..n {
            macierz[i][j] = 0;
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let wymiary: Vec<usize> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().expect("Nieprawidłowa liczba"))
        .collect();

    let n = wymiary[0];
    let m = wymiary[1];

    let mut macierz = wczytaj_macierz(n, m);
    zeruj_macierz(&mut macierz);

    for wiersz in macierz {
        for (i, val) in wiersz.iter().enumerate() {
            if i > 0 {
                print!(" ");
            }
            print!("{}", val);
        }
        println!();
    }
}
