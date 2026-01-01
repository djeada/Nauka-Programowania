/*
ZAD-05 — Klasa Macierz

**Poziom:** ★★☆
**Tagi:** `class`, `macierze`, `operacje`

### Treść

Zaprojektuj klasę **Macierz**:

1. Konstruktor przyjmuje listę list (domyślnie pusta).
2. Operacje: dodawanie, odejmowanie, mnożenie.
3. Metoda wypisująca macierz (wierszami).
4. Porównania `==` i `!=`.

(Operację odwracania możesz pominąć w tym zadaniu, jeśli nie jest wymagana w
sprawdzarce; najczęściej w podstawowych zadaniach nie ma testów na odwracanie.)

Program tworzy:

* A = [[1, 3], [4, 2]]
* B = [[5, 0], [1, 3]]

Wypisuje A, B, a potem A+B, A-B, A*B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Macierz A:
[1, 3]
[4, 2]

Macierz B:
[5, 0]
[1, 3]

Suma macierzy:
[6, 3]
[5, 5]

Różnica macierzy A - B:
[-4, 3]
[3, -1]

Iloczyn macierzy A * B:
[8, 9]
[22, 12]
```

*/

#include <iostream>
#include <vector>

class Macierz {
 public:
  Macierz(const std::vector<std::vector<int>> _macierz) : macierz(_macierz) {}

  void setElement(unsigned int wiersz, unsigned int kolumna, int wartosc) {
    if (wiersz >= wiersze() || kolumna >= kolumny())
      throw std::invalid_argument("Nieprawidlowy indeks.");

    macierz[wiersz][kolumna] = wartosc;
  }

  int element(unsigned int wiersz, unsigned int kolumna) const {
    if (wiersz >= wiersze() || kolumna >= kolumny())
      throw std::invalid_argument("Nieprawidlowy indeks.");

    return macierz[wiersz][kolumna];
  }

  unsigned int wiersze() const { return macierz.size(); }

  unsigned int kolumny() const {
    if (wiersze() >= 1)
      return macierz.front().size();
    else
      return 0;
  }

  Macierz operator+(const Macierz &innaMacierz) {
    if (wiersze() != innaMacierz.wiersze() ||
        kolumny() != innaMacierz.kolumny())
      throw std::invalid_argument("Wymiary macierzy musza byc jednakowe.");

    Macierz pom(
        std::vector<std::vector<int>>(wiersze(), std::vector<int>(kolumny())));

    for (unsigned int i = 0; i < pom.wiersze(); i++)
      for (unsigned int j = 0; j < pom.kolumny(); j++)
        pom.setElement(i, j, element(i, j) + innaMacierz.element(i, j));

    return pom;
  }
  Macierz operator-(const Macierz &innaMacierz) {
    if (wiersze() != innaMacierz.wiersze() ||
        kolumny() != innaMacierz.kolumny())
      throw std::invalid_argument("Wymiary macierzy musza byc jednakowe.");

    Macierz pom(
        std::vector<std::vector<int>>(wiersze(), std::vector<int>(kolumny())));

    for (unsigned int i = 0; i < pom.wiersze(); i++)
      for (unsigned int j = 0; j < pom.kolumny(); j++)
        pom.setElement(i, j, element(i, j) - innaMacierz.element(i, j));

    return pom;
  }

  Macierz operator*(const Macierz &innaMacierz) {
    if (kolumny() != innaMacierz.wiersze())
      throw std::invalid_argument(
          "Liczba kolumn mnoznej musi sie rownac liczbie wierszy mnoznika.");

    const unsigned int n = wiersze();
    const unsigned int m = kolumny();
    const unsigned int p = innaMacierz.kolumny();

    Macierz pom(std::vector<std::vector<int>>(n, std::vector<int>(p)));

    for (unsigned int j = 0; j < p; j++) {
      for (unsigned int k = 0; k < m; k++) {
        for (unsigned int i = 0; i < n; i++)
          pom.setElement(
              i, j,
              pom.element(i, j) + element(i, k) * innaMacierz.element(k, j));
      }
    }

    return pom;
  }

  friend std::ostream &operator<<(std::ostream &out, Macierz &p) {
    for (const auto &wiersz : p.macierz) {
      for (const auto &wartosc : wiersz) std::cout << wartosc << " ";
      std::cout << std::endl;
    }

    return out;
  }

  friend bool operator==(const Macierz &p1, const Macierz &p2) {
    return p1.macierz == p2.macierz;
  }

  friend bool operator!=(const Macierz &p1, const Macierz &p2) {
    return p1.macierz != p2.macierz;
  }

 private:
  std::vector<std::vector<int>> macierz;
};
int main() {
  Macierz macierzA(std::vector<std::vector<int>>{{1, -2, 3}});
  Macierz macierzB(std::vector<std::vector<int>>{{8, 9, -5}});

  auto suma = macierzA + macierzB;
  auto roznica = macierzA - macierzB;

  std::cout << "Macierz A \n"
            << macierzA << "Macierz B \n"
            << macierzB << std::endl
            << "suma: \n"
            << suma << std::endl
            << "roznica: \n"
            << roznica << std::endl;

  macierzA = Macierz(std::vector<std::vector<int>>{{1, 2, 3}});
  macierzB = Macierz(std::vector<std::vector<int>>{{4}, {5}, {6}});

  auto iloczynAB = macierzA * macierzB;
  auto iloczynBA = macierzB * macierzA;

  std::cout << "Macierz A \n"
            << macierzA << "Macierz B \n"
            << macierzB << std::endl
            << "iloczyn A*B: \n"
            << iloczynAB << std::endl
            << "iloczyn B*A: \n"
            << iloczynBA << std::endl;

  return 0;
}
