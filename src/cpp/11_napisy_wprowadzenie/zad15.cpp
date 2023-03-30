/*
Tytul: Zamien znaki na kody ASCII.
Tresc: Otrzymasz napis. Zmien wszystkie znaki w napisie na odpowiadajace im
numery w tablicy ASCII. Zastap otrzymany napis napisem skladajacym sie z
otrzymanych numerow, oddzielonych przecinkami. Dane wejsciowe: Napis. Dane
wyjsciowe: Napis. Przyklad: Dla otrzymanego napisu: "Robot", powinien zostac
zwrocony napis: "82, 111, 98, 111, 116".

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

void wyczysc(std::string &napis) {
  auto it = napis.begin();

  while (it != napis.end()) {
    if (ispunct(*it))
      napis.erase(it);
    else
      it++;
  }
}

std::vector<std::string> slowaV1(std::string &napis) {
  std::vector<std::string> wynik;
  unsigned int pocz = 0;
  unsigned int konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);
      if (!slowo.empty())
        wynik.push_back(slowo);
    }
    pocz = konc + 1;
  }
  if (konc != pocz) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    if (!slowo.empty())
      wynik.push_back(slowo);
  }

  return wynik;
}

void test1() {
  std::string napis = "We think in generalities, but we live in details";
  std::vector<std::string> wynik{"We", "think", "in", "generalities", "but",
                                 "we", "live",  "in", "details"};
  assert(slowaV1(napis) == wynik);
}

void test2() {
  std::string napis = "";
  std::vector<std::string> wynik;
  assert(slowaV1(napis) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

