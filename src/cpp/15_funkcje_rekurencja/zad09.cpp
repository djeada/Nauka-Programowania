/*
Tytul: Slowa elfickie.
Tresc: Otrzymujesz napis. Przy uzyciu rekurencji sprawdz czy otrzymane slowo jest slowem elfickim. Przez slowo elfickie rozumiemy taki napis, w ktorym co najmniej raz wystepuje kazda z liter slowa elf.
Dane wejsciowe: Napis.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla otrzymanego napisu: "reflektor", powinna zostac zwrocona wartosc logiczna: Prawda.

*/
#include <algorithm>
#include <cassert>
#include <string>

int znajdz(std::string slowo, char znak, unsigned int pozycja = 0) {
  /**
   * Funkcja zwraca indeks pierwszego wystapienia litera w slowie.
   */
  if (pozycja >= slowo.size())
    return -1;

  if (slowo[pozycja] == znak)
    return pozycja;

  return znajdz(slowo, znak, pozycja + 1);
}

bool czySlowoElfickie(std::string slowo, std::string elf = "elf") {
  /**
   * Funkcja sprawdza czy wszystkie litery slowa elf wystepuja w napisie.
   */

  if (elf.empty())
    return true;

  if (slowo.empty())
    return false;

  auto pozycja = znajdz(slowo, elf[0]);

  if (pozycja == -1)
    return false;

  // usun znak na pozycji pozycja z napisu slowo
  slowo.erase(pozycja, 1);

  return czySlowoElfickie(slowo, elf.substr(1));
}

void test1() {
  std::string slowo = "reflektor";
  bool wynik = true;

  assert(czySlowoElfickie(slowo) == wynik);
}

void test2() {
  std::string slowo = "elzbieta";
  bool wynik = false;

  assert(czySlowoElfickie(slowo) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

