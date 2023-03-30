/*
Tytul: Powtarzajace sie podnapisy.
Tresc: Dostajesz napis. Znajdz wszystkie powtarzajace sie podnapisy w tym
napisie. Dane wejsciowe: Napis. Dane wyjsciowe: Lista napisow. Przyklad: Dla
napisu "pythonpython" powinna zostac zwrocona lista zawierajaca napis "python".

*/
#include <cassert>
#include <climits>
#include <string>
#include <vector>

std::string najdluzszyPrzedrostekV1(const std::vector<std::string> &slowa) {

  std::string wynik = "";
  auto n = slowa.size();
  auto j = INT_MAX;

  for (const auto &slowo : slowa) {
    auto s = slowo.length();
    if (j > s)
      j = s;
  }

  for (auto i = 0; i < j; i++) {
    auto pom = slowa[0][i];
    auto k = 1;
    while (k < n) {
      if (pom == slowa[k][i])
        k++;
      else
        return wynik;
    }
    wynik += pom;
  }
  return wynik;
}

// Testy Poprawnosci
void test1() {
  std::vector<std::string> slowa = {"abcdefgh", "abcefgh", "abcd"};
  std::string wynik = "abc";

  assert(najdluzszyPrzedrostekV1(slowa) == wynik);
}

void test2() {
  std::vector<std::string> slowa = {"flower", "flow", "flight", "flix"};
  std::string wynik = "fl";

  assert(najdluzszyPrzedrostekV1(slowa) == wynik);
}

void test3() {
  std::vector<std::string> slowa = {"student", "studio", "stress", "lol"};
  std::string wynik;

  assert(najdluzszyPrzedrostekV1(slowa) == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}

