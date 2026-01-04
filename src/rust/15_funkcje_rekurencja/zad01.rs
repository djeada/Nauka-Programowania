/*
ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `Horner`, `I/O`

### Treść

Wczytaj współczynniki wielomianu ( a_nx^n + a_{n-1}x^{n-1} + \dots + a_0 ) oraz liczbę ( x ). Oblicz wartość wielomianu w punkcie ( x ).

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych: `a_n a_{n-1} ... a_0`
* 3. linia: `x` — liczba całkowita

### Wyjście

Jedna liczba całkowita — wartość wielomianu w punkcie `x`.

### Przykład

**Wejście:**

```
2
3 2 1
1
```

**Wyjście:**

```
6
```

### Uwagi o formatowaniu

* Użyj schematu Hornera (jest najprostszy i najszybszy).

*/

use std::io;

// Funkcja obliczająca wartość wielomianu metodą Hornera
// Złożoność czasowa: O(n), gdzie n to stopień wielomianu
// Złożoność pamięciowa: O(1)
fn wartosc_wielomianu(wspolczynniki: &[i32], x: i32) -> i32 {
    if wspolczynniki.is_empty() {
        return 0;
    }

    let mut wynik = wspolczynniki[0];
    for i in 1..wspolczynniki.len() {
        wynik = wynik * x + wspolczynniki[i];
    }

    wynik
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    let n: usize = n_str.trim().parse().expect("Nieprawidłowa liczba");

    let mut wspolczynniki_str = String::new();
    io::stdin()
        .read_line(&mut wspolczynniki_str)
        .expect("Błąd wczytywania");
    let wspolczynniki: Vec<i32> = wspolczynniki_str
        .trim()
        .split_whitespace()
        .map(|s| s.parse().expect("Nieprawidłowa liczba"))
        .collect();

    let mut x_str = String::new();
    io::stdin().read_line(&mut x_str).expect("Błąd wczytywania");
    let x: i32 = x_str.trim().parse().expect("Nieprawidłowa liczba");

    println!("{}", wartosc_wielomianu(&wspolczynniki, x));
}
