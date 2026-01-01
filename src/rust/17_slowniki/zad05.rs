/*
ZAD-05 — Pracownik z największym sumarycznym zyskiem

**Poziom:** ★☆☆
**Tagi:** `dict`, `sumowanie`

### Treść

Wczytaj `n` wpisów: `pracownik zysk`. Zsumuj zyski per pracownik i wypisz nazwę pracownika z największą sumą.
(Jeśli remis, wybierz tego, który pierwszy osiągnął tę maksymalną sumę podczas przetwarzania.)

### Wejście

* 1 linia: `n`
* następnie `n` linii: `imie_i_nazwisko zysk`

### Wyjście

* Jedna linia: `imie_i_nazwisko`

### Przykład

**Wejście:**

```
5
Barnaba_Barabash 120
Jon_Snow 100
Kira_Summer 300
Barnaba_Barabash 200
Bob_Marley 110
```

**Wyjście:**

```
Barnaba_Barabash
```

*/

use std::io;
use std::collections::HashMap;

// Funkcja znajdująca pracownika z największym zyskiem
// Złożoność czasowa: O(n)
// Złożoność pamięciowa: O(k), gdzie k to liczba unikalnych pracowników
fn pracownik_z_max_zyskiem(dane: Vec<(String, i32)>) -> String {
    let mut zyski: HashMap<String, i32> = HashMap::new();
    let mut kolejnosc = Vec::new();
    
    for (pracownik, zysk) in dane {
        if !zyski.contains_key(&pracownik) {
            kolejnosc.push(pracownik.clone());
        }
        *zyski.entry(pracownik).or_insert(0) += zysk;
    }
    
    let mut max_pracownik = String::new();
    let mut max_zysk = i32::MIN;
    
    for pracownik in kolejnosc {
        let zysk = *zyski.get(&pracownik).unwrap_or(&0);
        if zysk > max_zysk {
            max_zysk = zysk;
            max_pracownik = pracownik;
        }
    }
    
    max_pracownik
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    let n: usize = n_str.trim().parse().unwrap_or(0);
    
    let mut dane = Vec::new();
    
    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let czesci: Vec<&str> = input.trim().split_whitespace().collect();
        
        if czesci.len() >= 2 {
            let pracownik = czesci[0].to_string();
            let zysk: i32 = czesci[1].parse().unwrap_or(0);
            dane.push((pracownik, zysk));
        }
    }
    
    println!("{}", pracownik_z_max_zyskiem(dane));
}
