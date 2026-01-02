/*
ZAD-03 — Z ilu słów składa się zdanie?

**Poziom:** ★☆☆
**Tagi:** `string`, `split`

### Treść

Wczytaj zdanie i policz, z ilu słów się składa. Znaki interpunkcyjne nie są
słowami.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: liczba słów

### Przykład

**Wejście:**

```
gram na pianinie.
```

**Wyjście:**

```
3
```

### Uwagi o formatowaniu

* Najprościej: podziel po białych znakach, a z końców słów usuń interpunkcję.

*/
#include <algorithm>
#include <cassert>
#include <string>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
int policzSlowaV1(std::string &slowo) {
  bool spacja = true;
  int licznik = 0;

  for (auto znak : slowo) {
    if (isspace(znak))
      spacja = true;
    else if (isalpha(znak) && spacja) {
      licznik++;
      spacja = false;
    }
  }

  return licznik;
}

void test1() {
  std::string napis = "Ile to   ma :  slow w swoim zdaniu na   koniec?";
  int wynik = 9;

  assert(policzSlowaV1(napis) == wynik);
}

int main() {
  test1();
  return 0;
}
