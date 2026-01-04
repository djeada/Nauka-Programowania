/*
ZAD-09 — Klepsydra o największej sumie

**Poziom:** ★★☆
**Tagi:** `macierze`, `przeszukiwanie`

### Treść

Wczytaj macierz `n×m` (n,m ≥ 3). Znajdź maksymalną sumę „klepsydry” (7 pól):

```
a b c
  d
e f g
```

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb całkowitych

### Wyjście

* 1 linia: maksymalna suma klepsydry

### Przykład

**Wejście:**

```
4 4
7 4 2 0
4 8 10 8
3 6 7 6
3 9 19 14
```

**Wyjście:**

```
75
```

*/

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

// Funkcja obliczająca sumę klepsydry
// Złożoność czasowa: O(1)
// Złożoność pamięciowa: O(1)
fn suma_klepsydry(macierz: &Vec<Vec<i32>>, i: usize, j: usize) -> i32 {
    macierz[i][j]
        + macierz[i][j + 1]
        + macierz[i][j + 2]
        + macierz[i + 1][j + 1]
        + macierz[i + 2][j]
        + macierz[i + 2][j + 1]
        + macierz[i + 2][j + 2]
}

// Funkcja znajdująca maksymalną sumę klepsydry
// Złożoność czasowa: O((n-2) * (m-2))
// Złożoność pamięciowa: O(1)
fn max_suma_klepsydry(macierz: &Vec<Vec<i32>>) -> i32 {
    let n = macierz.len();
    let m = macierz[0].len();

    let mut max_suma = i32::MIN;

    for i in 0..n - 2 {
        for j in 0..m - 2 {
            let suma = suma_klepsydry(macierz, i, j);
            max_suma = max_suma.max(suma);
        }
    }

    max_suma
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
    println!("{}", max_suma_klepsydry(&macierz));
}
