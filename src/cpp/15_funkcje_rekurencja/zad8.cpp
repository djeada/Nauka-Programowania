/*
Tytul: Slowa elfickie.
Tresc: Otrzymujesz napis. Przy uzyciu rekurencji sprawdz czy otrzymane slowo
jest slowem elfickim. Przez slowo elfickie rozumiemy taki napis, w ktorym co
najmniej raz wystepuje kazda z liter slowa elf. Dane wejsciowe: Napis. Dane
wyjsciowe: Wartosc logiczna. Przyklad: Dla otrzymanego napisu: "reflektor",
powinna zostac zwrocona wartosc logiczna: Prawda.

*/
#include <cassert>
#include <utility>
#include <vector>

std::vector<std::pair<char, char>> hanoi(int n) {
  /**
   *
   */
  auto hanoiWew = [&](int n, char a, char b, char c,
                      std::vector<std::pair<char, char>> &wynik) {
    /**
     *
     */
    if (n == 1) {
      wynik.emplace_back(a, b);
      return;
    }

    hanoiWew(n - 1, a, c, b, wynik);
    wynik.emplace_back(a, b);
    hanoiWew(n - 1, c, b, a, wynik);
  };

  std::vector<std::pair<char, char>> wynik;
  hanoiWew(n, 'A', 'B', 'C', wynik);
  return wynik;
}

void test1() {
  int n = 3;
  std::vector<std::pair<char, char>> wynik = {
      {'A', 'B'}, {'A', 'C'}, {'B', 'C'}, {'A', 'B'},
      {'C', 'A'}, {'C', 'B'}, {'A', 'B'}};

  assert(hanoi(n) == wynik);
}

int main() {

  test1();

  return 0;
}

