/*
Tytul: Obliczenie sredniej wazonej.
Tresc: Otrzymujesz dwie listy liczb zmiennoprzecinkowych. Pierwsza lista reprezentuje wagi, a druga wartosci. Oblicz srednia wazona.
Dane wejsciowe: Dwie listy liczb zmiennoprzecinkowych.
Dane wyjsciowe: Liczba zmiennoprzecinkowa.
Przyklad:
Dla otrzymanych list [2.0, 5.0, 0.0, 2.0, 1.0] oraz [0.2, 0.4, 0.1, 0.2, 0.1] zostanie zwrocona wartosc: 0.29.

*/
#include <cassert>
#include <numeric>
#include <vector>

double sredniaWazona(std::vector<double> &wagi, std::vector<double> &wartosci) {

  assert(wagi.size() == wartosci.size());

  double suma = accumulate(wartosci.begin(), wartosci.end(), 0);
  double sumaIloczynow = 0;

  for (unsigned int i = 0; i < wartosci.size(); i++)
    sumaIloczynow += (wartosci[i] * wagi[i]);

  return sumaIloczynow / suma;
}

void test1() {
  std::vector<double> wartosci{0, -23, -5, 2, -3, 4, 9};
  std::vector<double> wagi{1, 2, 3, 4, 5, 6, 7};

  double wynik = -1.1875;
  assert(sredniaWazona(wagi, wartosci) == wynik);
}

void test2() {
  std::vector<double> wartosci{2, 5, 0, 2, 1};
  std::vector<double> wagi{0.2, 0.4, 0.1, 0.2, 0.1};

  double wynik = 0.29;
  assert(sredniaWazona(wagi, wartosci) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

