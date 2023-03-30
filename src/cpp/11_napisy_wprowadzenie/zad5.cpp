/*
Tytul: Napis skladajacy sie z liczb od 1 do n.
Tresc: Otrzymasz liczbe naturalna n. Zwroc napis skladajacy sie z liczb
naturalnych od 1 do n. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej liczby n rownej 3 powinien zostac zwrocony napis: "123".

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

