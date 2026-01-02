/*
ZAD-02 — Przesuń zera na koniec listy

**Poziom:** ★★☆
**Tagi:** `list`, `stabilność`, `przekształcenie`

### Treść

Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, **zachowując kolejność** pozostałych elementów.

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista po przekształceniu

### Przykład

**Wejście:**

```
[0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
```

**Wyjście:**

```
[1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]
```

*/

use std::io;

// Funkcja przesuwająca zera na koniec listy
// Złożoność czasowa: O(n), gdzie n to długość listy
// Złożoność pamięciowa: O(1) - modyfikacja in-place
fn przesun_zera_na_koniec(lista: &mut Vec<i32>) {
    let mut poz_zapisu = 0;
    
    // Pierwsza faza: przenieś wszystkie niezerowe elementy na początek
    for i in 0..lista.len() {
        if lista[i] != 0 {
            lista[poz_zapisu] = lista[i];
            poz_zapisu += 1;
        }
    }
    
    // Druga faza: wypełnij resztę zerami
    for i in poz_zapisu..lista.len() {
        lista[i] = 0;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    
    // Parsuj listę z formatu [0, 1, 3, ...]
    let lista_str = input.trim()
        .trim_start_matches('[')
        .trim_end_matches(']');
    
    let mut lista: Vec<i32> = lista_str
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect();
    
    przesun_zera_na_koniec(&mut lista);
    
    // Wypisz wynik
    print!("[");
    for (i, val) in lista.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("{}", val);
    }
    println!("]");
}
