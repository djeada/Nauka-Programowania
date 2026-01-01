/*
ZAD-07 — Zliczanie instancji klasy

**Poziom:** ★☆☆
**Tagi:** `class`, `static`

### Treść

Zaprojektuj klasę **MojaKlasa**, która zlicza ile instancji utworzono:

* prywatne pole statyczne licznik,
* konstruktor zwiększa licznik,
* metoda statyczna zwraca licznik.

Program tworzy np. 3 obiekty i wypisuje liczbę instancji.

### Wejście

Brak.

### Wyjście

Jedna linia.

### Przykład

**Wyjście:**

```
Liczba utworzonych instancji: 3
```

*/

use std::sync::atomic::{AtomicUsize, Ordering};

// Statyczny licznik instancji (thread-safe)
static LICZNIK_INSTANCJI: AtomicUsize = AtomicUsize::new(0);

// Struktura zliczająca instancje
// Złożoność pamięciowa: O(1) dla każdej instancji
struct MojaKlasa {
    _marker: (),
}

impl MojaKlasa {
    // Konstruktor zwiększający licznik
    fn new() -> Self {
        LICZNIK_INSTANCJI.fetch_add(1, Ordering::SeqCst);
        MojaKlasa { _marker: () }
    }
    
    // Metoda statyczna zwracająca licznik
    fn ile_instancji() -> usize {
        LICZNIK_INSTANCJI.load(Ordering::SeqCst)
    }
}

fn main() {
    // Tworzenie 3 instancji
    let _obj1 = MojaKlasa::new();
    let _obj2 = MojaKlasa::new();
    let _obj3 = MojaKlasa::new();
    
    println!("Liczba utworzonych instancji: {}", MojaKlasa::ile_instancji());
}
