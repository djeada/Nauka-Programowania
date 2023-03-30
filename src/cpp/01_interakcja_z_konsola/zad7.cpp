/*
Tytul: Pole powierzchni i objetosc figur geometrycznych.
Tresc zadania: Napisz program, ktory bedzie obliczal pola powierzchni i
objetosci figur geometrycznych zgodnie z nastepujacymi instrukcjami: a) Pobierz
dlugosci podstawy i wysokosci trojkata i wypisz jego pole. b) Pobierz dlugosci
bokow prostokata i wypisz jego pole. c) Pobierz dlugosci przekatnych rombu i
wypisz jego pole. d) Pobierz promien kuli i wypisz jej objetosc. e) Pobierz
promien podstawy i wysokosc stozka i wypisz jego objetosc. f) Pobierz dlugosc,
szerokosc i wysokosc graniastoslupa i wypisz jego objetosc. Jednostki sa
dowolne. Dane wejsciowe:
* Dwie liczby naturalne dla podpunktow a, b i c.
* Liczba naturalna dla podpunktu d.
* Dwie liczby naturalne dla podpunktu e.
* Trzy liczby naturalne dla podpunktu f.
Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.
Przyklad:
a) Dla pobranych liczb: 5 i 2, powinna zostac wypisana liczba: 5.
b) Dla pobranych liczb: 3 i 3, powinna zostac wypisana liczba: 4.
c) Dla pobranych liczb: 2 i 4, powinna zostac wypisana liczba: 1.
d) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 33.493.
e) Dla pobranych liczb: 3 i 2, powinna zostac wypisana liczba: 18.84.
f) Dla pobranych liczb: 2, 2 i 2, powinny zostac wypisana liczba: 8.

*/
#include <iostream>

int main() {

  std::cout << "podaj podstawe i wysokosc trojkata:" << std::endl;

  float a;
  float b;

  std::cin >> a;
  std::cin >> b;

  std::cout << "pole trojkata o podstawie " << a << " i wysokosci " << b
            << " jest rowne " << a * b / 2 << std::endl;

  std::cout << "podaj dlugosci bokow prostokata:" << std::endl;

  std::cin >> a;
  std::cin >> b;

  std::cout << "pole prostokata o bokach " << a << " i " << b << " jest rowne "
            << a * b << std::endl;

  std::cout << "podaj dlugosci przekatnych rombu:" << std::endl;
  std::cin >> a;
  std::cin >> b;
  std::cout << "pole rombu o przekotnych " << a << " i " << b << " jest rowne "
            << a * b / 2 << std::endl;

  std::cout << "podaj promien kuli:" << std::endl;
  std::cin >> a;
  std::cout << "objetosc kuli o promieniu " << a << " jest rowna "
            << 4 / 3 * 3.14 * a * a * a << std::endl;

  std::cout << "podaj promien podstawy i wysokosc stozka:" << std::endl;
  std::cin >> a;
  std::cin >> b;
  std::cout << "objetosc stozka o promieniu podstawy " << a << " i wysokosci "
            << b << " jest rowna " << 1 / 3 * 3.14 * a * a * b << std::endl;

  std::cout << "podaj dlugosc, szerokosc i wysokosc graniastoslupa:"
            << std::endl;
  std::cin >> a;
  std::cin >> b;
  float c;
  std::cin >> c;
  std::cout << "objetosc graniastoslupa o dlugosci " << a << " szerokosci " << b
            << " i wysokosci " << c << " jest rowna " << a * b * c << std::endl;

  return 0;
}

