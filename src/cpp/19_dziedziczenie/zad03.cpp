/*
ZAD-03 — Polimorfizm: Zwierz, Pies i Kot

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `override`

### Treść

Zaprojektuj klasy:

* **Zwierz** — metoda `odglos()` zwraca/drukuje ogólny dźwięk.
* **Pies** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.
* **Kot** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.

Program testowy:

* tworzy obiekty: `Zwierz`, `Pies`, `Kot`,
* umieszcza je w jednej kolekcji,
* iteruje i dla każdego wypisuje linię w formacie:
  `NazwaKlasy wydaje odgłos: ...`

### Wejście

Brak.

### Wyjście

Trzy linie, po jednej dla każdego obiektu.

### Przykład

**Wyjście:**

```
Zwierz wydaje odgłos: ...
Pies wydaje odgłos: Hau!
Kot wydaje odgłos: Miau!
```

*/

#include <cassert>
#include <iostream>
#include <vector>

class Zwierz {
 public:
  virtual void odglos() const { std::cout << "Jestem zwierzem" << std::endl; }
};

class Pies : public Zwierz {
 public:
  void odglos() const override { std::cout << "Hau" << std::endl; }
};

class Kot : public Zwierz {
 public:
  void odglos() const override { std::cout << "Miau" << std::endl; }
};

int main() {
  std::vector<Zwierz> zwierzaki{Zwierz(), Pies(), Kot()};

  for (const auto &zwierz : zwierzaki) zwierz.odglos();

  return 0;
}
