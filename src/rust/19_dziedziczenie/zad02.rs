/*
ZAD-02 — Klasa Kształt oraz klasy Koło i Kwadrat

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `math`

### Treść

Zaprojektuj hierarchię klas:

* **Kształt** — klasa bazowa (ogólna) dla kształtów.
* **Koło** — dziedziczy po `Kształt`.
* **Kwadrat** — dziedziczy po `Kształt`.

Każda klasa ma mieć:

* metodę obliczającą **pole**,
* metodę wypisującą informacje o obiekcie: typ, parametry i pole.

Program:

* wczytuje promień `r` koła oraz bok `a` kwadratu,
* tworzy obiekty `Koło(r)` i `Kwadrat(a)`,
* wypisuje informacje o obu.

**Uwaga do formatowania:**
*Pole koła wypisz do 4 miejsc po przecinku.*
*Pole kwadratu wypisz bez wymuszania miejsc po przecinku (jak w przykładzie).*

### Wejście

* 1 linia: `r` (liczba rzeczywista)
* 2 linia: `a` (liczba rzeczywista)

### Wyjście

Blok informacji o kole, pusta linia, blok informacji o kwadracie.

### Przykład

**Wejście:**

```
5
4
```

**Wyjście:**

```
Kształt: Koło
Promień: 5
Pole powierzchni: 78.5398

Kształt: Kwadrat
Długość boku: 4
Pole powierzchni: 16
```

*/

use std::f64::consts::PI;
use std::io;

// Trait reprezentujący kształt (interfejs polimorficzny)
trait Ksztalt {
    fn pole(&self) -> f64;
    fn wypisz_info(&self);
}

// Struktura reprezentująca koło
// Złożoność pamięciowa: O(1)
struct Kolo {
    promien: f64,
}

impl Kolo {
    fn new(promien: f64) -> Self {
        Kolo { promien }
    }
}

impl Ksztalt for Kolo {
    // Złożoność czasowa: O(1)
    fn pole(&self) -> f64 {
        PI * self.promien * self.promien
    }

    fn wypisz_info(&self) {
        println!("Kształt: Koło");
        println!("Promień: {}", self.promien);
        println!("Pole powierzchni: {:.4}", self.pole());
    }
}

// Struktura reprezentująca kwadrat
// Złożoność pamięciowa: O(1)
struct Kwadrat {
    bok: f64,
}

impl Kwadrat {
    fn new(bok: f64) -> Self {
        Kwadrat { bok }
    }
}

impl Ksztalt for Kwadrat {
    // Złożoność czasowa: O(1)
    fn pole(&self) -> f64 {
        self.bok * self.bok
    }

    fn wypisz_info(&self) {
        println!("Kształt: Kwadrat");
        println!("Długość boku: {}", self.bok);
        println!("Pole powierzchni: {}", self.pole() as i32);
    }
}

fn main() {
    let mut r_str = String::new();
    let mut a_str = String::new();

    io::stdin().read_line(&mut r_str).expect("Błąd wczytywania");
    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");

    let r: f64 = r_str.trim().parse().unwrap_or(1.0);
    let a: f64 = a_str.trim().parse().unwrap_or(1.0);

    let kolo = Kolo::new(r);
    let kwadrat = Kwadrat::new(a);

    kolo.wypisz_info();
    println!();
    kwadrat.wypisz_info();
}
