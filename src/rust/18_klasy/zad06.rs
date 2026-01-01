/*
ZAD-06 — Klasa LiczbaZespolona

**Poziom:** ★★☆
**Tagi:** `class`, `operacje`, `math`

### Treść

Zaprojektuj klasę **LiczbaZespolona**:

* konstruktor `(re=0, im=0)`,
* dodawanie, odejmowanie, mnożenie, dzielenie,
* porównania,
* moduł,
* wypisywanie w formacie `a + bi` lub `a - bi` (z zachowaniem znaku).

Program tworzy:

* A = 9 + 12i
* B = -3 - 3i

Wypisuje A, B oraz: sumę, różnicę A-B, iloczyn i iloraz A/B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Liczba A: 9 + 12i
Liczba B: -3 - 3i

Suma: 6 + 9i
Różnica A - B: 12 + 15i
Iloczyn: 27 + 63i
Iloraz A / B: -3.5 + 0.5i
```

*/

// Struktura reprezentująca liczbę zespoloną
// Złożoność pamięciowa: O(1)
#[derive(Debug, Clone, Copy, PartialEq)]
struct LiczbaZespolona {
    re: f64,  // część rzeczywista
    im: f64,  // część urojona
}

impl LiczbaZespolona {
    // Konstruktor
    fn new(re: f64, im: f64) -> Self {
        LiczbaZespolona { re, im }
    }
    
    // Dodawanie
    // Złożoność czasowa: O(1)
    fn dodaj(&self, other: &LiczbaZespolona) -> LiczbaZespolona {
        LiczbaZespolona::new(self.re + other.re, self.im + other.im)
    }
    
    // Odejmowanie
    // Złożoność czasowa: O(1)
    fn odejmij(&self, other: &LiczbaZespolona) -> LiczbaZespolona {
        LiczbaZespolona::new(self.re - other.re, self.im - other.im)
    }
    
    // Mnożenie
    // Złożoność czasowa: O(1)
    fn mnoz(&self, other: &LiczbaZespolona) -> LiczbaZespolona {
        LiczbaZespolona::new(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )
    }
    
    // Dzielenie
    // Złożoność czasowa: O(1)
    fn dziel(&self, other: &LiczbaZespolona) -> LiczbaZespolona {
        let mianownik = other.re * other.re + other.im * other.im;
        LiczbaZespolona::new(
            (self.re * other.re + self.im * other.im) / mianownik,
            (self.im * other.re - self.re * other.im) / mianownik,
        )
    }
    
    // Moduł
    // Złożoność czasowa: O(1)
    fn modul(&self) -> f64 {
        (self.re * self.re + self.im * self.im).sqrt()
    }
    
    // Wypisywanie w formacie a + bi lub a - bi
    fn wypisz(&self, nazwa: &str) {
        if !nazwa.is_empty() {
            print!("Liczba {}: ", nazwa);
        }
        
        if self.im >= 0.0 {
            println!("{} + {}i", self.re, self.im);
        } else {
            println!("{} - {}i", self.re, -self.im);
        }
    }
}

fn main() {
    let a = LiczbaZespolona::new(9.0, 12.0);
    let b = LiczbaZespolona::new(-3.0, -3.0);
    
    a.wypisz("A");
    b.wypisz("B");
    println!();
    
    let suma = a.dodaj(&b);
    print!("Suma: ");
    suma.wypisz("");
    
    let roznica = a.odejmij(&b);
    print!("Różnica A - B: ");
    roznica.wypisz("");
    
    let iloczyn = a.mnoz(&b);
    print!("Iloczyn: ");
    iloczyn.wypisz("");
    
    let iloraz = a.dziel(&b);
    print!("Iloraz A / B: ");
    iloraz.wypisz("");
}
