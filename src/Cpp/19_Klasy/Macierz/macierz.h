#include <iostream>
#include <vector>

class Macierz {
public:
  Macierz(const std::vector<std::vector<int>> macierz =
              std::vector<std::vector<int>>());
  void setElement(unsigned int wiersz, unsigned int kolumna, int wartosc);
  int element(unsigned int wiersz, unsigned int kolumna) const;
  unsigned int wiersze() const;
  unsigned int kolumny() const;
  Macierz operator+(const Macierz &innaMacierz);
  Macierz operator-(const Macierz &innaMacierz);
  Macierz operator*(const Macierz &innaMacierz);
  friend std::ostream &operator<<(std::ostream &out, Macierz &m);
  friend bool operator==(const Macierz &m1, const Macierz &m2);
  friend bool operator!=(const Macierz &m1, const Macierz &m2);

private:
  std::vector<std::vector<int>> macierz;
};
