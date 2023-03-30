/*
Tytul: Srednia z n liczb
Tresc: Napisz funkcje, ktora dla otrzymanej liczby n, poprosi uzytkownika o podanie n liczb i zwroci ich srednia arytmetyczna.
Dane wejsciowe: liczba naturalna n oraz n liczb
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla pobranych liczb 2, 4 i 6, funkcja powinna zwrocic liczbe 4.

*/
#include <iostream>

float srednia(int n) {

  float suma = 0.0;
  int x;

  for (int i = 0; i < n; i++) {
    std::cout << "Podaj liczbe: " << std::endl;
    std::cin >> x;
    suma += x;
  }

  return suma / n;
}

int main() {

  std::cout << "Podaj liczbe n: " << std::endl;
  int n;
  std::cin >> n;

  float wynik = srednia(n);

  std::cout << "Srednia z podanych liczb to " << wynik << std::endl;

  return 0;
}

