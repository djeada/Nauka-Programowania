/*
Tytul: Sortowanie wzgledem kluczy/wartosci
Otrzymujesz slownik skladajacy sie z par napisow i liczb calkowitych. Twoim zadaniem jest wypisanie par posortowanych wzgledem napisow oraz wzgledem liczb.
Dane wejsciowe: Slownik par: napis, liczba calkowita.
Dane wyjsciowe: Lista par.
Przyklad:
Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("b", 4), ("c", 3), ("x", 5)].
Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("c", 3), ("b", 4), ("x", 5)].

*/
#include <algorithm>
#include <cassert>
#include <unordered_map>
#include <utility>
#include <vector>

bool porownujKlucze(const std::pair<std::string, int> &a,
                    const std::pair<std::string, int> &b) {
  /*
   * Funkcja porownujaca pare napisow.
   */
  return a.first < b.first;
}

std::vector<std::pair<std::string, int>>
sortujWzgledemKluczy(const std::unordered_map<std::string, int> &slownik) {
  /*
   * Funkcja sortuje slownik wzgledem kluczy.
   */

  std::vector<std::pair<std::string, int>> wynik;

  for (const auto &it : slownik)
    wynik.push_back(std::pair<std::string, int>(it.first, it.second));

  sort(wynik.begin(), wynik.end(), porownujKlucze);

  return wynik;
}

bool porownujWartosci(const std::pair<std::string, int> &a,
                      const std::pair<std::string, int> &b) {
  /*
   * Funkcja porownuje wartosci.
   */
  return a.second < b.second;
}

std::vector<std::pair<std::string, int>>
sortujWzgledemWartosci(const std::unordered_map<std::string, int> &slownik) {
  /*
   * Funkcja sortuje slownik wzgledem wartosci.
   */

  std::vector<std::pair<std::string, int>> wynik;

  for (const auto &it : slownik)
    wynik.push_back(std::pair<std::string, int>(it.first, it.second));

  sort(wynik.begin(), wynik.end(), porownujWartosci);

  return wynik;
}

void test1() {
  std::unordered_map<std::string, int> slownik{
      {"c", 3}, {"x", 5}, {"a", -2}, {"b", 4}};
  std::vector<std::pair<std::string, int>> wynik{
      {"a", -2}, {"c", 3}, {"b", 4}, {"x", 5}};

  assert(sortujWzgledemWartosci(slownik) == wynik);
}

void test2() {
  std::unordered_map<std::string, int> slownik{
      {"c", 3}, {"x", 5}, {"a", -2}, {"b", 4}};
  std::vector<std::pair<std::string, int>> wynik{
      {"a", -2}, {"b", 4}, {"c", 3}, {"x", 5}};

  assert(sortujWzgledemKluczy(slownik) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

