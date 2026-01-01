/*
ZAD-06 — Wiersze kończące się określonym napisem

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`, `linijki`

### Treść

Otrzymujesz dwa napisy:

1. tekst wielowierszowy,
2. słowo lub fragment.

Znajdź wszystkie wiersze, które kończą się podanym napisem (wiersz może kończyć
się znakiem interpunkcyjnym).

### Wejście

Dwie części:

1. Tekst (wiele wierszy)
2. W osobnej linii: `koncowka`

*(Sposób wczytania tekstu wielowierszowego zależy od platformy — przyjmij, że
tekst jest podany w całości jako wejście, a ostatnia linia to `koncowka`.)*

### Wyjście

Wiersze spełniające warunek, każdy w osobnej linii, w kolejności występowania.

### Przykład

**Wejście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godności trzeba nie za nic tu cnota,
Miłości pragną nie pragną tu złota.
da
```

**Wyjście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
```

*/

#include <cassert>
#include <regex>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> rozdziel(const std::string &napis) {
  std::vector<std::string> wynik;
  std::string wiersz;
  std::istringstream strumien(napis);
  while (std::getline(strumien, wiersz, '\n')) wynik.push_back(wiersz);

  return wynik;
}

std::vector<std::string> wiersze(std::string &tekst, std::string &napis) {
  std::vector<std::string> wynik;
  std::regex wzorzec(std::string(".*" + napis + "[;,!?\\.]?"));

  auto _wiersze = rozdziel(tekst);

  for (auto &wiersz : _wiersze) {
    if (regex_match(wiersz, wzorzec)) wynik.push_back(wiersz);
  }

  return wynik;
}

void test1() {
  std::string tekst =
      "Folgujmy paniom nie sobie, ma rada;\nMilujmy wiernie "
      "nie jest w nich przysada.\nGodnosci trzeba nie za nic "
      "tu cnota,\nMilosci pragna nie pragna tu zlota";
  std::string napis = "ada";
  std::vector<std::string> wynik{"Folgujmy paniom nie sobie, ma rada;",
                                 "Milujmy wiernie nie jest w nich przysada."};

  assert(wiersze(tekst, napis) == wynik);
}

int main() {
  test1();

  return 0;
}
