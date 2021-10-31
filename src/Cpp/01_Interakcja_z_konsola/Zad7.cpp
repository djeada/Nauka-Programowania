#include <iostream>

/*
Oblicz pola figur i objetosci bryl:

a) Pobierz dlugosci podstawy i wysokosci trojkata i wypisz pole.
b) Pobierz dlugosci bokow prostokata i wypisz pole.
c) Pobierz dlugosci przekatnych rombu i wypisz pole.
d) Pobierz promien kuli i wypisz objetosc.
e) Pobierz promien podstawy i wysokosc stozka i wypisz objetosc.
f) Pobierz dlugosc, szerokosc i wysokosc graniastoslupa i wypisz objetosc.
*/

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
