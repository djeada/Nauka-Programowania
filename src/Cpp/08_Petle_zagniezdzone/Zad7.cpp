#include <iostream>

/*
Napisz funkcję, która dla otrzymanej liczby N, wypisze N trójkątów. 
Trójkąty powinny być ustawione w kolumnie, jeden na drugim. Wysokość 
pierwszego trójkąta to 1, a każdego następnego równa jest wysokości 
poprzedniego powiększonej o 1.
*/

void trojkat(int wysokosc) {

  for (int y = 0; y < wysokosc; y++) {
    for (int x = 0; x <= y; x++)
      std::cout << "*";
    std::cout << std::endl;
  }
}

void choinka(int wysokosc) {

  for (int i = 1; i <= wysokosc; i++)
    trojkat(i);
}

int main() {

  std::cout << "Podaj wysokosc choinki: ";
  int wysokosc;
  std::cin >> wysokosc;

  choinka(wysokosc);

  return 0;
}
