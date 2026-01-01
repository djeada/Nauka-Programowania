/*
ZAD-03 — Pole nałożenia się dwóch prostokątów

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `geometria`

### Treść

Zaprojektuj klasę **Prostokąt** opisaną przez dwa przeciwległe wierzchołki:

* lewy dolny `(x1, y1)`
* prawy górny `(x2, y2)`
  Boki równoległe do osi.

Klasa ma mieć:

1. Konstruktor `(x1, y1, x2, y2)`
2. Metodę statyczną `pole_wspolne(A, B)` zwracającą pole części wspólnej (albo 0).
3. Metodę wypisującą informacje o prostokącie.

Program tworzy:

* A: (3, 4) i (9, 6)
* B: (2, 2) i (7, 5)

Wypisuje oba i pole części wspólnej.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Prostokąt A: lewy dolny (3, 4), prawy górny (9, 6)
Prostokąt B: lewy dolny (2, 2), prawy górny (7, 5)
Pole części wspólnej: 6
```

*/

// Struktura reprezentująca prostokąt
// Złożoność pamięciowa: O(1)
struct Prostokat {
    x1: i32,
    y1: i32,
    x2: i32,
    y2: i32,
}

impl Prostokat {
    // Konstruktor
    fn new(x1: i32, y1: i32, x2: i32, y2: i32) -> Self {
        Prostokat { x1, y1, x2, y2 }
    }
    
    // Metoda statyczna obliczająca pole części wspólnej
    // Złożoność czasowa: O(1)
    fn pole_wspolne(a: &Prostokat, b: &Prostokat) -> i32 {
        // Znajdź współrzędne części wspólnej
        let x_lewy = a.x1.max(b.x1);
        let x_prawy = a.x2.min(b.x2);
        let y_dolny = a.y1.max(b.y1);
        let y_gorny = a.y2.min(b.y2);
        
        // Jeśli nie ma przecięcia
        if x_lewy >= x_prawy || y_dolny >= y_gorny {
            return 0;
        }
        
        // Oblicz pole
        let szerokosc = x_prawy - x_lewy;
        let wysokosc = y_gorny - y_dolny;
        szerokosc * wysokosc
    }
    
    // Metoda wypisująca informacje
    fn wypisz_info(&self, nazwa: &str) {
        println!("Prostokąt {}: lewy dolny ({}, {}), prawy górny ({}, {})",
                 nazwa, self.x1, self.y1, self.x2, self.y2);
    }
}

fn main() {
    let a = Prostokat::new(3, 4, 9, 6);
    let b = Prostokat::new(2, 2, 7, 5);
    
    a.wypisz_info("A");
    b.wypisz_info("B");
    
    let pole = Prostokat::pole_wspolne(&a, &b);
    println!("Pole części wspólnej: {}", pole);
}
