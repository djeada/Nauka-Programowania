/*
ZAD-06 — Sortowanie listy binarnej (0/1)

**Poziom:** ★★☆
**Tagi:** `sort`, `counting`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Posortuj ją rosnąco.

### Wejście

* 1 linia: liczba naturalna `N`
* 2 linia: `N` liczb (0/1) oddzielonych spacjami

### Wyjście

* 1 linia: posortowana lista w formacie jak w przykładzie

### Przykład

**Wejście:**

```
6
1 0 1 0 1 1
```

**Wyjście:**

```
[0, 0, 1, 1, 1, 1]
```

*/

use std::io;

// Funkcja sortująca listę binarną metodą zliczania
// Złożoność czasowa: O(n)
// Złożoność pamięciowa: O(1)
fn sortuj_binarna(lista: &mut Vec<u32>) {
    // Zliczamy wystąpienia 0 i 1
    let mut liczba_zer = 0;
    for &x in lista.iter() {
        if x == 0 {
            liczba_zer += 1;
        }
    }

    // Wypełniamy listę: najpierw zera, potem jedynki
    for i in 0..lista.len() {
        if i < liczba_zer {
            lista[i] = 0;
        } else {
            lista[i] = 1;
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

    sortuj_binarna(&mut lista);

    print!("[");
    for (i, x) in lista.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("{}", x);
    }
    println!("]");
}
