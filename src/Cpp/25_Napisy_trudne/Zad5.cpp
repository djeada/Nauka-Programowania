#include <cassert>
#include <string>

/*
Otrzymujesz napis. Jesli znaki stojace obok siebie powtarzaja sie,
zachowaj pierwsze wystapienie znaku i usun powtorzenia.
*/

std::string usunPowtorzeniaV1(const std::string &slowo) {

  std::string wynik;
  char ostatniUsunietyZnak;
  int n = slowo.size();

  for (auto i = 0; i < n - 1; i++) {
    if (slowo[i] != slowo[i + 1]) {
      wynik += slowo[i];
      ostatniUsunietyZnak = slowo[i];
    }
  }

  if (!slowo.empty() && slowo.back() != ostatniUsunietyZnak)
    wynik += slowo.back();

  return wynik;
}

// Testy Poprawnosci
void test1() {
  std::string napis = "AAAAAAAAAABBBBBBBBA";
  std::string wynik = "ABA";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test2() {
  std::string napis = "XXXYYASFBY";
  std::string wynik = "XYASFBY";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test3() {
  std::string napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC";
  std::string wynik = "C";

  assert(usunPowtorzeniaV1(napis) == wynik);
}

void test4() {
  std::string napis = "AAABB";
  std::string wynik = "AB";

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
