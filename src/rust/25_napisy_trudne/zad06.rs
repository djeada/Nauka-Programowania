/*
ZAD-06 — Rotacje napisów

**Poziom:** ★★★
**Tagi:** `string`, `rotation`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Sprawdź, czy jeden z nich jest **rotacją** drugiego (mają tę samą długość i da się uzyskać jeden przez przesunięcie cykliczne drugiego).

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
malpka
pkamal
```

**Wyjście:**

```
Prawda
```

*/

use std::io;

// Funkcja sprawdzająca czy jeden napis jest rotacją drugiego
// Złożoność czasowa: O(n), gdzie n to długość napisów
// Złożoność pamięciowa: O(n)
fn czy_rotacja(a: &str, b: &str) -> bool {
    if a.len() != b.len() {
        return false;
    }

    // Trick: jeśli b jest rotacją a, to b będzie podnapisem a+a
    let podwojone_a = format!("{}{}", a, a);
    podwojone_a.contains(b)
}

fn main() {
    let mut a_str = String::new();
    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");
    let a = a_str.trim();

    let mut b_str = String::new();
    io::stdin().read_line(&mut b_str).expect("Błąd wczytywania");
    let b = b_str.trim();

    if czy_rotacja(a, b) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
