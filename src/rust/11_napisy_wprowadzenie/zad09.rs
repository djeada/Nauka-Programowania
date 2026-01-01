/*
ZAD-09 — Rozdziel informacje o pracowniku

**Poziom:** ★☆☆
**Tagi:** `split`, `formatowanie`

### Treść

Wczytaj linię z danymi pracownika rozdzielonymi średnikami `;`:

1. Imię, 2) Nazwisko, 3) Miejsce urodzenia, 4) Stanowisko, 5) Zarobki

Wypisz każdą informację w osobnej linii z etykietą.

### Wejście

* 1. linia: dane w formacie `Imię; Nazwisko; Miasto; Zawód; Zarobki;`

### Wyjście

Pięć linii w formacie:

* `Imię: ...`
* `Nazwisko: ...`
* `Miejsce urodzenia: ...`
* `Zawód: ...`
* `Zarobki: ...`

### Przykład

**Wejście:**

```
Jan; Kowalski; Warszawa; Programista; 1000;
```

**Wyjście:**

```
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Warszawa
Zawód: Programista
Zarobki: 1000
```

### Uwagi

* Po `split(';')` usuń ewentualne spacje z brzegów pól (np. `strip()`).
* Ostatni średnik może powodować pusty element na końcu — zignoruj go.

*/

use std::io;

// Funkcja rozdzielająca dane pracownika
// Złożoność czasowa: O(n), gdzie n to długość linii
// Złożoność pamięciowa: O(n)
fn rozdziel_dane_pracownika(linia: &str) {
    let etykiety = ["Imię", "Nazwisko", "Miejsce urodzenia", "Zawód", "Zarobki"];
    let dane: Vec<&str> = linia
        .split(';')
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .collect();
    
    for (i, etykieta) in etykiety.iter().enumerate() {
        if i < dane.len() {
            println!("{}: {}", etykieta, dane[i]);
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let linia = input.trim();
    
    rozdziel_dane_pracownika(linia);
}
