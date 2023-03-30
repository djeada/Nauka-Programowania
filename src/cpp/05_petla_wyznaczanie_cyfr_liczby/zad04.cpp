/*
Tytul: Cyfry liczby spelniajace okreslone warunki.
Tresc: Dla otrzymanej liczby naturalnej wypisz cyfry tej liczby, ktore sa:
a) liczbami parzystymi,
b) mniejsze niz 5,
c) rozne od 0.
Dane wejsciowe: Liczba naturalna dla wszystkich podpunktow.
Dane wyjsciowe: Kilka liczb.
Przyklad:
a) Dla otrzymanej liczby 932, powinna zostac wypisana liczba 2.
b) Dla otrzymanej liczby 101, powinny zostac wypisane liczby 1, 0 i 1.
c) Dla otrzymanej liczby 650, powinny zostac wypisane liczby 6 i 5.

*/
#include <iostream>

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

