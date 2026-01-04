/*
ZAD-03 — Polimorfizm: Zwierz, Pies i Kot

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `override`

### Treść

Zaprojektuj klasy:

* **Zwierz** — metoda `odglos()` zwraca/drukuje ogólny dźwięk.
* **Pies** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.
* **Kot** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.

Program testowy:

* tworzy obiekty: `Zwierz`, `Pies`, `Kot`,
* umieszcza je w jednej kolekcji,
* iteruje i dla każdego wypisuje linię w formacie:
  `NazwaKlasy wydaje odgłos: ...`

### Wejście

Brak.

### Wyjście

Trzy linie, po jednej dla każdego obiektu.

### Przykład

**Wyjście:**

```
Zwierz wydaje odgłos: ...
Pies wydaje odgłos: Hau!
Kot wydaje odgłos: Miau!
```

*/

trait Zwierze {
    fn odglos(&self) -> &str;
    fn nazwa_klasy(&self) -> &str;
}

// Struktura bazowa Zwierz
// Złożoność pamięciowa: O(1)
struct ZwierzBazowy;

impl Zwierze for ZwierzBazowy {
    fn odglos(&self) -> &str {
        "..."
    }

    fn nazwa_klasy(&self) -> &str {
        "Zwierz"
    }
}

// Struktura Pies
// Złożoność pamięciowa: O(1)
struct Pies;

impl Zwierze for Pies {
    fn odglos(&self) -> &str {
        "Hau!"
    }

    fn nazwa_klasy(&self) -> &str {
        "Pies"
    }
}

// Struktura Kot
// Złożoność pamięciowa: O(1)
struct Kot;

impl Zwierze for Kot {
    fn odglos(&self) -> &str {
        "Miau!"
    }

    fn nazwa_klasy(&self) -> &str {
        "Kot"
    }
}

fn main() {
    // Tworzymy kolekcję zwierząt używając Box<dyn Zwierze> dla polimorfizmu
    let zwierzeta: Vec<Box<dyn Zwierze>> =
        vec![Box::new(ZwierzBazowy), Box::new(Pies), Box::new(Kot)];

    // Iterujemy i wypisujemy odgłosy
    for zwierze in zwierzeta.iter() {
        println!(
            "{} wydaje odgłos: {}",
            zwierze.nazwa_klasy(),
            zwierze.odglos()
        );
    }
}
