/*
Tytul: Sortowanie znakow w napisie.
Tresc: Otrzymujesz napis. Posortuj alfabetycznie jego znaki.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisu "Ala ma kota" powinno zostac zwrocone " Aaaaklmot".

*/

#include <algorithm>
#include <cassert>
#include <string>

void sortuj(std::string &napis) { std::sort(napis.begin(), napis.end()); }

void test1() {
  std::string napis = "bcda";
  std::string wynik = "abcd";

  sortuj(napis);

  assert(napis == wynik);
}

int main() {

  test1();

  return 0;
}

