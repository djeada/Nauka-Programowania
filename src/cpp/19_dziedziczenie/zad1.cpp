/*
Dla dowolnych dwoch klas, dla ktorych jedna jest klasa bazowa, 
a druga klasa potomna wywolaj metode klasy bazowej w metodzie 
klasy potomnej nadpisujacej ta metode.
*/

#include <iostream>

class Rodzic {
public:
  void info() { std::cout << "Jestem rodzicem" << std::endl; }
};

class DzieckoA : public Rodzic {
public:
  void info() { std::cout << "Jestem dzieckiem A" << std::endl; }
};

class DzieckoB : public Rodzic {
public:
  void info() {
    std::cout << "Jestem dzieckiem B" << std::endl;
    Rodzic::info();
  }
};

int main() {

  Rodzic rodzic;
  rodzic.info();

  DzieckoA dzieckoA;
  dzieckoA.info();

  DzieckoB dzieckoB;
  dzieckoB.info();

  return 0;
}
