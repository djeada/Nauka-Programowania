/*
Tytul: Usun powtorzenia znakow.
Tresc: Otrzymujesz napis. Twoim zadaniem jest usuniecie powtorzen kazdego znaku
w napisie. Kazdy znak moze wystapic tylko raz. Dane wejsciowe: Napis. Dane
wyjsciowe: Napis. Przyklad: Dla napisu: “AAAAAAAAAABBBBBBBBA”, zwrocony napis
powinien brzmiec: “AB”.

*/
#include <cassert>
#include <string>
#include <unordered_map>

std::string usunPowtorzeniaV1(const std::string &slowo) {

  std::unordered_map<char, int> histogram;
  std::string wynik;

  for (auto &znak : slowo) {

    if (!histogram.count(znak)) {
      histogram[znak] = 1;
      wynik += znak;
    }
  }

  return wynik;
}

// Testy Poprawnosci
void test1() {
  std::string napis = "AAAAAAAAAABBBBBBBBA";
  std::string wynik = "AB";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test2() {
  std::string napis = "XXXYYASFBY";
  std::string wynik = "XYASFB";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test3() {
  std::string napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC";
  std::string wynik = "C";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test4() {
  std::string napis = "XAZYBP";
  std::string wynik = "XAZYBP";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test5() {
  std::string napis;
  std::string wynik;

  assert(usunPowtorzeniaV1(napis) == wynik);
}

int main() {

  test1();
  test2();
  test3();
  test4();
  test5();

  return 0;
}

// Compiled with g++ -std=c++17 Zad1.cpp -lstdc++fs -o exe

