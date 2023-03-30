/*
Tytul: Rok przestepny.
Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie sprawdzal,
czy dany rok jest przestepny. Podpowiedz: Rok przestepny jest podzielny przez 4,
ale nie jest podzielny przez 100, chyba ze jest podzielny przez 400. Dane
wejsciowe: Liczba naturalna. Dane wyjsciowe: Komunikat o tym, czy rok jest
przestepny, czy tez nie. Przyklad: Dla pobranej liczby 2100, program powinien
wypisac informacje, ze rok nie jest przestepny.

*/
#include <iostream>

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

