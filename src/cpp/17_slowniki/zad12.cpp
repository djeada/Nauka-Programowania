/*
Tytul: Usuwanie z slownika.
Tresc: Otrzymujesz slownik par napisow i liczb calkowitych oraz pojedyncza
liczbe calkowita. Usun z slownika pary, dla ktorych wartosc jest rowna
otrzymanej liczbie. Dane wejsciowe: Slownik par napisow i liczb calkowitych oraz
liczba calkowita. Dane wyjsciowe: Slownik par napisow i liczb calkowitych.
Przyklad:
Dla slownika i liczby: {“aaa”: 5, “abc”: 1, “xxx”: 5, “cba” : 3} i 5, slownik
powinien wygladac nastepujaco: {“abc”: 1, “cba” : 3}.

*/
#include <algorithm>
#include <cassert>
#include <unordered_map>
#include <vector>

bool wektoryRowne(std::vector<int> v1, std::vector<int> v2) {
  /*
   * Funkcja porownuje wektory. Funkcja zwraca true, jesli oba wektory skladaja
   * sie z takich samych elementow.
   */
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end());
  return v1 == v2;
}

bool identyczne(std::unordered_map<std::string, std::vector<int>> &slownikA,
                std::unordered_map<std::string, std::vector<int>> &slownikB) {
  /*
   * Funkcja sprawdza czy dwa slowniki maja takie same elementy.
   */
  if (slownikA.size() != slownikB.size())
    return false;

  for (auto &[klucz, wektorA] : slownikA) {
    if (slownikB.count(klucz) == 0)
      return false;

    auto wektorB = slownikB[klucz];
    if (!wektoryRowne(wektorA, wektorB))
      return false;
  }

  return true;
}

void test1() {
  std::unordered_map<std::string, std::vector<int>> slownikA{
      {"c", {3, 2, 1}}, {"x", {-2, 9, 11}}, {"a", {4, 6, 7}}};

  std::unordered_map<std::string, std::vector<int>> slownikB{
      {"a", {7, 4, 6}}, {"c", {2, 3, 1}}, {"x", {-2, 11, 9}}};

  assert(identyczne(slownikA, slownikB));
}

void test2() {
  std::unordered_map<std::string, std::vector<int>> slownikA{
      {"abc", {1, 2, 3}}, {"123", {9, 0, 0}}, {"xxx", {5, 5, 5}}};
  std::unordered_map<std::string, std::vector<int>> slownikB{
      {"abc", {1, 2, 3}}, {"xxx", {0, 0, 9}}, {"123", {5, 5, 5}}};

  assert(!identyczne(slownikA, slownikB));
}

int main() {

  test1();
  test2();

  return 0;
}

