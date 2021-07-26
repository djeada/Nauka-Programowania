#include "wektor.h"

int main() {

  Wektor wektorA(5, 5, 5);
  Wektor wektorB(-3, -3, -3);

  auto suma = wektorA + wektorB;
  auto roznica = wektorA - wektorB;
  auto iloczynWek = wektorA * wektorB;

  std::cout << "Dla wektorow A \n"
            << wektorA << "oraz B \n"
            << wektorB << "otrzymujemy sume: \n"
            << suma << "roznice: \n"
            << roznica << "iloczyn wektorowy: \n"
            << iloczynWek << std::endl;

  return 0;
}
