/*
Tytul: Minimalny iloczyn.
Tresc: Otrzymujesz liste liczb calkowitych. Znajdz najmniejszy iloczyn dla
trzech liczb wybranych z listy. Jesli lista sklada sie z mniej niz trzech liczb,
zwroc iloczyn wszystkich elementow listy. Dane wejsciowe: Lista liczb
calkowitych. Dane wyjsciowe: Liczba calkowita. Przyklad: Dla otrzymanej listy:
[3, -1, -3, 2, 9, 4], powinna zostac zwrocona liczba: -108.

*/
#include <algorithm>
#include <cassert>
#include <climits>
#include <vector>

// Zlozonosc czasowa O(nlogn)
// Zlozonosc pamieciowa O(1)
int minIloczynV1(std::vector<int> lista) {

  auto n = lista.size();

  if (n <= 2)
    throw std::invalid_argument("Lista musi miec co najmniej 3 elementy.");

  sort(lista.begin(), lista.end());

  return std::min(lista[n - 1] * lista[n - 2] * lista[0],
                  lista[0] * lista[1] * lista[2]);
}

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
int minIloczynV2(std::vector<int> lista) {

  auto n = lista.size();

  if (n <= 2)
    throw std::invalid_argument("Lista musi miec co najmniej 3 elementy.");

  std::vector<int> maksLewo(n, 0);
  std::vector<int> maksPrawo(n, 0);
  std::vector<int> minLewo(n, 0);
  std::vector<int> minPrawo(n, 0);

  auto minimum = INT_MAX;
  auto maksimum = INT_MIN;

  for (unsigned int i = 0; i < n; i++) {
    minLewo[i] = minimum;
    maksLewo[i] = maksimum;

    minimum = std::min(minimum, lista[i]);
    maksimum = std::max(maksimum, lista[i]);
  }

  minimum = INT_MAX;
  maksimum = INT_MIN;

  for (int i = n - 1; i >= 0; i--) {
    minPrawo[i] = minimum;
    maksPrawo[i] = maksimum;

    minimum = std::min(minimum, lista[i]);
    maksimum = std::max(maksimum, lista[i]);
  }

  auto wynik = INT_MAX;

  for (unsigned int i = 0; i < n - 2; i++)
    wynik = std::min(
        wynik, std::min({lista[i + 1] * minLewo[i + 1] * minPrawo[i + 1],
                         lista[i + 1] * minLewo[i + 1] * maksPrawo[i + 1],
                         lista[i + 1] * maksLewo[i + 1] * minPrawo[i + 1],
                         lista[i + 1] * maksLewo[i + 1] * maksPrawo[i + 1]}));

  return wynik;
}

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(1)
int minIloczynV3(std::vector<int> lista) {

  auto n = lista.size();

  if (n <= 2)
    throw std::invalid_argument("Lista musi miec co najmniej 3 elementy.");

  auto min1 = INT_MAX;
  auto min2 = INT_MAX;
  auto min3 = INT_MAX;
  auto maks1 = INT_MIN;
  auto maks2 = INT_MIN;

  for (auto &x : lista) {

    if (x < min1) {
      min3 = min2;
      min2 = min1;
      min1 = x;
    }

    else if (x < min2) {
      min3 = min2;
      min2 = x;
    }

    else if (x < min3)
      min3 = x;

    if (x > maks1) {
      maks2 = maks1;
      maks1 = x;
    }

    else if (x > maks2)
      maks2 = x;
  }

  return std::min(maks1 * maks2 * min1, min1 * min2 * min3);
}

// Testy Poprawnosci
void test1() {
  std::vector<int> lista{3, -1, -3, 2, 9, 4};
  int wynik = -108;

  assert(minIloczynV1(lista) == wynik);
  assert(minIloczynV2(lista) == wynik);
  assert(minIloczynV3(lista) == wynik);
}

void test2() {
  std::vector<int> lista{3, 2, 1, 7, 8};
  int wynik = 6;

  assert(minIloczynV1(lista) == wynik);
  assert(minIloczynV2(lista) == wynik);
  assert(minIloczynV3(lista) == wynik);
}

void test3() {
  std::vector<int> lista{1, 20, 2, -2, -4, -3};
  int wynik = -160;

  assert(minIloczynV1(lista) == wynik);
  assert(minIloczynV2(lista) == wynik);
  assert(minIloczynV3(lista) == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}

