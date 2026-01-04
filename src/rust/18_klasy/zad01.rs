/*
ZAD-01 — Klasa Koło

**Poziom:** ★★☆
**Tagi:** `class`, `metody`, `float`, `math`

### Treść

Zaprojektuj klasę **Koło**:

1. Konstruktor przyjmuje promień `r` (domyślnie 1).
2. Metoda licząca **obwód**: ( 2\pi r )
3. Metoda licząca **pole**: ( \pi r^2 )
4. Metoda wypisująca informacje: promień, obwód i pole.

Program ma utworzyć koło o promieniu wczytanym z wejścia (np. 3) i wypisać informacje.

### Wejście

* 1 linia: `r` (liczba rzeczywista)

### Wyjście

Trzy linie jak w przykładzie (obwód i pole do 4 miejsc po przecinku).

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
Koło o promieniu: 3
Obwód koła: 18.8496
Pole koła: 28.2743
```

*/

use std::f64::consts::PI;
use std::io;

// Struktura reprezentująca koło
// Złożoność pamięciowa: O(1)
struct Kolo {
    promien: f64,
}

impl Kolo {
    // Konstruktor
    fn new(r: f64) -> Self {
        Kolo { promien: r }
    }

    // Metoda licząca obwód
    // Złożoność czasowa: O(1)
    fn obwod(&self) -> f64 {
        2.0 * PI * self.promien
    }

    // Metoda licząca pole
    // Złożoność czasowa: O(1)
    fn pole(&self) -> f64 {
        PI * self.promien * self.promien
    }

    // Metoda wypisująca informacje
    fn wypisz_info(&self) {
        println!("Koło o promieniu: {}", self.promien);
        println!("Obwód koła: {:.4}", self.obwod());
        println!("Pole koła: {:.4}", self.pole());
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let r: f64 = input.trim().parse().unwrap_or(1.0);

    let kolo = Kolo::new(r);
    kolo.wypisz_info();
}
