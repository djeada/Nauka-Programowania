/*
ZAD-04 — Iloczyn skalarny dwóch wektorów 3D

**Poziom:** ★☆☆
**Tagi:** `list`, `wektory`, `math`

### Treść

Wczytaj dwie listy długości 3 (wektory 3D) i oblicz ich **iloczyn skalarny**:
[
A_xB_x + A_yB_y + A_zB_z
]

### Wejście

* 1 linia: wektor A (lista 3 liczb całkowitych)
* 2 linia: wektor B (lista 3 liczb całkowitych)

### Wyjście

* 1 linia: jedna liczba całkowita — iloczyn skalarny

### Przykład

**Wejście:**

```
[1, 2, 3]
[3, 1, 2]
```

**Wyjście:**

```
11
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
    if (c != '[' && c != ']' && c != ' ') cleaned += c;
  }
  std::stringstream ss(cleaned);
  std::string token;
  while (std::getline(ss, token, ',')) {
    if (!token.empty()) result.push_back(std::stoi(token));
  }
  return result;
}

int main() {
  std::string line1, line2;
  std::getline(std::cin, line1);
  std::getline(std::cin, line2);

  std::vector<int> listaA = parseList(line1);
  std::vector<int> listaB = parseList(line2);

  // Iloczyn skalarny
  int iloczyn = 0;
  for (size_t i = 0; i < listaA.size(); i++) {
    iloczyn += listaA[i] * listaB[i];
  }

  std::cout << iloczyn << std::endl;
  return 0;
}
