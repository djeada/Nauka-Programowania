#include <iostream>
#include <vector>

/*
Dla otrzymanych dwóch list wypisuj na przemian elementy pierwszej 
i drugiej listy. Jeśli listy nie są równej długości po wyczerpaniu 
elementów krótszej listy, wypisuj tylko elementy dłuższej listy.
*/

void wypisz(std::vector<int> &listaA, std::vector<int> &listaB) {

  unsigned int n =
      listaA.size() < listaB.size() ? listaA.size() : listaB.size();

  for (unsigned int i = 0; i < n; i++) {
    std::cout << listaA[i] << ", ";
    std::cout << listaB[i] << ", ";
  }

  for (unsigned int i = n; i < listaA.size(); i++)
    std::cout << listaA[i] << ", ";

  for (unsigned int i = n; i < listaB.size(); i++)
    std::cout << listaB[i] << ", ";
}

int main() {

  std::vector<int> listaA({5, 3, 7, 2});
  std::vector<int> listaB({1, -2, 3});

  wypisz(listaA, listaB);

  return 0;
}
