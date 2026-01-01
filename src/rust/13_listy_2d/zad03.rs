/*
ZAD-03 — Macierz 2-kolumnowa z dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `macierze`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, wypisz macierz 2-kolumnową: wiersz `i` to `(lista1[i], lista2[i])`.
Jeśli długości są różne, wypisz: `Pusta macierz`

### Wejście

* 1. linia: `n`
* 2. linia: `m`
* następnie `n` liczb (pierwsza lista)
* następnie `m` liczb (druga lista)

### Wyjście

* Jeśli `n = m`: `n` wierszy `x y`
* Jeśli `n ≠ m`: jedna linia `Pusta macierz`

### Przykład

**Wejście:**

```
3
3
3
5
2
2
8
1
```

**Wyjście:**

```
3 2
5 8
2 1
```

*/

use std::io;

// Funkcja tworząca macierz 2-kolumnową z dwóch list
// Złożoność czasowa: O(n), gdzie n to długość list
// Złożoność pamięciowa: O(n)
fn utworz_macierz_2_kolumnowa(n: usize, m: usize, lista1: Vec<i32>, lista2: Vec<i32>) {
    if n != m {
        println!("Pusta macierz");
        return;
    }
    
    for i in 0..n {
        println!("{} {}", lista1[i], lista2[i]);
    }
}

fn main() {
    let mut n_str = String::new();
    let mut m_str = String::new();
    
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    io::stdin().read_line(&mut m_str).expect("Błąd wczytywania");
    
    let n: usize = n_str.trim().parse().expect("Nieprawidłowa liczba");
    let m: usize = m_str.trim().parse().expect("Nieprawidłowa liczba");
    
    let mut lista1 = Vec::new();
    let mut lista2 = Vec::new();
    
    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let liczba: i32 = input.trim().parse().expect("Nieprawidłowa liczba");
        lista1.push(liczba);
    }
    
    for _ in 0..m {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let liczba: i32 = input.trim().parse().expect("Nieprawidłowa liczba");
        lista2.push(liczba);
    }
    
    utworz_macierz_2_kolumnowa(n, m, lista1, lista2);
}
