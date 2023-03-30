/*
Tytul: Dziedziczenie wielokrotne
Tresc: Napisz klase Ptak, dziedziczaca po klasach Zwierz i ObiektLatajacy. W sklad klasy Zwierz powinny wchodzic funkcje o nazwach 'jedz()', 'spij()', 'wydaj_dzwiek()', ktore wypisuja odpowiednie komunikaty na standardowe wyjscie. W sklad klasy ObiektLatajacy powinny wchodzic funkcje o nazwach 'lec()', 'wyladuj()', ktore wypisuja odpowiednie komunikaty na standardowe wyjscie. Napisz program testujacy te klase.

*/

#include <iostream>

class Zwierz {

private:
  std::string nazwa;
  std::string pokarm;
  std::string dzwiek;

public:
  Zwierz(std::string nazwa, std::string pokarm, std::string dzwiek)
      : nazwa(nazwa), pokarm(pokarm), dzwiek(dzwiek) {}

  void jedz() {
    std::cout << nazwa << " spozywa " << pokarm << "." << std::endl;
  }

  void spij() { std::cout << nazwa << " idzie spac." << std::endl; }

  void wydajDzwiek() { std::cout << dzwiek << std::endl; }
};

class ObiektLatajacy {

private:
  std::string nazwa;

public:
  ObiektLatajacy(std::string nazwa) : nazwa(nazwa) {}

  void lec() { std::cout << nazwa << " wznosi sie w powietrze." << std::endl; }

  void laduj() { std::cout << nazwa << " laduje." << std::endl; }
};

class Ptak : public Zwierz, public ObiektLatajacy {

public:
  Ptak(std::string nazwa)
      : Zwierz(nazwa, "robaki", "Aww!Aww!"), ObiektLatajacy(nazwa) {}
};

int main() {

  Ptak koliber("Koliberek");
  koliber.jedz();
  koliber.lec();
  koliber.laduj();
  koliber.wydajDzwiek();
  koliber.spij();

  return 0;
}

