#include "macierz.h"

int main() {

  Macierz macierzA(std::vector<std::vector<int>>{{1, -2, 3}});
  Macierz macierzB(std::vector<std::vector<int>>{{8, 9, -5}});

  auto suma = macierzA + macierzB;
  auto roznica = macierzA - macierzB;

  std::cout << "Macierz A \n"
            << macierzA << "Macierz B \n"
            << macierzB << std::endl
            << "suma: \n"
            << suma << std::endl
            << "roznica: \n"
            << roznica << std::endl;

  macierzA = Macierz(std::vector<std::vector<int>>{{1, 2, 3}});
  macierzB = Macierz(std::vector<std::vector<int>>{{4}, {5}, {6}});

  auto iloczynAB = macierzA * macierzB;
  auto iloczynBA = macierzB * macierzA;

  std::cout << "Macierz A \n"
            << macierzA << "Macierz B \n"
            << macierzB << std::endl
            << "iloczyn A*B: \n"
            << iloczynAB << std::endl
            << "iloczyn B*A: \n"
            << iloczynBA << std::endl;

  return 0;
}
