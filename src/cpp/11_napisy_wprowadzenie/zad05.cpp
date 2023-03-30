/*
Tytul: Wypisz co k-ty znak napisu poziomo i pionowo.
Tresc: Otrzymasz napis oraz liczbe k.
a) Wypisz co k-ty znak napisu poziomo, rozdzielajac znaki spacjami.
b) Wypisz co k-ty znak napisu pionowo, rozdzielajac znaki enterami.
Dane wejsciowe: Napis oraz liczba.
Dane wyjsciowe: Napis.
Przyklad:
a) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony napis: "z h n".
b) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony napis:
z
h
n

*/
#include <iostream>

void wypiszPoziomo(const std::string &napis, int k) {

  for (unsigned int i = 0; i < napis.size(); i += k)
    std::cout << napis[i] << ", ";

  std::cout << std::endl;
}

void wypiszPionowo(const std::string &napis, int k) {

  for (unsigned int i = 0; i < napis.size(); i += k)
    std::cout << napis[i] << std::endl;
}

int main() {
  std::string napis = "hej dzieci jesli chcecie zobaczyc smerfow las";
  int k = 3;
  wypiszPoziomo(napis, k);
  wypiszPionowo(napis, k);

  return 0;
}

