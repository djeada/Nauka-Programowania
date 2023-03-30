/*
Tytul: Jaki mamy dzien tygodnia?
Tresc: Napisz program, ktory dla trzech pobranych liczb naturalnych
(reprezentujacych date) bedzie wypisywal odpowiadajacy im dzien tygodnia.
Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem. Podpowiedz: Mozna
uzyc wzoru Gaussa: Niech data bedzie dana w formacie DD/MM/CCYY :
* DD - dzien
* MM - miesiac
* CC - stulecie
* YY - rok
$$A = CC/4 - 2CC - 1$$
$$B = 5YY/4$$
$$C = 26*(MM + 1)/10$$
$$Dzien = (A + B + C + DD) mod 7$$
Dane wejsciowe: Trzy liczby naturalne.
Dane wyjsciowe: Komunikat o dniu tygodnia.
Przyklad:
Dla pobranych liczb 9, 10 i 2020, program powinien zwrocic napis "Czwartek".

*/
#include <iostream>

int main() {

  std::cout << "Podaj dzien:" << std::endl;
  int DD;
  std::cin >> DD;

  std::cout << "Podaj miesiac:" << std::endl;
  int MM;
  std::cin >> MM;

  std::cout << "Podaj rok:" << std::endl;
  int rok;
  std::cin >> rok;

  int CC = rok / 100;
  int YY = rok % 100;

  int A = (CC / 4) - 2 * CC - 1;
  int B = 5 * YY / 4;
  int C = 26 * (MM + 1) / 10;

  int wynik = (A + B + C + DD) % 7;

  switch (wynik) {
  case 1:
    std::cout << "Pierwszym dniem tygodnia jest poniedzialek." << std::endl;
    break;

  case 2:
    std::cout << "Drugim dniem tygodnia jest wtorek." << std::endl;
    break;

  case 3:
    std::cout << "Trzecim dniem tygodnia jest sroda." << std::endl;
    break;

  case 4:
    std::cout << "Czwartym dniem tygodnia jest czwartek." << std::endl;
    break;

  case 5:
    std::cout << "Piatym dniem tygodnia jest piatek." << std::endl;
    break;

  case 6:
    std::cout << "Szostym dniem tygodnia jest sobota." << std::endl;
    break;

  case 7:
    std::cout << "Siodmym dniem tygodnia jest niedziela." << std::endl;
    break;

  default:
    std::cout << "Podano bledne dane." << std::endl;
  }

  return 0;
}

