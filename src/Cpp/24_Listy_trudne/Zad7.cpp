#include <cassert>
#include <climits>
#include <vector>

/*
Otrzymujesz liste wysokosci slupkow. Wszystkie slupki maja jednakowa szerokosc,
rowna jednej jednostce wysokosci i ustawione sa jeden obok drugiego. Wysokosc
rowna 0 oznacza brak slupka. Oblicz ile jednostek wody mozemy maksymalnie
umiescic miedzy slupkami.
*/

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
int ileWodyV1(std::vector<int> &slupki) {

  auto n = slupki.size();
  auto woda = 0;

  std::vector<int> lewy{INT_MIN};

  for (auto i = 0; i < n; i++)
    lewy.push_back(std::max(lewy[i], slupki[i]));

  auto prawy = INT_MIN;

  for (int i = n - 1; i >= 0; i--) {

    prawy = std::max(prawy, slupki[i]);

    if (std::min(lewy[i], prawy) > slupki[i])
      woda += std::min(lewy[i], prawy) - slupki[i];
  }

  return woda;
}

// Testy Poprawnosci
void test1() {
  std::vector<int> lista{3, 0, 1, 0, 2};
  int wynik = 5;

  assert(ileWodyV1(lista) == wynik);
}

void test2() {
  std::vector<int> lista{9, 2, 3, 9, 0, 2};
  int wynik = 15;

  assert(ileWodyV1(lista) == wynik);
}

void test3() {
  std::vector<int> lista{1, 1};
  int wynik = 0;

  assert(ileWodyV1(lista) == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}
