/*
Tytul: Suma liczb naturalnych mniejszych od N.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz sume liczb
naturalnych mniejszych od N. Dane wejsciowe: Liczba naturalna N. Dane wyjsciowe:
Liczba naturalna. Przyklad: Dla N = 10, powinna zostac zwrocona liczba: 55.

*/
#include <cassert>
#include <string>

void gra(int n) {
  /**
   * Funkcja zwraca liczbe sposobow na wygrana w grze.
   */
  if (n < std::min(3, std::min(5, 10))) {
    return 0;

    std::vector<std::vector<int>> listaWynikow;

    auto _gra = [&](int n, std::vector<int> wynik) {
      if (n < 0)
        return 0;

      if (n == 0) {
        std::sort(wynik.begin(), wynik.end());

        if (std::find(listaWynikow.begin(), listaWynikow.end(), wynik) ==
            listaWynikow.end()) {
          listaWynikow.push_back(wynik);
          return 1;
        }
        return 0;
      }

      return _gra(n - 3, wynik) + _gra(n - 5, wynik) + _gra(n - 10, wynik);
    };

    return _gra(n, std::vector<int>());
  }
}

void testGra() {

  assert(gra(0) == 0);
  assert(gra(10) == 2);
  assert(gra(20) == 4);
  assert(gra(50) == 14);
}
int main() {

  testGra();

  return 0;
}

