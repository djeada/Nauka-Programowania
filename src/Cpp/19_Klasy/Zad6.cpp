/*
Napisz klase Zespolona reprezentujaca liczbe zespolona. W sklad klasy powinny wchodzic funkcje:
a) Konstruktor pobierajacy dwie liczby jako argumenty. Pierwsza liczba reprezentuje czesc 
rzeczywista, a druga czesc urojona liczby zespolonej. Domyslne wartosci dla obu argumentow to 0.
b) Funkcje zwracajace wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnozenie, 
dzielenie). Jesli jest to mozliwe nalezy przeciazyc operatory: +, -, *, /.
c) Funkcja wypisujaca informacje o liczbie zespolonej na standardowe wyjscie.
d) Funkcje umozliwiajace porownanie dwoch obiektow klasy Zespolona. Jesli jest to mozliwe nalezy 
przeciazyc operatory ==, !=.
e) Funkcja modul, zwracajaca modul liczby zespolonej. 

Napisz program testujacy twoja klase. Stworz liczby zespolone: A(9, 12) i B(-3, -3). Wypisz na 
standardowe wyjscie informacje o utworzonych liczbach zespolonych oraz ich sume, roznice pierwszej 
i drugiej, iloraz pierwszej przez druga oraz iloczyn liczb zespolonych.
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
