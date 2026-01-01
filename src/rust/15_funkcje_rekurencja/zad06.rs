/*
ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `delta`, `pierwiastki`, `I/O`

### Treść

Wczytaj współczynniki równania kwadratowego ( ax^2 + bx + c = 0 ). Wypisz wszystkie **rzeczywiste** miejsca zerowe w kolejności rosnącej.

### Wejście

* 1. linia: trzy liczby całkowite: `a b c` (oddzielone spacją)

### Wyjście

* Jeśli brak rzeczywistych pierwiastków: wypisz `[]`
* Jeśli jeden pierwiastek (delta = 0): wypisz go raz w formacie listy: `[x]`
* Jeśli dwa pierwiastki: wypisz w formacie listy: `[x1, x2]` gdzie `x1 ≤ x2`

**Format liczb:**

* wypisuj jako liczby zmiennoprzecinkowe (np. `-1.0`, `2.5`)

### Przykład

**Wejście:**

```
1 2 1
```

**Wyjście:**

```
[-1.0]
```

### Uwagi o formatowaniu

* Licz deltę: `Δ = b*b - 4*a*c`.
* Dla `Δ > 0`: policz oba pierwiastki i posortuj rosnąco.
* Zakładamy `a ≠ 0`.

*/

use std::io;

// Funkcja znajdująca rzeczywiste miejsca zerowe równania kwadratowego
// Złożoność czasowa: O(1)
// Złożoność pamięciowa: O(1)
fn miejsca_zerowe_kwadratowe(a: f64, b: f64, c: f64) -> Vec<f64> {
    let delta = b * b - 4.0 * a * c;
    
    if delta < 0.0 {
        Vec::new()
    } else if delta == 0.0 {
        let x = -b / (2.0 * a);
        vec![x]
    } else {
        let sqrt_delta = delta.sqrt();
        let x1 = (-b - sqrt_delta) / (2.0 * a);
        let x2 = (-b + sqrt_delta) / (2.0 * a);
        vec![x1.min(x2), x1.max(x2)]
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let coeffs: Vec<f64> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().expect("Nieprawidłowa liczba"))
        .collect();
    
    let wynik = miejsca_zerowe_kwadratowe(coeffs[0], coeffs[1], coeffs[2]);
    
    if wynik.is_empty() {
        println!("[]");
    } else if wynik.len() == 1 {
        println!("[{}]", wynik[0]);
    } else {
        print!("[");
        for (i, &x) in wynik.iter().enumerate() {
            if i > 0 {
                print!(", ");
            }
            print!("{}", x);
        }
        println!("]");
    }
}
