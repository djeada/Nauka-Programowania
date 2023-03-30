/*
Tytul: Wczytaj, zmodyfikuj i wypisz.
Tresc: Wczytaj liczbe calkowita N oraz N liczb calkowitych i umiesc je w liscie.
Nastepnie: a) Dodaj 1 do kazdego elementu listy. b) Pomnoz kazdy element przez
jego indeks w liscie (indeksy zaczynaja sie od 0). c) Zastap wszystkie elementy
wartoscia pierwszego elementu listy. Dla kazdego z powyzszych podpunktow wypisz
zmodyfikowana liste. Elementy listy powinny byc oddzielone przecinkami i
wypisane w jednym wierszu. Dane wejsciowe: N oraz N liczb calkowitych. Dane
wyjsciowe: N liczb calkowitych. Przyklad: Dla N rownego 3 oraz pobranych liczb
3, 9, 7 w pierwszym podpunkcie powinno zostac wypisana: 4, 10, 8.

*/
#include <cassert>
#include <cmath>
#include <vector>

int odleglosc(int x1, int y1, int x2, int y2) {
  int roznicaX = x1 - x2;
  int roznicaY = y1 - y2;
  int sumaKwadratow = pow(roznicaX, 2) + pow(roznicaY, 2);
  return sqrt(sumaKwadratow);
}

bool czyTrojkatV1(std::vector<int> &wsplX, std::vector<int> &wsplY) {

  assert(wsplX.size() == wsplY.size() && wsplX.size() == 3);

  int odlegloscAB = odleglosc(wsplX[0], wsplY[0], wsplX[1], wsplY[1]);
  int odlegloscBC = odleglosc(wsplX[2], wsplY[2], wsplX[1], wsplY[1]);
  int odlegloscAC = odleglosc(wsplX[0], wsplY[0], wsplX[2], wsplY[2]);

  return (odlegloscAB + odlegloscBC) > odlegloscAC &&
         (odlegloscAB + odlegloscAC) > odlegloscBC &&
         (odlegloscAC + odlegloscBC) > odlegloscAB;
}

bool czyTrojkatV2(std::vector<int> &wsplX, std::vector<int> &wsplY) {

  assert(wsplX.size() == wsplY.size() && wsplX.size() == 3);

  int a = wsplX[0] * (wsplY[1] - wsplY[2]) + wsplX[1] * (wsplY[2] - wsplY[0]) +
          wsplX[2] * (wsplY[0] - wsplY[1]);

  return a != 0;
}

void test1() {
  std::vector<int> wsplX{-2, 7, 8};
  std::vector<int> wsplY{4, 5, -8};
  assert(czyTrojkatV1(wsplX, wsplY));
  assert(czyTrojkatV2(wsplX, wsplY));
}

void test2() {
  std::vector<int> wsplX{0, 2, 5};
  std::vector<int> wsplY{0, -2, -5};
  assert(!czyTrojkatV1(wsplX, wsplY));
  assert(!czyTrojkatV2(wsplX, wsplY));
}

int main() {

  test1();
  test2();

  return 0;
}

