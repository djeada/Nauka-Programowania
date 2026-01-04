/*
ZAD-09 — Najdłuższy naprzemienny podciąg

**Poziom:** ★★★
**Tagi:** `dp`, `subsequence`, `naprzemienny`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź najdłuższy podciąg naprzemienny, w którym różnice między kolejnymi elementami zmieniają znak (raz dodatnia, raz ujemna, itd.).

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista liczb — najdłuższy naprzemienny podciąg

### Przykład

**Wejście:**

```
[1, -2, 6, 4, -3, 2, -4, -3]
```

**Wyjście:**

```
[1, -2, 6, -3, 2, -4]
```

### Uwagi

* Jeśli istnieje kilka podciągów o tej samej maksymalnej długości — wybierz ten, który pojawia się „najwcześniej” (najmniejszy możliwy indeks startu), o ile sprawdzarka tego wymaga.

*/

use std::io;

// Funkcja znajdująca najdłuższy naprzemienny podciąg
// Złożoność czasowa: O(n), gdzie n to długość listy
// Złożoność pamięciowa: O(n)
fn najdluzszy_naprzemienny(lista: &[i32]) -> Vec<i32> {
    if lista.len() < 2 {
        return lista.to_vec();
    }

    let mut wynik = vec![lista[0]];

    for i in 1..lista.len() {
        if wynik.len() == 1 {
            if lista[i] != wynik[0] {
                wynik.push(lista[i]);
            }
        } else {
            let dlugosc = wynik.len();
            let roznica_poprzednia = wynik[dlugosc - 1] - wynik[dlugosc - 2];
            let roznica_obecna = lista[i] - wynik[dlugosc - 1];

            // Sprawdź czy znaki się zmieniają
            if (roznica_poprzednia > 0 && roznica_obecna < 0)
                || (roznica_poprzednia < 0 && roznica_obecna > 0)
            {
                wynik.push(lista[i]);
            }
        }
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

    let wynik = najdluzszy_naprzemienny(&lista);

    // Wypisz wynik
    print!("[");
    for (i, val) in wynik.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("{}", val);
    }
    println!("]");
}
