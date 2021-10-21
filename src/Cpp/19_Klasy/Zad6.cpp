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
