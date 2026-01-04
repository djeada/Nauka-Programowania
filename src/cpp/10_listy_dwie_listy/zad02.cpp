/*
ZAD-02 — Połączenie dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `indeksy`, `concat`

### Treść

Wczytaj dwie listy liczb całkowitych i wykonaj niezależnie:

**a)** Połącz listy, doklejając drugą listę na koniec pierwszej.
**b)** W pierwszej liście **podmień** elementy o parzystych indeksach (0, 2, 4,
…) elementami z drugiej listy o tych samych indeksach — o ile taki indeks
istnieje w obu listach.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: wynik dla **a)** jako lista
* 2 linia: wynik dla **b)** jako lista

### Przykład

**Wejście:**

```
[1, 2, 3]
[4, 5, 6]
```

**Wyjście:**

```
[1, 2, 3, 4, 5, 6]
[4, 2, 6]
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

  // a) Połączenie
  std::vector<int> polacz = listaA;
  for (int x : listaB) {
    polacz.push_back(x);
  }
  printList(polacz);

  // b) Przeplot
  std::vector<int> przeplot;
  size_t n = std::min(listaA.size(), listaB.size());
  for (size_t i = 0; i < n; i++) {
    przeplot.push_back(listaB[i]);
    przeplot.push_back(listaA[i]);
  }
  printList(przeplot);

  return 0;
}
