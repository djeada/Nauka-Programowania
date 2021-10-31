#include <iomanip>
#include <iostream>

/*
Dla pobranej liczby, wyswietl liczbe Pi podniesiona do
potegi rownej pobranej liczbie. Wynik powinien byc
zaokraglony do dwoch miejsc po przecinku.
*/

int main() {

  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  std::cout << std::fixed << std::setprecision(2);

  int wynik = 1;
  for (unsigned int i = 0; i < n; i++)
    wynik *= 3.14;

  std::cout << wynik << std::endl;

  return 0;
}
