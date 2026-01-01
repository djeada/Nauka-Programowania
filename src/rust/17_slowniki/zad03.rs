/*
ZAD-03 — Biblioteka: baza wypożyczeń

**Poziom:** ★☆☆
**Tagi:** `dict`, `list`, `pętle`, `string`

### Treść

Utrzymuj słownik: `imię -> lista wypożyczonych książek`.
Obsługuj komendy (każda w osobnej linii) aż do `koniec`:

* `dodaj [imię] [tytuł]`
* `zwróć [imię] [tytuł]`
* `lista [imię]`

Po `lista [imię]` wypisz:

* jeśli lista niepusta: `Książki wypożyczone przez [imię]: t1, t2, ...`
* jeśli brak książek (lub brak czytelnika): `Książki wypożyczone przez [imię]: brak`

### Wejście

Wiele linii z komendami, koniec po słowie `koniec`.

### Wyjście

Tylko po komendach `lista ...`.

### Przykład

**Wejście:**

```
dodaj Jan Hobbit
dodaj Anna "Duma i uprzedzenie"
dodaj Jan "Władca Pierścieni"
lista Jan
zwróć Jan Hobbit
lista Jan
lista Anna
koniec
```

**Wyjście:**

```
Książki wypożyczone przez Jan: Hobbit, Władca Pierścieni
Książki wypożyczone przez Jan: Władca Pierścieni
Książki wypożyczone przez Anna: Duma i uprzedzenie
```

*/

use std::io;
use std::collections::HashMap;

// System zarządzania wypożyczeniami bibliotecznych
// Złożoność czasowa: O(n) dla każdej operacji
// Złożoność pamięciowa: O(n), gdzie n to liczba wypożyczeń

fn main() {
    let mut biblioteka: HashMap<String, Vec<String>> = HashMap::new();
    
    loop {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let linia = input.trim();
        
        if linia == "koniec" {
            break;
        }
        
        let czesci: Vec<&str> = linia.splitn(3, ' ').collect();
        
        if czesci.len() < 3 {
            continue;
        }
        
        let komenda = czesci[0];
        let imie = czesci[1].to_string();
        let tytul = czesci[2].trim_matches('"').to_string();
        
        match komenda {
            "dodaj" => {
                biblioteka.entry(imie).or_insert_with(Vec::new).push(tytul);
            }
            "zwróć" => {
                if let Some(ksiazki) = biblioteka.get_mut(&imie) {
                    ksiazki.retain(|k| k != &tytul);
                }
            }
            "lista" => {
                if let Some(ksiazki) = biblioteka.get(&czesci[1]) {
                    if ksiazki.is_empty() {
                        println!("Książki wypożyczone przez {}: brak", czesci[1]);
                    } else {
                        println!("Książki wypożyczone przez {}: {}", czesci[1], ksiazki.join(", "));
                    }
                } else {
                    println!("Książki wypożyczone przez {}: brak", czesci[1]);
                }
            }
            _ => {}
        }
    }
}
