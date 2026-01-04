/*
ZAD-05 — Czy macierz jest magiczna?

**Poziom:** ★★☆
**Tagi:** `macierze`, `suma`, `warunki`

### Treść

Wczytaj macierz kwadratową `n×n` z dodatnimi liczbami naturalnymi. Sprawdź, czy to **kwadrat magiczny**: suma każdego wiersza, każdej kolumny oraz obu przekątnych jest taka sama.

### Wejście

* 1. linia: `n`
* następnie `n` wierszy po `n` liczb

### Wyjście

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
3
6 7 2
1 5 9
8 3 4
```

**Wyjście:**

```
Prawda
```

*/

use std::io;

// Funkcja wczytująca macierz
fn wczytaj_macierz(n: usize) -> Vec<Vec<i32>> {
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

// Funkcja sprawdzająca czy macierz jest magiczna
// Złożoność czasowa: O(n^2)
// Złożoność pamięciowa: O(1)
fn czy_magiczna(macierz: &Vec<Vec<i32>>) -> bool {
    let n = macierz.len();

    // Oblicz sumę pierwszego wiersza jako wzorzec
    let suma_wzorcowa: i32 = macierz[0].iter().sum();

    // Sprawdź wszystkie wiersze
    for wiersz in macierz {
        if wiersz.iter().sum::<i32>() != suma_wzorcowa {
            return false;
        }
    }

    // Sprawdź wszystkie kolumny
    for j in 0..n {
        let suma: i32 = (0..n).map(|i| macierz[i][j]).sum();
        if suma != suma_wzorcowa {
            return false;
        }
    }

    // Sprawdź główną przekątną
    let suma: i32 = (0..n).map(|i| macierz[i][i]).sum();
    if suma != suma_wzorcowa {
        return false;
    }

    // Sprawdź drugą przekątną
    let suma: i32 = (0..n).map(|i| macierz[i][n - 1 - i]).sum();
    if suma != suma_wzorcowa {
        return false;
    }

    true
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: usize = input.trim().parse().expect("Nieprawidłowa liczba");

    let macierz = wczytaj_macierz(n);

    if czy_magiczna(&macierz) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
