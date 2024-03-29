/*
Tytul: Zlicz instancje klasy w programie.
Tresc: Opis zadania: Stworz klase Klasa, ktora bedzie zawierala funkcje statyczna, zwracajaca aktualna liczbe instancji tej klasy w programie. Nastepnie stworz kilka obiektow tej klasy i przetestuj dzialanie funkcji.
Dane wejsciowe: brak
Dane wyjsciowe: liczba naturalna, reprezentujaca liczbe instancji klasy w programie.

*/

#include <cassert>
#include <iostream>
#include <vector>

class Klasa {
  inline static unsigned int licznik = 0;

public:
  Klasa() { licznik++; }

  ~Klasa() { licznik--; }

  unsigned int static liczbaInstancji() { return licznik; }

  void static wyswietl() {
    std::cout << "Aktualna liczba instancji: " << licznik << std::endl;
  }
};

void test1() {
  unsigned int n = 5;
  std::vector<Klasa> lista(n);
  assert(Klasa::liczbaInstancji() == n);
}

void test2() { assert(Klasa::liczbaInstancji() == 0); }

int main() {

  test1();
  test2();

  return 0;
}

