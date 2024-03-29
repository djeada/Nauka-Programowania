/*
Tytul: Sortowanie listy par wzgledem jednej z kategorii.
Tresc: Masz dana liste par napisow i liczb. Posortuj pary w liscie wzgledem:
a) Liczb.
b) Dlugosci napisow.
Dane wejsciowe: Lista par napisow i liczb.
Dane wyjsciowe: Lista par napisow i liczb.
Przyklad:
Dla listy [(“ab”, 3), (“bca”, 1), (“c”, 2)] powinno zostac zwrocone:
a) [(“bca”, 1), (“c”, 2), (“ab”, 3)] lub
b) [(“c”, 2), (“ab”, 3), (“bca”, 1)].

*/

#include <algorithm>
#include <cassert>
#include <string>
#include <utility>
#include <vector>

void sortujWartosci(std::vector<std::pair<std::string, int>> &lista) {
  std::sort(lista.begin(), lista.end(),
            [](auto rhs, auto lhs) { return rhs.second < lhs.second; });
}

void sortujDlugosci(std::vector<std::pair<std::string, int>> &lista) {
  std::sort(lista.begin(), lista.end(), [](auto rhs, auto lhs) {
    return rhs.first.size() < lhs.first.size();
  });
}

void test1() {
  std::vector<std::pair<std::string, int>> lista{
      {"abc", 3}, {"bca", 1}, {"cab", 2}};
  std::vector<std::pair<std::string, int>> wynik{
      {"bca", 1}, {"cab", 2}, {"abc", 3}};

  sortujWartosci(lista);

  assert(lista == wynik);
}

void test2() {
  std::vector<std::pair<std::string, int>> lista{
      {"ab", 3}, {"abc", 1}, {"a", 2}};
  std::vector<std::pair<std::string, int>> wynik{
      {"a", 2}, {"ab", 3}, {"abc", 1}};

  sortujDlugosci(lista);

  assert(lista == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

