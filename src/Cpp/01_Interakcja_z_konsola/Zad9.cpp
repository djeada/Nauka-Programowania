#include <cmath>
#include <iomanip>
#include <iostream>

/*
Otrzymujesz roczną stopę procentową, liczbę lat na spłacenie kredytu
oraz wysokość udzielonego kredytu. Oblicz miesięczną ratę oraz
całkowity koszt kredytu.
*/

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
