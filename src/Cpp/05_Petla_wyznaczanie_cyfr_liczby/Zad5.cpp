#include <iostream>

/*
Dla pobranej liczby, sprawdź czy jest ona palindromem.
To znaczy, sprawdź czy liczba nie zmienia się po zapisaniu
jej cyfr w odwrotnej kolejności.
*/

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
