/*
ZAD-07 — Powtarzające się podnapisy

**Poziom:** ★★★
**Tagi:** `string`, `substrings`, `count`

### Treść

Otrzymujesz napis. Znajdź wszystkie **podnapisy**, które występują w nim **więcej niż jeden raz**.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: lista napisów — wszystkie powtarzające się podnapisy

### Przykład

**Wejście:**

```
pythonpython
```

**Wyjście:**

```
['python']
```

### Uwagi

* Jeśli sprawdzarka wymaga konkretnej kolejności (np. rosnąco po długości/alfabetycznie) — musi to być opisane. W przeciwnym razie dopuszczalna może być dowolna kolejność.

*/

use std::io;
use std::collections::HashMap;

// Funkcja znajdująca powtarzające się podnapisy
// Złożoność czasowa: O(n^2), gdzie n to długość napisu
// Złożoność pamięciowa: O(n^2)
fn powtarzajace_podnapisy(napis: &str) -> Vec<String> {
    let mut mapa: HashMap<String, usize> = HashMap::new();
    let n = napis.len();
    
    // Generuj wszystkie podnapisy
    for i in 0..n {
        for j in (i + 1)..=n {
            let podnapis = napis[i..j].to_string();
            *mapa.entry(podnapis).or_insert(0) += 1;
        }
    }
    
    // Zbierz te, które występują więcej niż raz
    let mut wynik: Vec<String> = mapa.iter()
        .filter(|(_, &count)| count > 1)
        .map(|(s, _)| s.clone())
        .collect();
    
    // Sortuj dla spójności
    wynik.sort();
    wynik
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();
    
    let wynik = powtarzajace_podnapisy(napis);
    
    // Wypisz wynik
    print!("[");
    for (i, s) in wynik.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("'{}'", s);
    }
    println!("]");
}
