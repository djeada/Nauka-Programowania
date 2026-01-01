/*
ZAD-04 — Usuń pary ze słownika na podstawie wartości

**Poziom:** ★☆☆
**Tagi:** `dict`, `filtrowanie`

### Treść

Wczytaj słownik (`n` par: klucz-napis, wartość-liczba) oraz liczbę `k`. Usuń
wszystkie pary, gdzie wartość == `k`. Wypisz wynikowy słownik.

### Wejście

* 1 linia: `n`
* następnie `n` linii: `klucz wartość`
* ostatnia linia: `k`

### Wyjście

* Słownik po usunięciu par

### Przykład

**Wejście:**

```
4
aaa 5
abc 1
xxx 5
cba 3
5
```

**Wyjście:**

```
{'abc': 1, 'cba': 3}
```

*/
#include <cassert>
#include <string>
#include <unordered_map>

void usun(std::unordered_map<std::string, int> &slownik, int liczba) {
  /*
   * Funkcja usuwa ze slownika pary, dla ktorych wartosc rowna jest
   * otrzymanej liczbie.
   */
  auto it = slownik.begin();

  while (it != slownik.end()) {
    if (it->second == liczba)
      it = slownik.erase(it);

    else
      it++;
  }
}

void test1() {
  std::unordered_map<std::string, int> slownik{
      {"aaa", 5}, {"abc", 1}, {"xxx", 5}, {"cba", 3}};
  int liczba = 5;

  std::unordered_map<std::string, int> wynik{{"abc", 1}, {"cba", 3}};

  usun(slownik, liczba);

  assert(slownik == wynik);
}

void test2() {
  std::unordered_map<std::string, int> slownik{
      {"slownik", 3}, {"word", 3}, {"lll", 3}, {"mmn", 1}};
  int liczba = 3;

  std::unordered_map<std::string, int> wynik{{"mmn", 1}};

  usun(slownik, liczba);

  assert(slownik == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
