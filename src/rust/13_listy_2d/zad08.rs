/*
ZAD-08 — Wypisanie elementów macierzy spiralnie

**Poziom:** ★★☆
**Tagi:** `macierze`, `spirala`

### Treść

Wczytaj macierz `n×m` i wypisz jej elementy spiralnie (zgodnie z ruchem wskazówek zegara), startując z lewego górnego rogu.

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb

### Wyjście

* 1 linia: elementy spiralnie, oddzielone spacjami

### Przykład

**Wejście:**

```
3 3
1 2 3
4 5 6
7 8 9
```

**Wyjście:**

```
1 2 3 6 9 8 7 4 5
```

*/

use std::io;

// Funkcja wczytująca macierz
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

// Funkcja wypisująca elementy macierzy spiralnie
// Złożoność czasowa: O(n * m)
// Złożoność pamięciowa: O(1)
fn wypisz_spiralnie(macierz: &Vec<Vec<i32>>) -> Vec<i32> {
    let n = macierz.len();
    if n == 0 {
        return Vec::new();
    }
    let m = macierz[0].len();
    
    let mut wynik = Vec::new();
    let mut gora = 0;
    let mut dol = n;
    let mut lewo = 0;
    let mut prawo = m;
    
    while gora < dol && lewo < prawo {
        // Przejdź w prawo po górnym wierszu
        for j in lewo..prawo {
            wynik.push(macierz[gora][j]);
        }
        gora += 1;
        
        // Przejdź w dół po prawej kolumnie
        for i in gora..dol {
            wynik.push(macierz[i][prawo - 1]);
        }
        prawo -= 1;
        
        // Przejdź w lewo po dolnym wierszu (jeśli istnieje)
        if gora < dol {
            for j in (lewo..prawo).rev() {
                wynik.push(macierz[dol - 1][j]);
            }
            dol -= 1;
        }
        
        // Przejdź w górę po lewej kolumnie (jeśli istnieje)
        if lewo < prawo {
            for i in (gora..dol).rev() {
                wynik.push(macierz[i][lewo]);
            }
            lewo += 1;
        }
    }
    
    wynik
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
    
    let macierz = wczytaj_macierz(n, m);
    let spirala = wypisz_spiralnie(&macierz);
    
    for (i, val) in spirala.iter().enumerate() {
        if i > 0 {
            print!(" ");
        }
        print!("{}", val);
    }
    println!();
}
