#include <iostream>

/*
Dla pobranej liczby reprezentujacej rok, sprawdz czy rok jest przestepny.
*/

int main() {

  std::cout << "Podaj rok:" << endl;

  int rok;
  std::cin >> rok;

  if (rok % 4 == 0 && rok % 100 != 0 || rok % 400 == 0)
    std::cout << "Rok jest przestepny." << endl;
  else
    std::cout << "Rok nie jest przestepny." << endl;

  return 0;
}
