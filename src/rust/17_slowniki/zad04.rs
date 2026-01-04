/*
ZAD-04 — Usuń pary ze słownika na podstawie wartości

**Poziom:** ★☆☆
**Tagi:** `dict`, `filtrowanie`

### Treść

Wczytaj słownik (`n` par: klucz-napis, wartość-liczba) oraz liczbę `k`. Usuń wszystkie pary, gdzie wartość == `k`. Wypisz wynikowy słownik.

### Wejście

* 1 linia: `n`
* następnie `n` linii: `klucz wartość`
* ostatnia linia: `k`

### Wyjście

* Słownik po usunięciu par

### Przykład

**Wejście:**

```
4
aaa 5
abc 1
xxx 5
cba 3
5
```

**Wyjście:**

```
{'abc': 1, 'cba': 3}
```

*/

use std::collections::HashMap;
use std::io;

// Funkcja usuwająca pary ze słownika na podstawie wartości
// Złożoność czasowa: O(n)
// Złożoność pamięciowa: O(n)
fn usun_pary_po_wartosci(slownik: HashMap<String, i32>, k: i32) -> HashMap<String, i32> {
    slownik.into_iter().filter(|(_, v)| *v != k).collect()
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    let n: usize = n_str.trim().parse().unwrap_or(0);

    let mut slownik = HashMap::new();
    let mut kolejnosc = Vec::new();

    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let czesci: Vec<&str> = input.trim().split_whitespace().collect();

        if czesci.len() >= 2 {
            let klucz = czesci[0].to_string();
            let wartosc: i32 = czesci[1].parse().unwrap_or(0);
            slownik.insert(klucz.clone(), wartosc);
            kolejnosc.push(klucz);
        }
    }

    let mut k_str = String::new();
    io::stdin().read_line(&mut k_str).expect("Błąd wczytywania");
    let k: i32 = k_str.trim().parse().unwrap_or(0);

    let wynik = usun_pary_po_wartosci(slownik, k);

    if wynik.is_empty() {
        println!("{{}}");
    } else {
        print!("{{");
        let mut first = true;
        for klucz in kolejnosc {
            if let Some(&wartosc) = wynik.get(&klucz) {
                if !first {
                    print!(", ");
                }
                print!("'{}': {}", klucz, wartosc);
                first = false;
            }
        }
        println!("}}");
    }
}
