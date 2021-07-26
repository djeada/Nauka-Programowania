#include <cmath>

#include "zespolona.h"

Zespolona::Zespolona() {
  Re = 0;
  Im = 0;
}

Zespolona::Zespolona(double a, double b) {
  Re = a;
  Im = b;
}

double Zespolona::Modul() { return sqrt(Re * Re + Im * Im); }

void Zespolona::Sprzezenie() { Im *= -1; }

Zespolona operator+(const Zespolona &z1, const Zespolona &z2) {
  Zespolona z3(z1.Re + z2.Re, z1.Im + z2.Im);
  return z3;
}

Zespolona operator-(const Zespolona &z1, const Zespolona &z2) {
  Zespolona z3(z1.Re - z2.Re, z1.Im - z2.Im);
  return z3;
}

Zespolona operator*(const Zespolona &z1, const Zespolona &z2) {
  Zespolona z3(z1.Re * z2.Re - z1.Im * z2.Im, z1.Im * z2.Re + z2.Im * z1.Re);
  return z3;
}

Zespolona operator/(const Zespolona &z1, const Zespolona &z2) {
  double a = (z1.Re * z2.Re + z1.Im * z2.Im) / (z2.Re * z2.Re + z2.Im * z2.Im);
  double b = (z1.Re * z2.Im - z1.Im * z2.Re) / (z2.Re * z2.Re + z2.Im * z2.Im);
  Zespolona z3(a, b);
  return z3;
}

ostream &operator<<(ostream &out, const Zespolona &z) {
  if (z.Im >= 0)
    cout << z.Re << " + j" << z.Im << endl;
  else
    cout << z.Re << " - j" << abs(z.Im) << endl;
  return out;
}

bool operator==(const Zespolona &z1, const Zespolona &z2) {
  return z1.Re == z2.Re && z1.Im == z2.Im;
}
