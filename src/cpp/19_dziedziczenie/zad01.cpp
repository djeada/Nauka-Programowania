/*
ZAD-01 — Wywołanie metody klasy bazowej w klasie potomnej

**Poziom:** ★☆☆
**Tagi:** `dziedziczenie`, `override`, `super`

### Treść

Zaprojektuj dwie klasy:

1. **Bazowa** — posiada metodę `przedstaw_sie()`, która wypisuje komunikat o
klasie bazowej.
2. **Potomna** — dziedziczy po **Bazowej** i **nadpisuje** metodę
`przedstaw_sie()`, ale w swojej implementacji:

   * najpierw **wywołuje** wersję metody z klasy bazowej,
   * potem dopisuje własny komunikat.

Program testowy:

* tworzy obiekt klasy potomnej,
* wywołuje metodę `przedstaw_sie()`.

### Wejście

Brak.

### Wyjście

Dwie linie, pokazujące najpierw komunikat klasy bazowej, a potem potomnej.

### Przykład

**Wyjście:**

```
Jestem klasą bazową.
A ja jestem klasą potomną.
```

*/

#include <iostream>

class Rodzic {
 public:
  void info() { std::cout << "Jestem rodzicem" << std::endl; }
};

class DzieckoA : public Rodzic {
 public:
  void info() { std::cout << "Jestem dzieckiem A" << std::endl; }
};

class DzieckoB : public Rodzic {
 public:
  void info() {
    std::cout << "Jestem dzieckiem B" << std::endl;
    Rodzic::info();
  }
};

int main() {
  Rodzic rodzic;
  rodzic.info();

  DzieckoA dzieckoA;
  dzieckoA.info();

  DzieckoB dzieckoB;
  dzieckoB.info();

  return 0;
}
