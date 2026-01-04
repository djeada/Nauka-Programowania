/*
ZAD-05 — Dziedziczenie wielokrotne: Ptak

**Poziom:** ★★☆
**Tagi:** `multiple inheritance`, `dziedziczenie`, `metody`

### Treść

Zaprojektuj klasy:

* **Zwierz** — metody:

  * `jedz()` → wypisuje `Ptak je.`
  * `spij()` → wypisuje `Ptak śpi.`
  * `wydaj_dzwiek()` → wypisuje `Ptak wydaje dźwięk.`

* **ObiektLatajacy** — metody:

  * `lec()` → wypisuje `Ptak leci.`
  * `wyladuj()` → wypisuje `Ptak ląduje.`

* **Ptak** — dziedziczy po `Zwierz` oraz `ObiektLatajacy`.

Program testowy:

* tworzy obiekt `Ptak`,
* wywołuje metody w kolejności: `jedz`, `spij`, `wydaj_dzwiek`, `lec`, `wyladuj`.

### Wejście

Brak.

### Wyjście

Pięć linii jak w przykładzie.

### Przykład

**Wyjście:**

```
Ptak je.
Ptak śpi.
Ptak wydaje dźwięk.
Ptak leci.
Ptak ląduje.
```

*/

trait Zwierze {
    fn jedz(&self) {
        println!("Ptak je.");
    }

    fn spij(&self) {
        println!("Ptak śpi.");
    }

    fn wydaj_dzwiek(&self) {
        println!("Ptak wydaje dźwięk.");
    }
}

// Trait ObiektLatajacy
trait ObiektLatajacy {
    fn lec(&self) {
        println!("Ptak leci.");
    }

    fn wyladuj(&self) {
        println!("Ptak ląduje.");
    }
}

// Struktura Ptak implementująca oba trait'y
// Złożoność pamięciowa: O(1)
struct Ptak;

impl Ptak {
    fn new() -> Self {
        Ptak
    }
}

// Implementacja trait'ów dla Ptak
impl Zwierze for Ptak {}
impl ObiektLatajacy for Ptak {}

fn main() {
    let ptak = Ptak::new();

    ptak.jedz();
    ptak.spij();
    ptak.wydaj_dzwiek();
    ptak.lec();
    ptak.wyladuj();
}
