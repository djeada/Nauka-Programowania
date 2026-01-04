/*
ZAD-07 — Sortowanie listy 0/1/2

**Poziom:** ★★☆
**Tagi:** `sort`, `counting`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0`, `1` lub `2`. Posortuj ją rosnąco.

### Wejście

* 1 linia: liczba naturalna `N`
* 2 linia: `N` liczb (0/1/2) oddzielonych spacjami

### Wyjście

* 1 linia: posortowana lista w formacie jak w przykładzie

### Przykład

**Wejście:**

```
7
1 0 1 2 2 0 1
```

**Wyjście:**

```
[0, 0, 1, 1, 1, 2, 2]
```

*/

use std::io;

// Funkcja sortująca listę z trzema wartościami metodą zliczania
// Złożoność czasowa: O(n)
// Złożoność pamięciowa: O(1)
fn sortuj_trojwartosciowa(lista: &mut Vec<u32>) {
    // Zliczamy wystąpienia 0, 1 i 2
    let mut licznik = [0, 0, 0];
    for &x in lista.iter() {
        if x <= 2 {
            licznik[x as usize] += 1;
        }
    }

    // Wypełniamy listę: najpierw zera, potem jedynki, na końcu dwójki
    let mut idx = 0;
    for wartosc in 0..3 {
        for _ in 0..licznik[wartosc] {
            lista[idx] = wartosc as u32;
            idx += 1;
        }
    }
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    let _n: usize = n_str.trim().parse().unwrap_or(0);

    let mut lista_str = String::new();
    io::stdin()
        .read_line(&mut lista_str)
        .expect("Błąd wczytywania");

    let mut lista: Vec<u32> = lista_str
        .trim()
        .split_whitespace()
        .filter_map(|s| s.parse().ok())
        .collect();

    sortuj_trojwartosciowa(&mut lista);

    print!("[");
    for (i, x) in lista.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("{}", x);
    }
    println!("]");
}
