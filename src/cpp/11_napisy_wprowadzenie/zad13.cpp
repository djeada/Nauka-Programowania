/*
Tytul: Wypisz co k-ty znak napisu poziomo i pionowo.
Tresc: Otrzymasz napis oraz liczbe k.
a) Wypisz co k-ty znak napisu poziomo, rozdzielajac znaki spacjami.
b) Wypisz co k-ty znak napisu pionowo, rozdzielajac znaki enterami.
Dane wejsciowe: Napis oraz liczba.
Dane wyjsciowe: Napis.
Przyklad:
a) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony
napis: "z h n". b) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien
zostac zwrocony napis:
z
h
n

*/
#include <cassert>
#include <cmath>
#include <string>
#include <vector>

bool czyPierwsza(int n) {

  if (!(n % 2) && n < 2)
    return false;

  for (int i = 3; i <= sqrt((double)n); i += 2) {
    if (!(n % i))
      return false;
  }

  return true;
}

std::vector<char> znaki(const std::string &napis) {

  std::vector<char> znaki;

  for (unsigned int i = 0; i < napis.size(); i++) {
    if (czyPierwsza(i))
      znaki.push_back(napis[i]);
  }

  return znaki;
}

void test1() {
  std::string napis = "Kaczka lubi wiosne.";
  std::vector<char> wynik{'c', 'z', 'a', 'l', ' ', 'i', 'e'};
  assert(znaki(napis) == wynik);
}

int main() {
  test1();
  return 0;
}

