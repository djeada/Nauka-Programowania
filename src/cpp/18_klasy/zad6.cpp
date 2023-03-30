/*
Tytul: Zaprojektuj klase Zespolona.
Tresc: Napisz klase Zespolona, ktora bedzie reprezentowala liczbe zespolona.
Klasa powinna zawierac nastepujace funkcje:
1. Konstruktor, ktory przyjmuje jako argument dwie liczby. Pierwsza liczba
reprezentuje czesc rzeczywista, a druga czesc urojona liczby zespolonej.
Domyslne wartosci dla obu argumentow to 0.
2. Funkcje, ktore zwracaja wynik podstawowych operacji arytmetycznych
(dodawanie, odejmowanie, mnozenie, dzielenie). Jesli jest to mozliwe, nalezy
przeciazyc operatory: +, -, *, /.
3. Funkcje, ktora wypisuje informacje o liczbie zespolonej na standardowe
wyjscie.
4. Funkcje umozliwiajace porownanie dwoch obiektow klasy Zespolona. Jesli jest
to mozliwe, nalezy przeciazyc operatory == oraz !=.
5. Funkcje modul, ktora zwraca modul liczby zespolonej.
Napisz program, ktory przetestuje twoja klase. Stworz liczby zespolone: A (9,
12) oraz B (-3, -3). Wypisz na standardowe wyjscie informacje o utworzonych
liczbach zespolonych oraz ich sume, roznice pierwszej i drugiej, iloraz
pierwszej przez druga oraz iloczyn liczb zespolonych.

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

