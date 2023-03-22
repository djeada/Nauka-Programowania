/*
Klasa Miasto sklada sie z dwoch pol: nazwa (napis) oraz liczba_mieszkancow (liczba naturalna). 
a) Posortuj liste obiektow klasy Miasto wzgledem pola nazwa.
b) Posortuj liste obiektow klasy Miasto wzgledem pola liczba_mieszkancow.
*/

#include <algorithm>
#include <cassert>
#include <string>
#include <vector>


class Miasto {
  std::string nazwa;
  int liczbaMieszkancow;

public:
  Miasto(std::string _nazwa, int _liczbaMieszkancow)
      : nazwa(_nazwa), liczbaMieszkancow(_liczbaMieszkancow){};

  bool operator==(const Miasto &m) const {
    return nazwa == m.getNazwa() &&
           liczbaMieszkancow == m.getLiczbaMieszkancow();
  }

  std::string getNazwa() const { return nazwa; };
  int getLiczbaMieszkancow() const { return liczbaMieszkancow; };
};

void sortujWzgledemNazwy(std::vector<Miasto> &lista) {
  std::sort(lista.begin(), lista.end(),
            [](auto rhs, auto lhs) { return rhs.getNazwa() < lhs.getNazwa(); });
}

void sortujWzgledemLiczby(std::vector<Miasto> &lista) {
  std::sort(lista.begin(), lista.end(), [](auto rhs, auto lhs) {
    return rhs.getLiczbaMieszkancow() < lhs.getLiczbaMieszkancow();
  });
}

void test1() {
  std::vector<Miasto> miasta{Miasto("New York", 8400000),
                             Miasto("Paris", 2150000),
                             Miasto("Berlin", 3800000)};
  std::vector<Miasto> wynik{Miasto("Berlin", 3800000),
                            Miasto("New York", 8400000),
                            Miasto("Paris", 2150000)};

  sortujWzgledemNazwy(miasta);

  assert(miasta == wynik);
}

void test2() {
  std::vector<Miasto> miasta{Miasto("New York", 8400000),
                             Miasto("Paris", 2150000),
                             Miasto("Berlin", 3800000)};

  std::vector<Miasto> wynik{Miasto("Paris", 2150000), Miasto("Berlin", 3800000),
                            Miasto("New York", 8400000)};
  sortujWzgledemLiczby(miasta);

  assert(miasta == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}