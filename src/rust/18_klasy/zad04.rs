/*
ZAD-04 — Klasy Wektor2D i Wektor3D

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasy **Wektor2D** i **Wektor3D**:

Wspólne:

* konstruktor z domyślnymi współrzędnymi 0,
* dodawanie, odejmowanie,
* iloczyn skalarny,
* porównania `==` i `!=`,
* moduł (długość),
* metoda wypisująca wektor.

Dodatkowo dla **Wektor3D**:

* iloczyn wektorowy.

Program tworzy:

* A = (-3, -3, -3)
* B = (5, 5, 5)

Wypisuje A, B oraz:

* A + B
* A - B
* A · B
* A × B

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Wektor A: (-3, -3, -3)
Wektor B: (5, 5, 5)
Suma wektorów: (2, 2, 2)
Różnica wektorów A - B: (-8, -8, -8)
Iloczyn skalarny: -45
Iloczyn wektorowy: (0, 0, 0)
```

*/

#[derive(Debug, Clone, Copy, PartialEq)]
struct Wektor3D {
    x: f64,
    y: f64,
    z: f64,
}

impl Wektor3D {
    // Konstruktor
    fn new(x: f64, y: f64, z: f64) -> Self {
        Wektor3D { x, y, z }
    }

    // Dodawanie wektorów
    // Złożoność czasowa: O(1)
    fn dodaj(&self, other: &Wektor3D) -> Wektor3D {
        Wektor3D::new(self.x + other.x, self.y + other.y, self.z + other.z)
    }

    // Odejmowanie wektorów
    // Złożoność czasowa: O(1)
    fn odejmij(&self, other: &Wektor3D) -> Wektor3D {
        Wektor3D::new(self.x - other.x, self.y - other.y, self.z - other.z)
    }

    // Iloczyn skalarny
    // Złożoność czasowa: O(1)
    fn iloczyn_skalarny(&self, other: &Wektor3D) -> f64 {
        self.x * other.x + self.y * other.y + self.z * other.z
    }

    // Iloczyn wektorowy (tylko dla 3D)
    // Złożoność czasowa: O(1)
    fn iloczyn_wektorowy(&self, other: &Wektor3D) -> Wektor3D {
        Wektor3D::new(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )
    }

    // Moduł (długość) wektora
    // Złożoność czasowa: O(1)
    fn modul(&self) -> f64 {
        (self.x * self.x + self.y * self.y + self.z * self.z).sqrt()
    }

    // Metoda wypisująca wektor
    fn wypisz(&self, nazwa: &str) {
        println!("Wektor {}: ({}, {}, {})", nazwa, self.x, self.y, self.z);
    }
}

fn main() {
    let a = Wektor3D::new(-3.0, -3.0, -3.0);
    let b = Wektor3D::new(5.0, 5.0, 5.0);

    a.wypisz("A");
    b.wypisz("B");

    let suma = a.dodaj(&b);
    print!("A + B = ");
    suma.wypisz("");

    let roznica = a.odejmij(&b);
    print!("A - B = ");
    roznica.wypisz("");

    let iloczyn_skal = a.iloczyn_skalarny(&b);
    println!("A · B = {}", iloczyn_skal);

    let iloczyn_wekt = a.iloczyn_wektorowy(&b);
    print!("A × B = ");
    iloczyn_wekt.wypisz("");
}
