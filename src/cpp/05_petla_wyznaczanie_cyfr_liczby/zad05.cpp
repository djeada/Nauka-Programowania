/*
Czy liczba jest palindromem?
Tresc: Dla otrzymanej liczby naturalnej sprawdz, czy jest ona palindromem, tj. czy nie zmienia sie po zapisaniu cyfr w odwrotnej kolejnosci.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 13231, powinna zostac wypisana informacja o tym, ze liczba jest palindromem.

*/
#include <iostream>

int main() {

  std::cout << "Podaj liczbe" << std::endl;
  int liczba;
  std::cin >> liczba;

  int odwrocona = 0;
  int liczbaPomocnicza = liczba;

  while (liczbaPomocnicza > 0) {
    int cyfra = liczbaPomocnicza % 10;
    odwrocona = (odwrocona * 10 + cyfra);
    liczbaPomocnicza /= 10;
  }

  if (odwrocona == liczba)
    std::cout << "Podana liczba jest palindromem." << std::endl;
  else
    std::cout << "Podana liczba nie jest palindromem." << std::endl;

  return 0;
}

