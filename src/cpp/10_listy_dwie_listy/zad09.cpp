/*
ZAD-09 — Usuń z pierwszej listy część wspólną obu list

**Poziom:** ★★☆
**Tagi:** `list`, `filter`

### Treść

Wczytaj dwie listy liczb całkowitych. Usuń z pierwszej listy wszystkie elementy,
które występują również w drugiej liście.

* Zachowaj kolejność pozostałych elementów z pierwszej listy.
* Jeśli wszystko zostanie usunięte — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista 1 po usunięciu elementów wspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście:**

```
[9, 5]
```

*/
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

std::vector<int> parseList(const std::string& line) {
  std::vector<int> result;
  std::string cleaned;
  for (char c : line) {
    if (c != '[' && c != ']' && c != ' ') cleaned += c;
  }
  std::stringstream ss(cleaned);
  std::string token;
  while (std::getline(ss, token, ',')) {
    if (!token.empty()) result.push_back(std::stoi(token));
  }
  return result;
}

void printList(const std::vector<int>& lista) {
  std::cout << "[";
  for (size_t i = 0; i < lista.size(); i++) {
    if (i > 0) std::cout << ", ";
    std::cout << lista[i];
  }
  std::cout << "]" << std::endl;
}

int main() {
  std::string line1, line2;
  std::getline(std::cin, line1);
  std::getline(std::cin, line2);

  std::vector<int> listaA = parseList(line1);
  std::vector<int> listaB = parseList(line2);

  std::vector<int> wynik;
  for (int a : listaA) {
    if (std::find(listaB.begin(), listaB.end(), a) == listaB.end()) {
      wynik.push_back(a);
    }
  }

  printList(wynik);
  return 0;
}
