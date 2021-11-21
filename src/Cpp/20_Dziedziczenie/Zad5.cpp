/*
Napisz klase Ptak, dziedziczaca po klasach Zwierz oraz ObiektLatajacy. 
a) W sklad klasy Zwierz powinny wchodzic funkcje wypisujace na standardowe 
wyjscie komunikaty odpowiadajace ich nazwom. Funkcje powinny miec 
nastepujace nazwy: jedz(), spij(), wydaj_dzwiek(). 
b) W sklad klasy ObiektLatajacy powinny wchodzic funkcje wypisujace na 
standardowe wyjscie komunikaty odpowiadajace ich nazwom. Funkcje powinny 
miec nastepujace nazwy: lec(), wyladuj().
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
