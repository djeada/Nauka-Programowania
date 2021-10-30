#include <iostream>

/*
Dla pobranej liczby reprezentującej rok, sprawdź czy rok jest przestępny.
*/

int main() {

  std::cout << "Podaj rok:" << endl;

  int rok;
  std::cin >> rok;

  if (rok % 4 == 0 && rok % 100 != 0 || rok % 400 == 0)
    std::cout << "Rok jest przestępny." << endl;
  else
    std::cout << "Rok nie jest przestępny." << endl;

  return 0;
}
