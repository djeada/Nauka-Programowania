/*
ZAD-02 — Słownik z dwóch list (klucze i wartości)

**Poziom:** ★☆☆
**Tagi:** `dict`, `listy`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, utwórz słownik: klucz z pierwszej listy → wartość z drugiej listy.
Jeśli długości są różne, wypisz pusty słownik `{}`.

### Wejście

* 1 linia: `n`
* 2 linia: `m`
* następnie `n` liczb (pierwsza lista)
* następnie `m` liczb (druga lista)

### Wyjście

* Słownik albo `{}`

### Przykład

**Wejście:**

```
3
3
3 5 8
1 2 -1
```

**Wyjście:**

```
{3: 1, 5: 2, 8: -1}
```

*/

use std::io;
use std::collections::HashMap;

// Funkcja tworząca słownik z dwóch list
// Złożoność czasowa: O(min(n, m))
// Złożoność pamięciowa: O(min(n, m))
fn slownik_z_list(klucze: Vec<i32>, wartosci: Vec<i32>) -> HashMap<i32, i32> {
    if klucze.len() != wartosci.len() {
        return HashMap::new();
    }
    
    let mut slownik = HashMap::new();
    for (k, v) in klucze.iter().zip(wartosci.iter()) {
        slownik.insert(*k, *v);
    }
    
    slownik
}

fn main() {
    let mut n_str = String::new();
    let mut m_str = String::new();
    
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    io::stdin().read_line(&mut m_str).expect("Błąd wczytywania");
    
    let n: usize = n_str.trim().parse().unwrap_or(0);
    let m: usize = m_str.trim().parse().unwrap_or(0);
    
    let mut klucze = Vec::new();
    let mut wartosci = Vec::new();
    
    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let liczba: i32 = input.trim().parse().unwrap_or(0);
        klucze.push(liczba);
    }
    
    for _ in 0..m {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let liczba: i32 = input.trim().parse().unwrap_or(0);
        wartosci.push(liczba);
    }
    
    let slownik = slownik_z_list(klucze.clone(), wartosci.clone());
    
    if slownik.is_empty() {
        println!("{{}}");
    } else {
        print!("{{");
        let mut first = true;
        for k in klucze {
            if let Some(&v) = slownik.get(&k) {
                if !first {
                    print!(", ");
                }
                print!("{}: {}", k, v);
                first = false;
            }
        }
        println!("}}");
    }
}
