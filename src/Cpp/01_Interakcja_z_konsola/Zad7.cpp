#include <iostream>

/*
Oblicz pola figur i objętości brył:

a) Pobierz długości podstawy i wysokości trójkąta i wypisz pole.
b) Pobierz długości boków prostokąta i wypisz pole.
c) Pobierz długości przekątnych rombu i wypisz pole.
d) Pobierz promień kuli i wypisz objętość.
e) Pobierz promień podstawy i wysokość stożka i wypisz objętość.
f) Pobierz długość, szerokość i wysokość graniastosłupa i wypisz objętość.
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
