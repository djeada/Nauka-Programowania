/*
ZAD-10 — Obróć macierz o 90° w prawo

**Poziom:** ★★☆
**Tagi:** `macierze`, `transpozycja`

### Treść

Wczytaj kwadratową macierz `n×n` i wypisz ją po obrocie o 90° zgodnie z ruchem wskazówek zegara.

### Wejście

* 1. linia: `n`
* następnie `n` wierszy po `n` liczb

### Wyjście

* `n` wierszy obróconej macierzy

### Przykład

**Wejście:**

```
3
1 2 3
4 5 6
7 8 9
```

**Wyjście:**

```
7 4 1
8 5 2
9 6 3
```

*/

use std::io;

// Funkcja wczytująca macierz
fn wczytaj_macierz(n: usize) -> Vec<Vec<i32>> {
    let mut macierz = Vec::new();
    
    for _ in 0..n {
        let mut wiersz = String::new();
        io::stdin().read_line(&mut wiersz).expect("Błąd wczytywania");
        let liczby: Vec<i32> = wiersz
            .trim()
            .split_whitespace()
            .map(|s| s.parse().expect("Nieprawidłowa liczba"))
            .collect();
        macierz.push(liczby);
    }
    
    macierz
}

// Funkcja obracająca macierz o 90° w prawo
// Złożoność czasowa: O(n^2)
// Złożoność pamięciowa: O(n^2)
fn obroc_90_stopni(macierz: &Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    let n = macierz.len();
    let mut wynik = vec![vec![0; n]; n];
    
    for i in 0..n {
        for j in 0..n {
            wynik[j][n - 1 - i] = macierz[i][j];
        }
    }
    
    wynik
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: usize = input.trim().parse().expect("Nieprawidłowa liczba");
    
    let macierz = wczytaj_macierz(n);
    let obrocona = obroc_90_stopni(&macierz);
    
    for wiersz in obrocona {
        for (i, val) in wiersz.iter().enumerate() {
            if i > 0 {
                print!(" ");
            }
            print!("{}", val);
        }
        println!();
    }
}
