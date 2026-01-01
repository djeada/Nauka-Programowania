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

#include <cmath>
#include <iostream>

using namespace std;

class Zespolona {
 private:
  double Re;
  double Im;

 public:
  Zespolona() {
    Re = 0;
    Im = 0;
  }

  Zespolona(double a, double b) {
    Re = a;
    Im = b;
  }

  double Modul() { return sqrt(Re * Re + Im * Im); }

  void Sprzezenie() { Im *= -1; }

  friend Zespolona operator+(const Zespolona &z1, const Zespolona &z2) {
    Zespolona z3(z1.Re + z2.Re, z1.Im + z2.Im);
    return z3;
  }

  friend Zespolona operator-(const Zespolona &z1, const Zespolona &z2) {
    Zespolona z3(z1.Re - z2.Re, z1.Im - z2.Im);
    return z3;
  }

  friend Zespolona operator*(const Zespolona &z1, const Zespolona &z2) {
    Zespolona z3(z1.Re * z2.Re - z1.Im * z2.Im, z1.Im * z2.Re + z2.Im * z1.Re);
    return z3;
  }

  friend Zespolona operator/(const Zespolona &z1, const Zespolona &z2) {
    double a =
        (z1.Re * z2.Re + z1.Im * z2.Im) / (z2.Re * z2.Re + z2.Im * z2.Im);
    double b =
        (z1.Re * z2.Im - z1.Im * z2.Re) / (z2.Re * z2.Re + z2.Im * z2.Im);
    Zespolona z3(a, b);
    return z3;
  }

  friend ostream &operator<<(ostream &out, const Zespolona &z) {
    if (z.Im >= 0)
      cout << z.Re << " + j" << z.Im << endl;
    else
      cout << z.Re << " - j" << abs(z.Im) << endl;
    return out;
  }

  friend bool operator==(const Zespolona &z1, const Zespolona &z2) {
    return z1.Re == z2.Re && z1.Im == z2.Im;
  }
};

int main() {
  Zespolona z1;
  Zespolona z2(9, 12);

  std::cout << z1;
  std::cout << z2;

  std::cout << z1 * z2;

  Zespolona z3(-3, -3);

  std::cout << z3 + z2;
  std::cout << z3 / z2;

  z2.Sprzezenie();

  std::cout << z2;

  std::cout << z3.Modul() << std::endl;

  return 0;
}
