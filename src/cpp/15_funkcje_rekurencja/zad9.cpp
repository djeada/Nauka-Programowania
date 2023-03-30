/*
Tytul: Gra.
Tresc: W grze, w kazdym ruchu gracz moze zdobyc 3, 5 lub 10 punktow. Oblicz przy
uzyciu rekurencji, ile sposobow istnieje, aby gracz wygral gre, gdy ma do
dyspozycji N punktow. Dane wejsciowe: Liczba naturalna N. Dane wyjsciowe: Liczba
naturalna. Przyklad: Dla N = 20, powinna zostac zwrocona liczba: 4.

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

