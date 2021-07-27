#include <cassert>
#include <vector>

/*
Otrzymujesz liste liczb. Znajdz najdluzszy naprzemienny podciag w liscie.
*/

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(1)
std::vector<int> najdluzszyNaprzemiennyPodciagV1(std::vector<int> &lista) {

  if (lista.empty())
    return {};

  auto n = lista.size();

  auto dlugoscMaks = 1;
  auto indeksKoncowy = 0;
  auto dlugosc = 1;

  for (auto i = 0; i < n; i++) {

    if (lista[i] * lista[i + 1] < 0) {
      dlugosc++;

      if (dlugosc > dlugoscMaks) {
        dlugoscMaks = dlugosc;
        indeksKoncowy = i + 1;
      }
    } else
      dlugosc = 1;
  }

  auto wynik = std::vector<int>(lista.begin() + indeksKoncowy - dlugoscMaks + 1,
                                lista.begin() + indeksKoncowy + 1);

  if (wynik.size() > 1)
    return wynik;

  return {};
}

// Testy Poprawnosci
void test1() {
  std::vector<int> lista{1, -2, 6, 4, -3, 2, -4, -3};
  std::vector<int> wynik{4, -3, 2, -4};

  assert(najdluzszyNaprzemiennyPodciagV1(lista) == wynik);
}

void test2() {
  std::vector<int> lista{1, 2, 3, 4, 5};
  std::vector<int> wynik;

  assert(najdluzszyNaprzemiennyPodciagV1(lista) == wynik);
}

void test3() {
  std::vector<int> lista;
  std::vector<int> wynik;

  assert(najdluzszyNaprzemiennyPodciagV1(lista) == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}
