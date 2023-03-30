/*
Tytul: Kalkulator kredytowy
Tresc: Pobierz roczna stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc udzielonego kredytu. Oblicz miesieczna rate oraz calkowity koszt kredytu.
Dane wejsciowe: Trzy liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Dla pobranych liczb: 3.5 (roczna stopa procentowa), 8 (liczba lat) oraz 12000 (wysokosc kredytu), powinny zostac wypisane liczby 143.5 (miesieczna rata) oraz 13776 (calkowity koszt kredytu). Waluta jest umowna.

*/
#include <cmath>
#include <iomanip>
#include <iostream>

int main() {

  std::cout
      << "Podaj: stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc 
      udzielonego kredytu " << std::endl;

      float stopa;
  int lata;
  int wysokoscKredytu;

  std::cin >> stopa;
  std::cin >> lata;
  std::cin >> wysokoscKredytu;

  float r = stopa / 12 * 0.01;
  int n = lata * 12;

  float rata = wysokoscKredytu * r * pow((1 + r), n) / (pow((1 + r), n) - 1);
  float calkKoszt = rata * n;

  std::cout << std::fixed << std::setprecision(2);
  std::cout << "rata mieieczna to " << rata << std::endl;
  std::cout << "calkowity koszt to " << calkKoszt << std::endl;

  return 0;
}

