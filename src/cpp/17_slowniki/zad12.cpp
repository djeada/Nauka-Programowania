/*
ZAD-12 — Porównanie dwóch słowników z listami (kolejność list bez znaczenia)

**Poziom:** ★★☆
**Tagi:** `dict`, `porównanie`, `list`

### Treść

Wczytaj dwa „słowniki” (opis w wejściu). Dla każdego klucza wartościami są listy
liczb całkowitych, ale **kolejność w listach nie ma znaczenia**. Wypisz `Prawda`
jeśli słowniki są identyczne (te same klucze i te same wielozbiory wartości), w
przeciwnym razie `Fałsz`.

### Wejście

* Najpierw:

  * 1 linia: `n`
  * następnie `n` linii: `klucz v1 v2 v3 ...` (co najmniej jedna wartość)
* Potem:

  * 1 linia: `m`
  * następnie `m` linii: `klucz v1 v2 v3 ...`

### Wyjście

* `Prawda` lub `Fałsz`

### Przykład

**Wejście:**

```
2
a 1 2 3
b 4 5
2
a 3 2 1
b 5 4
```

**Wyjście:**

```
Prawda
```

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
  if (slownikA.size() != slownikB.size()) return false;

  for (auto &[klucz, wektorA] : slownikA) {
    if (slownikB.count(klucz) == 0) return false;

    auto wektorB = slownikB[klucz];
    if (!wektoryRowne(wektorA, wektorB)) return false;
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
