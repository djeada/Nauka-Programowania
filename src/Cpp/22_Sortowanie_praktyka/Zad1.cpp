/*
Dla otrzymanego napisu, posortuj alfabetycznie jego znaki.
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
