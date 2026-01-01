/*
ZAD-04 — Dodawanie i odejmowanie macierzy

**Poziom:** ★☆☆
**Tagi:** `macierze`, `arytmetyka`

### Treść

Wczytaj dwie macierze `n×m`.
a) Wypisz ich sumę.
b) Wypisz różnicę: (pierwsza − druga).

### Wejście

* 1. linia: `n`
* 2. linia: `m`
* potem `n` wierszy pierwszej macierzy (po `m` liczb)
* potem `n` wierszy drugiej macierzy (po `m` liczb)

### Wyjście

Najpierw `n` wierszy sumy, potem `n` wierszy różnicy (bez dodatkowych napisów).

### Przykład

**Wejście:**

```
2
2
1 2
-2 0
5 -3
1 7
```

**Wyjście:**

```
6 -1
-1 7
-4 5
-3 -7
```

*/

use std::io;

// Funkcja wczytująca macierz
// Złożoność czasowa: O(n * m)
// Złożoność pamięciowa: O(n * m)
fn wczytaj_macierz(n: usize, m: usize) -> Vec<Vec<i32>> {
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

// Funkcja wypisująca macierz
// Złożoność czasowa: O(n * m)
// Złożoność pamięciowa: O(1)
fn wypisz_macierz(macierz: &Vec<Vec<i32>>) {
    for wiersz in macierz {
        for (i, &val) in wiersz.iter().enumerate() {
            if i > 0 {
                print!(" ");
            }
            print!("{}", val);
        }
        println!();
    }
}

// Funkcja dodająca dwie macierze
// Złożoność czasowa: O(n * m)
// Złożoność pamięciowa: O(n * m)
fn dodaj_macierze(a: &Vec<Vec<i32>>, b: &Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    let n = a.len();
    let m = a[0].len();
    let mut wynik = vec![vec![0; m]; n];
    
    for i in 0..n {
        for j in 0..m {
            wynik[i][j] = a[i][j] + b[i][j];
        }
    }
    
    wynik
}

// Funkcja odejmująca dwie macierze
// Złożoność czasowa: O(n * m)
// Złożoność pamięciowa: O(n * m)
fn odejmij_macierze(a: &Vec<Vec<i32>>, b: &Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    let n = a.len();
    let m = a[0].len();
    let mut wynik = vec![vec![0; m]; n];
    
    for i in 0..n {
        for j in 0..m {
            wynik[i][j] = a[i][j] - b[i][j];
        }
    }
    
    wynik
}

fn main() {
    let mut n_str = String::new();
    let mut m_str = String::new();
    
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    io::stdin().read_line(&mut m_str).expect("Błąd wczytywania");
    
    let n: usize = n_str.trim().parse().expect("Nieprawidłowa liczba");
    let m: usize = m_str.trim().parse().expect("Nieprawidłowa liczba");
    
    let macierz1 = wczytaj_macierz(n, m);
    let macierz2 = wczytaj_macierz(n, m);
    
    let suma = dodaj_macierze(&macierz1, &macierz2);
    let roznica = odejmij_macierze(&macierz1, &macierz2);
    
    wypisz_macierz(&suma);
    wypisz_macierz(&roznica);
}
