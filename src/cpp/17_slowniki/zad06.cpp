/*
Tytul: Histogram wystapien znakow w slowie.
Tresc: Otrzymujesz napis. Znajdz czestosc wystepowania znakow w otrzymanym napisie. Innymi slowy, zwroc histogram znakow w otrzymanym napisie.
Dane wejsciowe: Napis.
Dane wyjsciowe: Slownik par znakow i liczb naturalnych.
Przyklad:
Dla otrzymanego napisu: “klasa”, slownik powinien wygladac nastepujaco: {“k”: 1, “l”: 1, “a”: 2, “s”: 1}.

*/
#include <cassert>
#include <string>
#include <unordered_map>

std::unordered_map<char, int> budujSlownik(const std::string &slowo) {
  /*
   * Funkcja zwraca slownik zawierajacy wszystkie litery w napisie oraz czestosc
   * ich wystepowania.
   */
  std::unordered_map<char, int> slownik;

  for (const auto &znak : slowo)
    slownik[znak]++;

  return slownik;
}

void test1() {
  std::string slowo = "klasa";
  std::unordered_map<char, int> wynik{{'k', 1}, {'l', 1}, {'a', 2}, {'s', 1}};

  assert(budujSlownik(slowo) == wynik);
}

void test2() {
  std::string slowo = "robot";
  std::unordered_map<char, int> wynik{{'r', 1}, {'o', 2}, {'b', 1}, {'t', 1}};

  assert(budujSlownik(slowo) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

