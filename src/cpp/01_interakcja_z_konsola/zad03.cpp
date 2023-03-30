/*
Tytul: Rysowanie ksztaltow za pomoca znakow.
Tresc zadania: Napisz program, ktory wypisze na standardowe wyjscie ciagi znakow tworzace kwadrat, trojkat oraz romb z jedynek. Pamietaj o dodawaniu odpowiednich spacji i przejsciach do nowej linii.
Przyklady:
Kwadrat:
xx
xx
Trojkat:
1
22
333
Romb z jedynek:
1
111
11111
111
1
Dane wejsciowe: Brak.
Dane wyjsciowe: Komunikat.

*/
#include <iostream>

int main() {

  std::cout << "xx" << std::endl;
  std::cout << "xx" << std::endl << std::endl;

  std::cout << "1" << std::endl;
  std::cout << "22" << std::endl;
  std::cout << "333" << std::endl << std::endl;

  std::cout << "  1" << std::endl;
  std::cout << " 111" << std::endl;
  std::cout << "11111" << std::endl;
  std::cout << " 111" << std::endl;
  std::cout << "  1" << std::endl;

  return 0;
}

