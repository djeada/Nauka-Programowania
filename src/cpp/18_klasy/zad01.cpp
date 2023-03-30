/*
Tytul: Zaprojektuj klase Kolo.
Opis zadania: Napisz klase Kolo, ktora bedzie reprezentowala kolo. Klasa powinna zawierac nastepujace funkcje:
1. Konstruktor, ktory przyjmuje jedna liczbe jako argument, reprezentujaca promien kola. Domyslna wartoscia promienia powinno byc 1.
2. Funkcje obwod, ktora zwraca obwod kola.
3. Funkcje pole, ktora zwraca pole kola.
4. Funkcje, ktora wypisuje informacje o kole na standardowe wyjscie.
Napisz program, ktory przetestuje twoja klase. Stworz kolo o promieniu 3 i uzyj funkcji wypisujacej informacje o kole.

*/

#include <cmath>
#include <iostream>
#include <numbers>

class Kolo {

public:
  Kolo(double r) {
    if (r <= 0) {
      std::cout << "Promien nie moze byc liczba ujemna." << std::endl;
      std::cout << "Promien ustawiono na 1" << std::endl;
      promien = 1.0;
    }

    else
      promien = r;
  }

  void setPromien(double r) { promien = r; }

  double getPromien() { return promien; }

  double pole() { return std::numbers::pi * pow(promien, 2); }

  double obwod() { return 2 * std::numbers::pi * promien; }

  double srednica() { return 2 * promien; }

  friend std::ostream &operator<<(std::ostream &out, Kolo &k) {
    std::cout << "Promien = " << k.promien << std::endl;
    std::cout << "Srednica = " << k.srednica() << std::endl;
    std::cout << "Pole = " << k.pole() << std::endl;
    std::cout << "Obwod = " << k.obwod() << std::endl;

    return out;
  }

private:
  double promien;
};

int main() {

  Kolo kolo(3);
  std::cout << kolo;

  return 0;
}

