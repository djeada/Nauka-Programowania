/*
Tytul: Ile dni minelo od poczatku roku?
Tresc: Dla trzech pobranych liczb: reprezentujacych date wypisz, ile dni minelo od poczatku roku. Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad: Dla pobranych liczb: 14, 2 oraz 1482, powinna zostac zwrocona liczba 45. **

*/
#include <iostream>

int main() {

  int dzien, miesiac, rok;
  std::cin >> dzien >> miesiac >> rok;

  int liczba_dni = 0;
  switch (miesiac) {
  case 1:
    liczba_dni = dzien;
    break;
  case 2:
    liczba_dni = 31 + dzien;
    break;
  case 3:
    liczba_dni = 59 + dzien;
    break;
  case 4:
    liczba_dni = 90 + dzien;
    break;
  case 5:
    liczba_dni = 120 + dzien;
    break;
  case 6:
    liczba_dni = 151 + dzien;
    break;
  case 7:
    liczba_dni = 181 + dzien;
    break;
  case 8:
    liczba_dni = 212 + dzien;
    break;
  case 9:
    liczba_dni = 243 + dzien;
    break;
  case 10:
    liczba_dni = 273 + dzien;
    break;
  case 11:
    liczba_dni = 304 + dzien;
    break;
  case 12:
    liczba_dni = 334 + dzien;
    break;
  }

  if (rok % 4 == 0 && rok % 100 != 0 || rok % 400 == 0) {
    if (miesiac > 2) {
      liczba_dni += 1;
    }
  }

  std::cout << "Od poczatku roku uplynelo: " << liczba_dni << std::endl;

  return 0;
}

