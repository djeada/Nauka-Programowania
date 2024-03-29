/*
Tytul: Sortowanie listy miast.
Tresc: Klasa Miasto ma dwie wlasciwosci: nazwa (napis) oraz liczba_mieszkancow (liczba naturalna). Posortuj liste miast wzgledem nazwy oraz wzgledem liczby mieszkancow.
Dane wejsciowe: Lista miast.
Dane wyjsciowe: Posortowana lista miast.
Przyklad:
Dla listy miast: [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)], powinna zostac zwrocona lista: [Miasto("Berlin", 3800000), Miasto("New York", 8400000), Miasto("Paris", 2150000)].
Dla listy miast: [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)], powinna zostac zwrocona lista: [Miasto("Berlin", 3800000), Miasto("Paris", 2150000), Miasto("New York", 8400000)].

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

