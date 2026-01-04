/*
ZAD-01 — Wywołanie metody klasy bazowej w klasie potomnej

**Poziom:** ★☆☆
**Tagi:** `dziedziczenie`, `override`, `super`

### Treść

Zaprojektuj dwie klasy:

1. **Bazowa** — posiada metodę `przedstaw_sie()`, która wypisuje komunikat o klasie bazowej.
2. **Potomna** — dziedziczy po **Bazowej** i **nadpisuje** metodę `przedstaw_sie()`, ale w swojej implementacji:

   * najpierw **wywołuje** wersję metody z klasy bazowej,
   * potem dopisuje własny komunikat.

Program testowy:

* tworzy obiekt klasy potomnej,
* wywołuje metodę `przedstaw_sie()`.

### Wejście

Brak.

### Wyjście

Dwie linie, pokazujące najpierw komunikat klasy bazowej, a potem potomnej.

### Przykład

**Wyjście:**

```
Jestem klasą bazową.
A ja jestem klasą potomną.
```

*/

struct Bazowa;

impl Bazowa {
    fn new() -> Self {
        Bazowa
    }

    fn przedstaw_sie(&self) {
        println!("Jestem klasą bazową.");
    }
}

// Struktura potomna zawierająca bazową
// Złożoność pamięciowa: O(1)
struct Potomna {
    bazowa: Bazowa,
}

impl Potomna {
    fn new() -> Self {
        Potomna {
            bazowa: Bazowa::new(),
        }
    }

    // Metoda nadpisująca, która najpierw wywołuje metodę bazową
    fn przedstaw_sie(&self) {
        self.bazowa.przedstaw_sie();
        println!("A ja jestem klasą potomną.");
    }
}

fn main() {
    let potomna = Potomna::new();
    potomna.przedstaw_sie();
}
