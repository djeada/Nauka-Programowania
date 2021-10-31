#include <iostream>

/*
Dla pobranej liczby, powinne zostac wypisane cyfry liczb, ktore sa:

a) Liczbami parzystymi.
b) Mniejsze niz 5.
c) Rozne od 0.
*/

int main() {

  std::cout << "Podaj liczbe: " << std::endl;
  int liczba;
  std::cin >> liczba;

  int liczbaPomocnicza = liczba;
  std::cout << "Cyfry liczby badace liczbami parzystymi: " << std::endl;

  while (liczbaPomocnicza > 0) {
    int cyfra = liczbaPomocnicza % 10;

    if (cyfra % 2 == 0)
      std::cout << cyfra << std::endl;

    liczbaPomocnicza /= 10;
  }

  liczbaPomocnicza = liczba;
  std::cout << "Cyfry liczby mniejsze niz 5: " << std::endl;

  while (liczbaPomocnicza > 0) {
    int cyfra = liczbaPomocnicza % 10;

    if (cyfra < 5)
      std::cout << cyfra << std::endl;

    liczbaPomocnicza /= 10;
  }

  liczbaPomocnicza = liczba;
  std::cout << "Cyfry liczby rozne od 0: " << std::endl;

  while (liczbaPomocnicza > 0) {
    int cyfra = liczbaPomocnicza % 10;

    if (cyfra != 0)
      std::cout << cyfra << std::endl;

    liczbaPomocnicza /= 10;
  }

  return 0;
}
