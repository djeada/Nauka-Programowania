/*
Tytul: Gra.
Tresc: W grze, w kazdym ruchu gracz moze zdobyc 3, 5 lub 10 punktow. Oblicz przy
uzyciu rekurencji, ile sposobow istnieje, aby gracz wygral gre, gdy ma do
dyspozycji N punktow. Dane wejsciowe: Liczba naturalna N. Dane wyjsciowe: Liczba
naturalna. Przyklad: Dla N = 20, powinna zostac zwrocona liczba: 4.

*/
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>

// Zlozonosc Czasowa: O(3^n)
// Zlozonosc Pamieciowa: O(n) - przez stos rekurencji
int gra(int n) {
  /**
   * Funkcja zwraca liczbe sposobow na wygrana w grze.
   */
  if (n < std::min(3, std::min(5, 10))) {
    return 0;
  }

  std::vector<std::vector<int>> listaWynikow;

  std::function<int(int, std::vector<int>)> _gra = 
      [&](int n, std::vector<int> wynik) -> int {
    if (n < 0) return 0;

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
