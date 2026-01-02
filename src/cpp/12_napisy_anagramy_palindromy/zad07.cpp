/*
Tytul: Minimalna ilosc usunietych znakow, aby uzyskac anagramy.
Tresc: Napisz program, ktory dla dwoch slow zwroci minimalna ilosc znakow, ktore
trzeba usunac, aby uzyskac anagramy. Jesli slowa sa roznej dlugosci, zwroc -1.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanych napisow: “grazyna” oraz “razynax”, powinna zostac zwrocona
liczba: 2.

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <unordered_map>
#include <vector>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
int liczbaZnakow(const std::string &slowoA, const std::string &slowoB) {
  if (slowoA.length() != slowoB.length()) return -1;
  
  std::vector<int> pom(256, 0);

  for (auto znak : slowoA) pom[znak - 'a']++;

  for (auto znak : slowoB) pom[znak - 'a']--;

  long wynik = 0;

  for (auto liczba : pom) wynik += abs(liczba);

  return wynik;
}

void test1() {
  std::string slowoA = "grazyna";
  std::string slowoB = "razynax";
  int wynik = 2;
  assert(liczbaZnakow(slowoA, slowoB) == wynik);
}

void test2() {
  std::string slowoA = "pan cytryna";
  std::string slowoB = "pan pomarancza";
  int wynik = -1;
  assert(liczbaZnakow(slowoA, slowoB) == wynik);
}

void test3() {
  std::string slowoA = "20ejdy0978oa";
  std::string slowoB = "akv81w39j1ob";
  int wynik = 14;
  assert(liczbaZnakow(slowoA, slowoB) == wynik);
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
