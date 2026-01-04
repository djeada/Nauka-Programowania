/*
ZAD-05 — Obliczenie średniej ważonej

**Poziom:** ★☆☆
**Tagi:** `list`, `float`

### Treść

Wczytaj dwie listy liczb zmiennoprzecinkowych tej samej długości:

* lista wartości,
* lista wag.

Oblicz średnią ważoną:
[
\frac{\sum (wartość_i \cdot waga_i)}{\sum waga_i}
]

### Wejście

* 1 linia: lista wartości (float)
* 2 linia: lista wag (float)

### Wyjście

* 1 linia: jedna liczba zmiennoprzecinkowa — średnia ważona **z dokładnością do
2 miejsc po przecinku**

### Przykład

**Wejście:**

```
[0.2, 0.4, 0.1, 0.2, 0.1]
[2.0, 5.0, 0.0, 2.0, 1.0]
```

**Wyjście:**

```
0.29
```

*/
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

std::vector<double> parseDoubleList(const std::string& line) {
  std::vector<double> result;
  std::string cleaned;
  for (char c : line) {
    if (c != '[' && c != ']' && c != ' ') cleaned += c;
  }
  std::stringstream ss(cleaned);
  std::string token;
  while (std::getline(ss, token, ',')) {
    if (!token.empty()) result.push_back(std::stod(token));
  }
  return result;
}

int main() {
  std::string line1, line2;
  std::getline(std::cin, line1);
  std::getline(std::cin, line2);

  std::vector<double> wagi = parseDoubleList(line1);
  std::vector<double> wartosci = parseDoubleList(line2);

  double suma = 0.0;
  double suma_wag = 0.0;
  for (size_t i = 0; i < wagi.size(); i++) {
    suma += wagi[i] * wartosci[i];
    suma_wag += wartosci[i];
  }

  double srednia = suma / suma_wag;
  std::cout << std::fixed << std::setprecision(2) << srednia << std::endl;
  return 0;
}
