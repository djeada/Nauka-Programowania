/*
ZAD-09A — Wielkie → małe (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis z liter alfabetu łacińskiego. Zamień wszystkie wielkie litery na małe, używając operacji bitowych na kodach ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
test
```

ZAD-09B — Małe → wielkie (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis. Zamień wszystkie małe litery na wielkie, używając operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
TEST
```

ZAD-09C — Odwróć wielkość liter (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `toggle case`

### Treść

Wczytaj napis. Zamień wielkość każdej litery na przeciwną (mała↔wielka) używając operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po zmianie.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
tEST
```

*/

use std::io;

// Funkcja konwertująca wielkie litery na małe (bitowo)
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n)
fn wielkie_na_male_bitowo(napis: &str) -> String {
    napis
        .chars()
        .map(|c| {
            if c.is_ascii_uppercase() {
                // Ustaw bit 5 (dodaj 32)
                ((c as u8) | 0x20) as char
            } else {
                c
            }
        })
        .collect()
}

// Funkcja konwertująca małe litery na wielkie (bitowo)
// Złożoność czasowa: O(n)
// Złożoność pamięciowa: O(n)
fn male_na_wielkie_bitowo(napis: &str) -> String {
    napis
        .chars()
        .map(|c| {
            if c.is_ascii_lowercase() {
                // Wyczyść bit 5 (odejmij 32)
                ((c as u8) & !0x20) as char
            } else {
                c
            }
        })
        .collect()
}

fn main() {
    // ZAD-09A: Wielkie → małe (bitowo)
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();
    
    println!("{}", wielkie_na_male_bitowo(napis));
    
    // ZAD-09B: Małe → wielkie (bitowo) (opcjonalnie)
    // println!("{}", male_na_wielkie_bitowo(napis));
}
