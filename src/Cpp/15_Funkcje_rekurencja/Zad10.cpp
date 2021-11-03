#include <cassert>
#include <string>

/*
Rozważ grę, w której w każdym ruchu gracz może zdobyć 3, 5 lub 10 punktów. 
Dla otrzymanej liczby N, reprezentującej całkowitą liczbę punktów, 
oblicz na ile sposobów gracz może wygrać grę.
*/

void gra(int n) {
  /**
   * Funkcja zwraca liczbę sposobów na wygraną w grze.
   */
  if (n < std::min(3, std::min(5, 10))) {
    return 0;

  std::vector<std::vector<int>> listaWynikow;


  auto _gra = [&](int n, std::vector<int> wynik) {
    
    if (n < 0) 
      return 0;

    if (n == 0) {
      std::sort(wynik.begin(), wynik.end());
      
      if (std::find(listaWynikow.begin(), listaWynikow.end(), wynik) == listaWynikow.end()) {
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

  assert (gra(0) == 0);
  assert (gra(10) == 2);
  assert (gra(20) == 4);
  assert (gra(50) == 14);

}
int main() {

  testGra();

  return 0;
}
