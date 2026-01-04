/*
ZAD-01 — Sprawdź poprawność adresu e-mail

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `walidacja`

### Treść

Otrzymujesz napis reprezentujący adres e-mail. Sprawdź, czy jest poprawny zgodnie z regułami:

* Adres e-mail składa się z identyfikatora użytkownika, znaku `@` oraz nazwy domeny.
* **Identyfikator użytkownika** może zawierać wyłącznie:

  * litery `a–z`, `A–Z`,
  * cyfry `0–9`,
  * znaki specjalne: `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`,
  * kropki `.`, ale:

    * nie może być pierwszym ani ostatnim znakiem,
    * nie może wystąpić dwukrotnie po sobie.
* **Nazwa domeny** może zawierać wyłącznie:

  * litery `a–z`, `A–Z`,
  * cyfry `0–9`,
  * kropki `.` oraz myślniki `-`, ale:

    * nie mogą być pierwszym ani ostatnim znakiem,
    * nie mogą wystąpić dwukrotnie po sobie.

### Wejście

Jedna linia:

* `email`

### Wyjście

Jedna linia:

* `Prawda` — jeśli e-mail jest poprawny
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
adam@gmail.com
```

**Wyjście:**

```
Prawda
```

*/

use std::io;

// Funkcja sprawdzająca poprawność adresu email (uproszczona)
// Złożoność czasowa: O(n), gdzie n to długość emaila
// Złożoność pamięciowa: O(1)
fn czy_poprawny_email(email: &str) -> bool {
    // Podstawowa walidacja bez pełnych regex
    let czesci: Vec<&str> = email.split('@').collect();

    if czesci.len() != 2 {
        return false;
    }

    let uzytkownik = czesci[0];
    let domena = czesci[1];

    // Sprawdź czy użytkownik niepusty
    if uzytkownik.is_empty() || domena.is_empty() {
        return false;
    }

    // Sprawdź czy nie zaczyna/kończy się kropką
    if uzytkownik.starts_with('.') || uzytkownik.ends_with('.') {
        return false;
    }

    // Sprawdź czy domena zawiera kropkę
    if !domena.contains('.') {
        return false;
    }

    // Sprawdź podwójne kropki
    if uzytkownik.contains("..") || domena.contains("..") {
        return false;
    }

    // Sprawdź czy domena nie zaczyna/kończy się kropką lub myślnikiem
    if domena.starts_with('.')
        || domena.ends_with('.')
        || domena.starts_with('-')
        || domena.ends_with('-')
    {
        return false;
    }

    true
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let email = input.trim();

    if czy_poprawny_email(email) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
