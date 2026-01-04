/*
ZAD-11 — Samochody jadące w przeciwnych kierunkach

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`, `string`

### Treść

Wczytaj `N` oraz napis długości `N` złożony z liter `A` i `B`:

* `A` oznacza samochód jadący na wschód,
* `B` oznacza samochód jadący na zachód.

Policz, ile par samochodów minie się, gdy uznamy, że para mija się wtedy, gdy
`A` stoi **przed** `B` w ciągu.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* 2. linia: napis długości `N`, tylko `A` i `B` (bez spacji)

### Wyjście

Jedna liczba naturalna — liczba mijających się par.

### Przykład

**Wejście:**

```
5
ABABB
```

**Wyjście:**

```
5
```

*/
#include <iostream>
#include <string>

int main() {
  int n;
  std::cin >> n;

  std::string lista;
  std::cin >> lista;

  int licznik = 0;
  for (int i = 0; i < n; i++) {
    if (lista[i] == 'A') {
      for (int j = i + 1; j < n; j++) {
        if (lista[j] == 'B') licznik++;
      }
    }
  }

  std::cout << licznik << std::endl;

  return 0;
}
