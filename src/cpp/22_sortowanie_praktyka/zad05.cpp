/*
ZAD-05 — Sortowanie listy miast

**Poziom:** ★☆☆
**Tagi:** `class`, `sort`, `obiekty`

### Treść

Masz klasę `Miasto` z polami:

* `nazwa` (napis),
* `liczba_mieszkancow` (liczba naturalna).

Otrzymujesz listę miast.

a) Posortuj miasta alfabetycznie po nazwie.
b) Posortuj miasta rosnąco po liczbie mieszkańców.

Wypisz wyniki w dwóch liniach jako listy w formacie jak w przykładzie.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: `nazwa liczba_mieszkancow` (nazwa bez spacji)

### Wyjście

* 1 linia: lista miast po sortowaniu a)
* 2 linia: lista miast po sortowaniu b)

### Przykład

**Wejście:**

```
3
Paris 2150000
Berlin 3800000
New_York 8400000
```

**Wyjście:**

```
[Miasto("Berlin", 3800000), Miasto("New_York", 8400000), Miasto("Paris",
2150000)] [Miasto("Paris", 2150000), Miasto("Berlin", 3800000),
Miasto("New_York", 8400000)]
```

### Uwagi o formatowaniu

* Wydruk obiektów ma mieć dokładnie format: `Miasto("NAZWA", LICZBA)`.

*/

#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

class Miasto {
  std::string nazwa;
  int liczbaMieszkancow;

 public:
  Miasto(std::string _nazwa, int _liczbaMieszkancow)
      : nazwa(_nazwa), liczbaMieszkancow(_liczbaMieszkancow){};

  bool operator==(const Miasto &m) const {
    return nazwa == m.getNazwa() &&
           liczbaMieszkancow == m.getLiczbaMieszkancow();
  }

  std::string getNazwa() const { return nazwa; };
  int getLiczbaMieszkancow() const { return liczbaMieszkancow; };
};

void sortujWzgledemNazwy(std::vector<Miasto> &lista) {
  std::sort(lista.begin(), lista.end(),
            [](auto rhs, auto lhs) { return rhs.getNazwa() < lhs.getNazwa(); });
}

void sortujWzgledemLiczby(std::vector<Miasto> &lista) {
  std::sort(lista.begin(), lista.end(), [](auto rhs, auto lhs) {
    return rhs.getLiczbaMieszkancow() < lhs.getLiczbaMieszkancow();
  });
}

void test1() {
  std::vector<Miasto> miasta{Miasto("New York", 8400000),
                             Miasto("Paris", 2150000),
                             Miasto("Berlin", 3800000)};
  std::vector<Miasto> wynik{Miasto("Berlin", 3800000),
                            Miasto("New York", 8400000),
                            Miasto("Paris", 2150000)};

  sortujWzgledemNazwy(miasta);

  assert(miasta == wynik);
}

void test2() {
  std::vector<Miasto> miasta{Miasto("New York", 8400000),
                             Miasto("Paris", 2150000),
                             Miasto("Berlin", 3800000)};

  std::vector<Miasto> wynik{Miasto("Paris", 2150000), Miasto("Berlin", 3800000),
                            Miasto("New York", 8400000)};
  sortujWzgledemLiczby(miasta);

  assert(miasta == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
