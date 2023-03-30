/*
Tytul: Zaprojektuj klasy Wektor2D oraz Wektor3D.
Tresc:  Napisz klasy Wektor2D oraz Wektor3D, ktore beda reprezentowaly odpowiednio wektory w przestrzeni dwuwymiarowej i trzywymiarowej. Klasy powinny zawierac nastepujace funkcje:
1. Konstruktor, ktory przyjmuje dwa (trzy) argumenty (liczby). Liczby reprezentuja wspolrzedne wektora. Domyslne wartosci dla wszystkich argumentow powinny wynosic 0.
2. Funkcje, ktore zwracaja wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie) oraz iloczyn wektorowy i skalarny. Jesli jest to mozliwe, nalezy przeciazyc operatory: +, -, *.
3. Funkcje, ktora wypisuje informacje o wektorze na standardowe wyjscie.
4. Funkcje umozliwiajace porownanie dwoch obiektow klasy Wektor2D (Wektor3D). Jesli jest to mozliwe, nalezy przeciazyc operatory == oraz !=.
5. Funkcje modul, ktora zwraca modul wektora.
Napisz program, ktory przetestuje twoja klase. Stworz wektory: A (-3, -3, -3) oraz B (5, 5, 5). Wypisz na standardowe wyjscie informacje o utworzonych wektorach oraz sume wektorow, roznice pierwszego i drugiego oraz ich iloczyn wektorowy.

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

