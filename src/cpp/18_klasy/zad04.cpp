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

#include <cmath>
#include <iostream>

class Wektor {
 public:
  Wektor(double _x, double _y, double _z) : x(_x), y(_y), z(_z) {}

  void setX(double _x) { x = _x; }

  void setY(double _y) { y = _y; }

  void setZ(double _z) { z = _z; }

  double getX() { return x; }

  double getY() { return y; }

  double getZ() { return z; }

  double modul() {
    double kwadratX = pow(x, 2);
    double kwadratY = pow(y, 2);
    double kwadratZ = pow(z, 2);

    return sqrt(kwadratX + kwadratY + kwadratZ);
  }

  friend Wektor operator+(const Wektor &w1, const Wektor &w2) {
    Wektor w3(w1.x + w2.x, w1.y + w2.y, w1.z + w2.z);
    return w3;
  }

  friend Wektor operator-(const Wektor &w1, const Wektor &w2) {
    Wektor w3(w1.x - w2.x, w1.y - w2.y, w1.z - w2.z);
    return w3;
  }

  friend Wektor operator*(const Wektor &w1, const Wektor &w2) {
    double x = w1.y * w2.z - w1.z * w2.y;
    double y = w1.z * w2.x - w1.x * w2.z;
    double z = w1.x * w2.y - w1.y * w2.x;

    return Wektor(x, y, z);
  }

  friend std::ostream &operator<<(std::ostream &out, Wektor &w) {
    std::cout << "X = " << w.x << std::endl;
    std::cout << "Y = " << w.y << std::endl;
    std::cout << "Z = " << w.z << std::endl;
    return out;
  }
  friend bool operator==(const Wektor &w1, const Wektor &w2) {
    return w1.x == w2.x && w1.y == w2.y && w1.z == w2.z;
  }

  friend bool operator!=(const Wektor &w1, const Wektor &w2) {
    return w1.x != w2.x || w1.y != w2.y || w1.z != w2.z;
  }

 private:
  double x, y, z;
};

int main() {
  Wektor wektorA(5, 5, 5);
  Wektor wektorB(-3, -3, -3);

  auto suma = wektorA + wektorB;
  auto roznica = wektorA - wektorB;
  auto iloczynWek = wektorA * wektorB;

  std::cout << "Dla wektorow A \n"
            << wektorA << "oraz B \n"
            << wektorB << "otrzymujemy sume: \n"
            << suma << "roznice: \n"
            << roznica << "iloczyn wektorowy: \n"
            << iloczynWek << std::endl;

  return 0;
}
