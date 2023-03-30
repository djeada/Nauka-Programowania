/*
Tytul: Polimorfizm.
Tresc: Zaprojektuj klase Zwierz oraz klasy potomne Pies i Kot. Obie klasy
potomne powinny nadpisywac metode 'odglos()' zdefiniowana w klasie bazowej.
Napisz program testujacy te klasy, w ktorym umiescisz obiekty wszystkich trzech
klas w jednej liscie i przejdziesz przez wszystkie elementy tej listy, wywolujac
dla kazdego z nich funkcje 'odglos()'."

*/

#include <cassert>
#include <iostream>
#include <vector>

class Zwierz {
public:
  virtual void odglos() const { std::cout << "Jestem zwierzem" << std::endl; }
};

class Pies : public Zwierz {
public:
  void odglos() const override { std::cout << "Hau" << std::endl; }
};

class Kot : public Zwierz {
public:
  void odglos() const override { std::cout << "Miau" << std::endl; }
};

int main() {

  std::vector<Zwierz> zwierzaki{Zwierz(), Pies(), Kot()};

  for (const auto &zwierz : zwierzaki)
    zwierz.odglos();

  return 0;
}

