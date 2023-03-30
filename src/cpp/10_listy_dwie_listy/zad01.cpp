/*
Tytul: Wypisanie elementow dwoch list na przemian.
Tresc: Dla otrzymanych dwoch list, wypisuj na przemian elementy z obu list. Jesli listy nie sa tej samej dlugosci, po wyczerpaniu elementow krotszej listy, wypisuj pozostale elementy dluzszej listy.
Dane wejsciowe: Dwie listy.
Dane wyjsciowe: Kilka liczb.
Przyklad:
Dla otrzymanych list [5, 3, 7, 2] oraz [1, -2, 3], zostana wypisane: 5, 1, 3, -2, 7, 3, 2.

*/
#include <iostream>
#include <vector>

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

