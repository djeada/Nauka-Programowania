/*
ZAD-05 — Zbiór potęgowy listy

**Poziom:** ★★★
**Tagi:** `list`, `subsets`, `combinatorics`

### Treść

Otrzymujesz listę liczb naturalnych (mogą występować powtórzenia). Wygeneruj zbiór wszystkich możliwych podzbiorów tej listy.

Wynik ma zawierać wszystkie podzbiory (włącznie z pustym).

### Wejście

* 1 linia: lista liczb naturalnych `A`

### Wyjście

* 1 linia: lista list (wszystkie podzbiory)

### Przykład

**Wejście:**

```
[1, 2, 1]
```

**Wyjście:**

```
[[], [1], [2], [1, 2], [1, 1], [2, 1], [1, 1, 2], [1, 2, 1]]
```

### Uwagi

* Jeśli sprawdzarka wymaga konkretnej kolejności podzbiorów, musi być ona opisana w treści — w przeciwnym razie dopuszczalna może być dowolna. (Jeśli chcesz, mogę dopisać sztywną konwencję kolejności, ale bez rozwiązań.)

*/

use std::io;

// Funkcja generująca wszystkie podzbiory listy
// Złożoność czasowa: O(2^n), gdzie n to liczba elementów
// Złożoność pamięciowa: O(2^n)
fn zbior_potegowy(lista: &[i32]) -> Vec<Vec<i32>> {
    let n = lista.len();
    let mut wynik = Vec::new();

    // Generujemy wszystkie 2^n podzbiorów
    for i in 0..(1 << n) {
        let mut podzbior = Vec::new();
        for j in 0..n {
            if (i & (1 << j)) != 0 {
                podzbior.push(lista[j]);
            }
        }
        wynik.push(podzbior);
    }

    wynik
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");

    let lista_str = input.trim().trim_start_matches('[').trim_end_matches(']');

    let lista: Vec<i32> = lista_str
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect();

    let podzbiory = zbior_potegowy(&lista);

    // Wypisz wynik
    print!("[");
    for (i, podzbior) in podzbiory.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("[");
        for (j, &val) in podzbior.iter().enumerate() {
            if j > 0 {
                print!(", ");
            }
            print!("{}", val);
        }
        print!("]");
    }
    println!("]");
}
