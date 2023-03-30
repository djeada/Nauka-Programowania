/*
Tytul: Czy slowniki sa identyczne?
Otrzymujesz dwa slowniki skladajace sie z par napisow i list liczb calkowitych.
Listy sa nieuporzadkowane. Twoim zadaniem jest sprawdzenie, czy slowniki
skladaja sie z tych samych par. Dwie listy uznajemy za identyczne, jesli
zawieraja te same elementy, niezaleznie od kolejnosci, w jakiej sie one
znajduja. Dane wejsciowe: Dwa slowniki par: napis, lista liczb calkowitych. Dane
wyjsciowe: Wartosc boolowska. Przyklad: Dla otrzymanych slownikow:
{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4]}
Powinna zostac zwrocona wartosc logiczna: Prawda.
Dla otrzymanych slownikow:
{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4], 'c': [6, 7]}
Powinna zostac zwrocona wartosc logiczna: Falsz.

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <unordered_map>
#include <vector>

std::unordered_map<char, int> budujSlownik(const std::string &slowo) {
  /*
   * Tworzy slownik, ktory bedzie przechowywal wszystkie znaki z napisu oraz
   * czestotliwosci ich wystepowania.
   */
  std::unordered_map<char, int> slownik;

  for (const auto &znak : slowo)
    slownik[znak]++;

  return slownik;
}

std::vector<char> znaki(const std::string &slowo) {
  /*
   * Zwraca wektor znakow, ktore wystepuja w napisie wiecej niz raz.
   */

  std::unordered_map<char, int> slownik = budujSlownik(slowo);
  std::vector<char> wynik;

  for (auto it = slownik.begin(); it != slownik.end(); it++) {
    if (it->second > 1)
      wynik.push_back(it->first);
  }

  return wynik;
}

bool wektoryRowne(std::vector<char> v1, std::vector<char> v2) {
  /*
   * Funkcja porownuje wektory. Funkcja zwraca true, jesli oba wektory skladaja
   * sie z takich samych elementow.
   */
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end());
  return v1 == v2;
}

void test1() {
  std::string slowo = "podwodny";
  std::vector<char> wynik{'o', 'd'};

  assert(wektoryRowne(znaki(slowo), wynik));
}

void test2() {
  std::string slowo = "jedzie pociag z daleka";
  std::vector<char> wynik{'e', 'a', 'i', 'd', 'z', ' '};

  assert(wektoryRowne(znaki(slowo), wynik));
}

int main() {

  test1();
  test2();

  return 0;
}

