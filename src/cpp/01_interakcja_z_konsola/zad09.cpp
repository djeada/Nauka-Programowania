/*
ZAD-09 — Kalkulator kredytowy (rata annuitetowa)

**Poziom:** ★★☆
**Tagi:** `finanse`, `float`, `formatowanie`

### Treść

Wczytaj:

* roczną stopę procentową `R` (w %),
* okres spłaty `Y` (w latach),
* kwotę kredytu `P`.

Oblicz miesięczną ratę `M` oraz całkowity koszt `C = M * n`, gdzie `n = 12 * Y`.

Dla `R > 0` użyj wzoru:
[
M = P \cdot \frac{r(1+r)^n}{(1+r)^n-1}
]
gdzie `r = R / (12*100)`.

Dla `R = 0` przyjmij:

* `M = P / n`.

### Wejście

3 liczby (w osobnych liniach):

1. `R` (float, `R ≥ 0`)
2. `Y` (int, `Y > 0`)
3. `P` (float, `P > 0`)

### Wyjście

Dwie linie (do **2 miejsc po przecinku**):

1. miesięczna rata `M`
2. całkowity koszt `C`

### Przykład

**Wejście:**

```
3.5
8
12000
```

**Wyjście:**

```
143.50
13776.00
```

*/
#include <cmath>
#include <iomanip>
#include <iostream>

int main() {
  std::cout
      << "Podaj: stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc 
      udzielonego kredytu " << std::endl;

      float stopa;
  int lata;
  int wysokoscKredytu;

  std::cin >> stopa;
  std::cin >> lata;
  std::cin >> wysokoscKredytu;

  float r = stopa / 12 * 0.01;
  int n = lata * 12;

  float rata = wysokoscKredytu * r * pow((1 + r), n) / (pow((1 + r), n) - 1);
  float calkKoszt = rata * n;

  std::cout << std::fixed << std::setprecision(2);
  std::cout << "rata mieieczna to " << rata << std::endl;
  std::cout << "calkowity koszt to " << calkKoszt << std::endl;

  return 0;
}
