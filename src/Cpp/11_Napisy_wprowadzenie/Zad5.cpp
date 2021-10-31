#include <iostream>

/*
Otrzymujesz napis oraz liczbę k. 
a) Wypisz poziomo co k-ty znak. Znaki powinny być oddzielone spacjami.
b) Wypisz pionowo co k-ty znak. Znaki powinny być oddzielone enterami.
*/

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
