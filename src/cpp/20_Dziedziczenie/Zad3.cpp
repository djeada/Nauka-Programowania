/*
Zaprojektuj klase Zwierz oraz klasy pochodne Pies oraz Kot. 
Obie klasy potomne powinny nadpisywac metode odglos() klasy 
zdefiniowana w klasie bazowej. Nastepnie w programie 
testujacym napisane klasy, nalezy w jednej liscie zebrac 
obiekty wszystkich trzech klas. Nalezy przy pomocy petli 
przejsc przez wszystkie elementy listy i dla kazdego z nich 
wywolac funkcje odglos().
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
