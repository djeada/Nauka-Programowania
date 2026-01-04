/*
ZAD-01 — Wypisanie elementów dwóch list na przemian

**Poziom:** ★☆☆
**Tagi:** `list`, `iteracja`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz ich elementy **na przemian**:
pierwszy z listy 1, pierwszy z listy 2, drugi z listy 1, drugi z listy 2, itd.

Jeśli listy mają różne długości, po wyczerpaniu krótszej listy dopisz pozostałe
elementy dłuższej listy w tej samej kolejności.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: elementy obu list wypisane na przemian, oddzielone przecinkami **bez
spacji**

### Przykład

**Wejście:**

```
[5, 3, 7, 2]
[1, -2, 3]
```

**Wyjście:**

```
5,1,3,-2,7,3,2
```

*/
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

std::vector<int> parseList(const std::string& line) {
  std::vector<int> result;
  std::string cleaned;
  for (char c : line) {
    if (c != '[' && c != ']' && c != ' ') {
      cleaned += c;
    }
  }
  std::stringstream ss(cleaned);
  std::string token;
  while (std::getline(ss, token, ',')) {
    if (!token.empty()) {
      result.push_back(std::stoi(token));
    }
  }
  return result;
}

int main() {
  std::string line1, line2;
  std::getline(std::cin, line1);
  std::getline(std::cin, line2);

  std::vector<int> listaA = parseList(line1);
  std::vector<int> listaB = parseList(line2);

  size_t n = std::min(listaA.size(), listaB.size());
  bool first = true;

  for (size_t i = 0; i < n; i++) {
    if (!first) std::cout << ",";
    std::cout << listaA[i];
    first = false;
    if (!first) std::cout << ",";
    std::cout << listaB[i];
  }

  for (size_t i = n; i < listaA.size(); i++) {
    if (!first) std::cout << ",";
    std::cout << listaA[i];
    first = false;
  }

  for (size_t i = n; i < listaB.size(); i++) {
    if (!first) std::cout << ",";
    std::cout << listaB[i];
    first = false;
  }

  std::cout << std::endl;

  return 0;
}
