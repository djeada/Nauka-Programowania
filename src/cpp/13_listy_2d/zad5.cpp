/*
Tytul: Zerowanie macierzy.
Tresc: Otrzymujesz liste list liczb naturalnych reprezentujaca macierz. Jesli
element macierzy jest rowny zero, zamien wszystkie elementy tej samej kolumny i
wiersza na zera. Dane wejsciowe: Lista list liczb naturalnych. Dane wyjsciowe:
Lista list liczb naturalnych. Przyklad: Dla otrzymanej macierzy: [[1,2,3],
[4,0,6], [7,8,9]], powinna zostac zwrocona macierz: [[1,0,3], [0,0,0], [7,0,9]].

*/
#include <cassert>
#include <utility>
#include <vector>

bool macierzKwadratowa(const std::vector<std::vector<int>> &macierz) {
  /**
   *
   */
  unsigned int n = macierz.size();

  for (unsigned int i = 0; i < n; i++) {
    if (macierz[i].size() != n)
      return false;
  }

  return true;
}

std::pair<int, int> przekatne(const std::vector<std::vector<int>> &macierz) {
  /**
   *
   */
  unsigned int n = macierz.size();
  int sumaPrzekatnej1 = 0, sumaPrzekatnej2 = 0;

  for (unsigned int i = 0; i < n; i++) {
    sumaPrzekatnej1 += macierz[i][i];
    sumaPrzekatnej2 += macierz[i][n - i - 1];
  }

  return std::make_pair(sumaPrzekatnej1, sumaPrzekatnej2);
}

std::vector<int> wiersze(const std::vector<std::vector<int>> &macierz) {
  /**
   *
   */
  std::vector<int> wynik;

  for (auto wiersz : macierz) {
    int sumaWiersz = 0;

    for (auto liczba : wiersz)
      sumaWiersz += liczba;

    wynik.push_back(sumaWiersz);
  }

  return wynik;
}

std::vector<int> kolumny(const std::vector<std::vector<int>> &macierz) {
  /**
   *
   */
  std::vector<int> wynik;

  for (unsigned int i = 0; i < macierz.size(); i++) {
    int sumaKolumna = 0;

    for (unsigned int j = 0; j < macierz.size(); j++)
      sumaKolumna += macierz[j][i];

    wynik.push_back(sumaKolumna);
  }

  return wynik;
}

bool magicznyKwadrat(const std::vector<std::vector<int>> &macierz) {
  /**
   *
   */
  if (!macierzKwadratowa(macierz))
    return false;

  int n = macierz.size();

  std::pair<int, int> sumaPrzekatnych = przekatne(macierz);

  if (sumaPrzekatnych.first != sumaPrzekatnych.second)
    return false;

  for (auto sumaWiersz : wiersze(macierz)) {
    if (sumaWiersz != sumaPrzekatnych.first)
      return false;
  }

  for (auto sumaKolumna : kolumny(macierz)) {
    if (sumaKolumna != sumaPrzekatnych.first)
      return false;
  }

  return true;
}

void test1() {
  std::vector<std::vector<int>> macierz{{2, 7, 6}, {9, 5, 1}, {4, 3, 8}};
  assert(magicznyKwadrat(macierz));
}

void test2() {
  std::vector<std::vector<int>> macierz{{1, 2}, {-2, 0}};
  assert(!magicznyKwadrat(macierz));
}

int main() {
  test1();
  test2();
  return 0;
}

