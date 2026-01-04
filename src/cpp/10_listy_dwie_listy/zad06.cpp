/*
ZAD-06 — Znalezienie elementów wspólnych dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `set`

### Treść

Wczytaj dwie listy liczb całkowitych. Wypisz listę elementów, które występują w
obu listach:

* zachowaj **kolejność występowania w pierwszej liście**,
* jeśli element z pierwszej listy występuje w drugiej liście, dodaj go do
wyniku,
* jeśli nie ma elementów wspólnych — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista elementów wspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście:**

```
[2, 4]
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

  std::vector<int> wspolne;
  for (int a : listaA) {
    if (std::find(listaB.begin(), listaB.end(), a) != listaB.end()) {
      if (std::find(wspolne.begin(), wspolne.end(), a) == wspolne.end()) {
        wspolne.push_back(a);
      }
    }
  }

  printList(wspolne);
  return 0;
}
