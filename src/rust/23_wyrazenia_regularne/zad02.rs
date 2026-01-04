/*
ZAD-02 — Sprawdź poprawność hasła

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `walidacja`

### Treść

Otrzymujesz napis reprezentujący hasło. Sprawdź, czy hasło spełnia wszystkie warunki:

1. Zawiera co najmniej jedną małą literę `[a–z]`.
2. Zawiera co najmniej jedną wielką literę `[A–Z]`.
3. Zawiera co najmniej jedną cyfrę `[0–9]`.
4. Zawiera co najmniej jeden znak specjalny spośród:
   `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`.
5. Ma długość co najmniej 8 znaków.
6. Ma długość nie większą niż 20 znaków.

### Wejście

Jedna linia:

* `haslo`

### Wyjście

Jedna linia:

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
abc1234
```

**Wyjście:**

```
Fałsz
```

*/

use std::io;

// Funkcja sprawdzająca poprawność hasła
// Złożoność czasowa: O(n), gdzie n to długość hasła
// Złożoność pamięciowa: O(1)
fn czy_poprawne_haslo(haslo: &str) -> bool {
    let dlugosc = haslo.len();

    // Sprawdź długość
    if dlugosc < 8 || dlugosc > 20 {
        return false;
    }

    let mut ma_mala = false;
    let mut ma_wielka = false;
    let mut ma_cyfre = false;
    let mut ma_specjalny = false;

    let znaki_specjalne = "!#$%&'*+-/=?^_`{|}~";

    for c in haslo.chars() {
        if c.is_lowercase() {
            ma_mala = true;
        } else if c.is_uppercase() {
            ma_wielka = true;
        } else if c.is_digit(10) {
            ma_cyfre = true;
        } else if znaki_specjalne.contains(c) {
            ma_specjalny = true;
        }
    }

    ma_mala && ma_wielka && ma_cyfre && ma_specjalny
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let haslo = input.trim();

    if czy_poprawne_haslo(haslo) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
