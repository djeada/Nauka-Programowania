/*
ZAD-07 — Różnica między dwoma listami

**Poziom:** ★☆☆
**Tagi:** `list`, `set`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz elementy, które występują **tylko
w jednej** z list (różnica symetryczna).

* Kolejność elementów w wyniku może być **dowolna**.
* Jeśli wszystkie elementy są wspólne — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista elementów niewspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście (jedna z poprawnych odpowiedzi):**

```
[9, 5, 1]
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

  std::vector<int> roznica;
  for (int a : listaA) {
    if (std::find(listaB.begin(), listaB.end(), a) == listaB.end()) {
      roznica.push_back(a);
    }
  }
  for (int b : listaB) {
    if (std::find(listaA.begin(), listaA.end(), b) == listaA.end()) {
      roznica.push_back(b);
    }
  }

  printList(roznica);
  return 0;
}
