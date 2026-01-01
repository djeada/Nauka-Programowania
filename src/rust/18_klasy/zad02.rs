/*
ZAD-02 — Klasa Punkt

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `porównania`, `math`

### Treść

Zaprojektuj klasę **Punkt**:

1. Konstruktor `(x=0, y=0)`.
2. Metoda statyczna `odleglosc(p1, p2)` licząca odległość.
3. Metoda wypisująca współrzędne.
4. Porównania `==` i `!=` (równe, gdy oba współrzędne identyczne).

Program tworzy:

* A = (5, 5)
* B = (-3, -3)

Wypisuje oba punkty i odległość między nimi (4 miejsca po przecinku).

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Punkt A: (5, 5)
Punkt B: (-3, -3)
Odległość między punktami A i B: 11.3137
```

*/

// Struktura reprezentująca punkt w przestrzeni 2D
// Złożoność pamięciowa: O(1)
#[derive(Debug, Clone, Copy, PartialEq)]
struct Punkt {
    x: f64,
    y: f64,
}

impl Punkt {
    // Konstruktor
    fn new(x: f64, y: f64) -> Self {
        Punkt { x, y }
    }
    
    // Metoda statyczna obliczająca odległość między dwoma punktami
    // Złożoność czasowa: O(1)
    fn odleglosc(p1: &Punkt, p2: &Punkt) -> f64 {
        let dx = p1.x - p2.x;
        let dy = p1.y - p2.y;
        (dx * dx + dy * dy).sqrt()
    }
    
    // Metoda wypisująca współrzędne
    fn wypisz(&self, nazwa: &str) {
        println!("Punkt {}: ({}, {})", nazwa, self.x, self.y);
    }
}

fn main() {
    let a = Punkt::new(5.0, 5.0);
    let b = Punkt::new(-3.0, -3.0);
    
    a.wypisz("A");
    b.wypisz("B");
    
    let odl = Punkt::odleglosc(&a, &b);
    println!("Odległość między punktami A i B: {:.4}", odl);
}
