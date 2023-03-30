/*
Tytul: Liczby spelniajace okreslone warunki.
Tresc: Dla pobranej liczby naturalnej wypisz:
a) wszystkie liczby naturalne mniejsze od pobranej, ktorych suma cyfr jest rowna 10,
b) wszystkie liczby naturalne dwucyfrowe wieksze od pobranej,
c) wszystkie liczby naturalne trzycyfrowe, ktorych suma cyfr jest rowna pobranej liczbie,
d) wszystkie liczby naturalne trzycyfrowe podzielne przez sume cyfr pobranej liczby,
e) wszystkie liczby naturalne mniejsze od pobranej, skladajace sie wylacznie z parzystych cyfr.
Dane wejsciowe: Liczba naturalna dla wszystkich podpunktow.
Dane wyjsciowe: Kilka liczb naturalnych.
Przyklady
Dla pobranej liczby: 95:
a) wszystkie liczby naturalne mniejsze od pobranej, ktorych suma cyfr jest rowna 10: brak
b) wszystkie liczby naturalne dwucyfrowe wieksze od pobranej: 96, 97, 98, 99
c) wszystkie liczby naturalne trzycyfrowe, ktorych suma cyfr jest rowna pobranej liczbie: brak
d) wszystkie liczby naturalne trzycyfrowe podzielne przez sume cyfr pobranej liczby: brak
e) wszystkie liczby naturalne mniejsze od pobranej, skladajace sie wylacznie z parzystych cyfr: 2, 4

*/
#include <iostream>

int main() {

  std::cout << "Podaj liczbe: " << std::endl;
  int liczba;
  std::cin >> liczba;

  std::cout << "mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10: "
            << std::endl;
  for (int i = 0; i < liczba; i++) {
    int liczbaPomocnicza = i;
    int suma = 0;

    while (liczbaPomocnicza > 0) {
      suma += (liczbaPomocnicza % 10);
      liczbaPomocnicza /= 10;
    }

    if (suma == 10)
      std::cout << i << std::endl;
  }

  std::cout << "dwucyfrowe mniejsze od pobranej liczby: " << std::endl;
  for (int i = 10; i < 100 && i < liczba; i++) {
    std::cout << i << std::endl;
  }

  std::cout << "trzycyfrowe ktorych suma cyfr jest rowna pobranej liczbie"
            << std::endl;
  for (int i = 100; i < 1000; i++) {
    int liczbaPomocnicza = i;
    int suma = 0;

    while (liczbaPomocnicza > 0) {
      suma += (liczbaPomocnicza % 10);
      liczbaPomocnicza /= 10;
    }

    if (suma == liczba)
      std::cout << i << std::endl;
  }

  std::cout << "trzycyfrowe podzielne przez sume cyfr pobranej liczby"
            << std::endl;

  int liczbaPomocnicza = liczba;
  int suma = 0;

  while (liczbaPomocnicza > 0) {
    suma += (liczbaPomocnicza % 10);
    liczbaPomocnicza /= 10;
  }

  for (int i = 100; i < 1000; i++) {

    if (i % suma == 0)
      std::cout << i << std::endl;
  }

  std::cout << "mniejsze od pobranej liczby, skladajace sie wylacznie z "
               "parzystych cyfr"
            << std::endl;

  for (int i = 0; i < liczba; i++) {
    int liczbaPomocnicza = i;
    bool flaga = true;
    while (liczbaPomocnicza > 0) {
      int cyfra = liczbaPomocnicza % 10;
      if (cyfra % 2 == 1) {
        flaga = false;
        break;
      }
      liczbaPomocnicza /= 10;
    }

    if (flaga)
      std::cout << i << std::endl;
  }

  return 0;
}

