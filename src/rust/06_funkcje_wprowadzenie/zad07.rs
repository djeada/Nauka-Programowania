/*
ZAD-07 — Weryfikacja nazwy użytkownika i hasła

**Poziom:** ★★☆
**Tagi:** `funkcje`, `while`, `string`, `porównania`

### Treść

Napisz dwie funkcje:

1. `pobierz_dane()` — pobiera od użytkownika nazwę użytkownika i hasło i zwraca je (np. jako parę).
2. `sprawdz_dane(poprawny_login, poprawne_haslo)` — w pętli wczytuje login i hasło aż będą identyczne z przekazanymi. Po poprawnym wczytaniu wypisuje:
   `Dane poprawne. Dostęp przyznany.`

### Wejście

* `pobierz_dane()` wczytuje dwie linie:

  1. login
  2. hasło
* `sprawdz_dane(...)` wczytuje kolejne pary (login, hasło), po dwie linie na próbę.

### Wyjście

Jedna linia (tylko raz, po poprawnym dopasowaniu):

* `Dane poprawne. Dostęp przyznany.`

### Ograniczenia / gwarancje

* W pewnym momencie użytkownik poda poprawne dane.

### Uwagi o formatowaniu

* **Nie wypisuj promptów** typu „Podaj nazwę użytkownika:”.
* Porównanie jest czułe na wielkość liter.

*/

fn pobierz_dane() -> (String, String) {
    let mut login = String::new();
    std::io::stdin().read_line(&mut login).unwrap();
    let login = login.trim().to_string();

    let mut haslo = String::new();
    std::io::stdin().read_line(&mut haslo).unwrap();
    let haslo = haslo.trim().to_string();

    (login, haslo)
}

fn sprawdz_dane(poprawny_login: &str, poprawne_haslo: &str) {
    loop {
        let (login, haslo) = pobierz_dane();
        if login == poprawny_login && haslo == poprawne_haslo {
            println!("Dane poprawne. Dostęp przyznany.");
            break;
        }
    }
}

fn main() {
    sprawdz_dane("admin", "haslo123");
}
