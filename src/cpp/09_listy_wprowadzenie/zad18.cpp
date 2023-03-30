/*
Tytul: Czy punkty moga stanowic wierzcholki trojkata?
Tresc: Otrzymujesz dokladnie 6 liczb calkowitych, ktore odpowiadaja wspolrzednym
punktow A, B, C w kolejnosci: xA, yA, xB, yB, xC, yC. Sprawdz, czy punkty A, B,
C moga stanowic wierzcholki trojkata. Dane wejsciowe: Lista liczb calkowitych
reprezentujaca wspolrzedne punktow A, B, C. Dane wyjsciowe: Wartosc logiczna
okreslajaca, czy punkty A, B, C moga stanowic wierzcholki trojkata. Przyklad:
Dla otrzymanej listy [-3, -2, -3, 1, -3, 0], powinna zostac zwrocona wartosc
logiczna: Falsz.

*/
#include <algorithm>
#include <cassert>
#include <vector>

int indeksMin(std::vector<int> &lista) {
  int n = lista.size();

  for (int i = 0; i < n - 1; i++) {
    if (lista[i] > lista[i + 1])
      return i + 1;
  }

  return 0;
}

void test1() {
  std::vector<int> lista{7, 8, -1, 4, 5};
  int wynik = 2;
  assert(indeksMin(lista) == wynik);
}

void test2() {
  std::vector<int> lista{2, 3, 4, 5, 6};
  int wynik = 0;
  assert(indeksMin(lista) == wynik);
}

void test3() {
  std::vector<int> lista{8, 9, 10, 11, 1};
  int wynik = 4;
  assert(indeksMin(lista) == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}

