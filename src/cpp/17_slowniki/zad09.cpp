/*
ZAD-09 — Znaki występujące co najmniej dwa razy

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Wypisz napis złożony z **unikalnych** znaków, które występują co
najmniej 2 razy, w kolejności pierwszego pojawienia się w wejściu.

### Wejście

* 1 linia: napis

### Wyjście

* 1 linia: wynikowy napis

### Przykład

**Wejście:**

```
aaabbbccc
```

**Wyjście:**

```
abc
```

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

  for (const auto &znak : slowo) slownik[znak]++;

  return slownik;
}

std::vector<char> znaki(const std::string &slowo) {
  /*
   * Zwraca wektor znakow, ktore wystepuja w napisie wiecej niz raz.
   */

  std::unordered_map<char, int> slownik = budujSlownik(slowo);
  std::vector<char> wynik;

  for (auto it = slownik.begin(); it != slownik.end(); it++) {
    if (it->second > 1) wynik.push_back(it->first);
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
