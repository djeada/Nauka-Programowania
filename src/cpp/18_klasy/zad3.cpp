/*
Tytul: Prostokat powstaly z nalozenia sie dwoch prostokatow.
Opis zadania: Napisz klase Prostokat, ktora bedzie reprezentowala prostokat w
ukladzie kartezjanskim. Prostokat jest okreslony przez wspolrzedne jego czterech
wierzcholkow. Boki prostokata sa prostopadle do osi ukladu wspolrzednych. Klasa
powinna zawierac funkcje statyczna, ktora zwraca pole prostokata powstalego z
nalozenia sie dwoch prostokatow. Jesli dwa prostokaty nie pokrywaja sie, funkcja
powinna zwracac 0. Napisz program, ktory przetestuje twoja klase. Stworz
prostokaty: A (3, 6, 9, 4) oraz B (2, 5, 7, 2). Wypisz na standardowe wyjscie
informacje o utworzonych prostokatach. Sprawdz, czy pole czesci wspolnej rowne
jest 6.

*/

#include <cassert>
#include <cmath>

class Prostokat {
public:
  Prostokat(double _lewo, double _prawo, double _gora, double _dol)
      : lewo(_lewo), prawo(_prawo), gora(_gora), dol(_dol) {}

  double getLewo() { return lewo; }

  double getPrawo() { return prawo; }

  double getGora() { return gora; }

  double getDol() { return dol; }

  double poleCzesciWspolnej(Prostokat &innyProstokat) {
    double poleX = std::max(0.00, std::min(prawo, innyProstokat.getPrawo()) -
                                      std::max(lewo, innyProstokat.getLewo()));
    double poleY = std::max(0.00, std::min(gora, innyProstokat.getGora()) -
                                      std::max(dol, innyProstokat.getDol()));
    return poleX * poleY;
  }

private:
  double lewo, prawo, gora, dol;
};

void test1() {
  Prostokat prostokatA(2, 5, 7, 2);
  Prostokat prostokatB(3, 6, 9, 4);
  double wynik = 6.00;

  assert(prostokatA.poleCzesciWspolnej(prostokatB) == wynik);
}

void test2() {
  Prostokat prostokatA(-9.5, 10.5, 6, 2);
  Prostokat prostokatB(-4.5, 2.3, 3.8, -3.3);
  double wynik = 12.24;

  assert(abs(prostokatA.poleCzesciWspolnej(prostokatB) - wynik) < 0.01);
}

int main() {

  test1();
  test2();

  return 0;
}

