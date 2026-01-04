/*
ZAD-08 — Cyfry w słowach

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz zdanie. Wyodrębnij wszystkie ciągi cyfr, które są częścią słów (czyli są bezpośrednio połączone z literami). Nie uwzględniaj cyfr oddzielonych od liter spacjami.

### Wejście

Jedna linia:

* `zdanie`

### Wyjście

Każdy znaleziony ciąg cyfr w osobnej linii (w kolejności występowania).

### Przykład

**Wejście:**

```
Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego
```

**Wyjście:**

```
29
37
3
91
```

*/

use std::io;

// Funkcja wyodrębniająca cyfry będące częścią słów
// Złożoność czasowa: O(n), gdzie n to długość zdania
// Złożoność pamięciowa: O(n)
fn wyodrebnij_cyfry_w_slowach(zdanie: &str) -> Vec<String> {
    let mut wynik = Vec::new();
    let mut biezacy_ciag = String::new();
    let mut w_slowie = false;

    let chars: Vec<char> = zdanie.chars().collect();

    for (i, &c) in chars.iter().enumerate() {
        if c.is_alphanumeric() {
            if c.is_digit(10) {
                // Sprawdź czy jesteśmy w słowie (czy poprzedni/następny znak to litera)
                let poprzedni_litera = i > 0 && chars[i - 1].is_alphabetic();
                let nastepny_litera = i + 1 < chars.len() && chars[i + 1].is_alphabetic();

                if poprzedni_litera || nastepny_litera || w_slowie {
                    biezacy_ciag.push(c);
                    w_slowie = true;
                }
            } else {
                // To litera
                if !biezacy_ciag.is_empty() {
                    wynik.push(biezacy_ciag.clone());
                    biezacy_ciag.clear();
                }
                w_slowie = true;
            }
        } else {
            // Koniec słowa
            if !biezacy_ciag.is_empty() {
                wynik.push(biezacy_ciag.clone());
                biezacy_ciag.clear();
            }
            w_slowie = false;
        }
    }

    if !biezacy_ciag.is_empty() {
        wynik.push(biezacy_ciag);
    }

    wynik
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let zdanie = input.trim();

    let cyfry = wyodrebnij_cyfry_w_slowach(zdanie);

    for ciag in cyfry {
        println!("{}", ciag);
    }
}
