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

use std::collections::HashMap;
use std::io;

// System zarządzania wypożyczeniami bibliotecznych
// Złożoność czasowa: O(n) dla każdej operacji
// Złożoność pamięciowa: O(n), gdzie n to liczba wypożyczeń

fn main() {
    let mut biblioteka: HashMap<String, Vec<String>> = HashMap::new();

    loop {
        let mut input = String::new();
        let wczytane = io::stdin()
            .read_line(&mut input)
            .expect("Błąd wczytywania");
        let linia = input.trim();

        if wczytane == 0 || linia == "koniec" {
            break;
        }

        let czesci: Vec<&str> = linia.splitn(3, ' ').collect();

        match czesci.as_slice() {
            ["dodaj", imie, tytul] => {
                biblioteka
                    .entry(imie.to_string())
                    .or_insert_with(Vec::new)
                    .push(tytul.trim_matches('"').to_string());
            }
            ["zwróć", imie, tytul] => {
                let tytul = tytul.trim_matches('"');
                if let Some(ksiazki) = biblioteka.get_mut(*imie) {
                    ksiazki.retain(|k| k != tytul);
                }
            }
            ["lista", imie, ..] => match biblioteka.get(*imie) {
                Some(ksiazki) if !ksiazki.is_empty() => {
                    println!(
                        "Książki wypożyczone przez {}: {}",
                        imie,
                        ksiazki.join(", ")
                    );
                }
                _ => println!("Książki wypożyczone przez {}: brak", imie),
            },
            _ => {}
        }
    }
}
