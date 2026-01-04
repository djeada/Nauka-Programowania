/*
ZAD-08 — Połącz posortowane listy w posortowaną listę bez duplikatów

**Poziom:** ★★☆
**Tagi:** `list`, `merge`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych, każda **posortowana rosnąco**. Połącz je w
jedną listę:

* wynik ma być posortowany rosnąco,
* wynik ma zawierać **unikalne** elementy (bez duplikatów).

### Wejście

* 1 linia: lista 1 (posortowana rosnąco)
* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

**Wyjście:**

```
[2, 3, 4, 5, 7, 9]
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
  size_t i = 0, j = 0;

  while (i < listaA.size() && j < listaB.size()) {
    if (listaA[i] < listaB[j]) {
      wynik.push_back(listaA[i++]);
    } else {
      wynik.push_back(listaB[j++]);
    }
  }

  while (i < listaA.size()) {
    wynik.push_back(listaA[i++]);
  }

  while (j < listaB.size()) {
    wynik.push_back(listaB[j++]);
  }

  printList(wynik);
  return 0;
}
