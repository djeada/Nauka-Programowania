/*
ZAD-09 — Rozdziel informacje o pracowniku

**Poziom:** ★☆☆
**Tagi:** `split`, `formatowanie`

### Treść

Wczytaj linię z danymi pracownika rozdzielonymi średnikami `;`:

1. Imię, 2) Nazwisko, 3) Miejsce urodzenia, 4) Stanowisko, 5) Zarobki

Wypisz każdą informację w osobnej linii z etykietą.

### Wejście

* 1. linia: dane w formacie `Imię; Nazwisko; Miasto; Zawód; Zarobki;`

### Wyjście

Pięć linii w formacie:

* `Imię: ...`
* `Nazwisko: ...`
* `Miejsce urodzenia: ...`
* `Zawód: ...`
* `Zarobki: ...`

### Przykład

**Wejście:**

```
Jan; Kowalski; Warszawa; Programista; 1000;
```

**Wyjście:**

```
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Warszawa
Zawód: Programista
Zarobki: 1000
```

### Uwagi

* Po `split(';')` usuń ewentualne spacje z brzegów pól (np. `strip()`).
* Ostatni średnik może powodować pusty element na końcu — zignoruj go.

*/
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>

std::vector<std::string> dane(std::string &napis) {
  std::vector<std::string> wynik;
  std::stringstream ss(napis);

  for (std::string slowo; ss >> slowo;) {
    if (slowo.size() > 1) {
      wynik.push_back(slowo.substr(0, slowo.size() - 1));
      if (ss.peek() == ';') ss.ignore();
    }
  }

  return wynik;
}

void wypiszDane(std::string &napis) {
  std::vector<std::string> wynik = dane(napis);
  assert(wynik.size() == 5);

  std::cout << "Imie: " << wynik[0] << std::endl;
  std::cout << "Nazwisko: " << wynik[1] << std::endl;
  std::cout << "Miejsce urodzenia: " << wynik[2] << std::endl;
  std::cout << "Zawod: " << wynik[3] << std::endl;
  std::cout << "Zarobki: " << wynik[4] << std::endl;
}

int main() {
  std::string napis = "Jan; Kowalski; Warszawa; Programista; 1000";
  wypiszDane(napis);
  return 0;
}
