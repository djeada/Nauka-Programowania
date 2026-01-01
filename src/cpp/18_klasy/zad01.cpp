/*
ZAD-01 — Klasa Koło

**Poziom:** ★★☆
**Tagi:** `class`, `metody`, `float`, `math`

### Treść

Zaprojektuj klasę **Koło**:

1. Konstruktor przyjmuje promień `r` (domyślnie 1).
2. Metoda licząca **obwód**: ( 2\pi r )
3. Metoda licząca **pole**: ( \pi r^2 )
4. Metoda wypisująca informacje: promień, obwód i pole.

Program ma utworzyć koło o promieniu wczytanym z wejścia (np. 3) i wypisać
informacje.

### Wejście

* 1 linia: `r` (liczba rzeczywista)

### Wyjście

Trzy linie jak w przykładzie (obwód i pole do 4 miejsc po przecinku).

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
Koło o promieniu: 3
Obwód koła: 18.8496
Pole koła: 28.2743
```

*/

#include <cmath>
#include <iostream>
#include <numbers>

class Kolo {
 public:
  Kolo(double r) {
    if (r <= 0) {
      std::cout << "Promien nie moze byc liczba ujemna." << std::endl;
      std::cout << "Promien ustawiono na 1" << std::endl;
      promien = 1.0;
    }

    else
      promien = r;
  }

  void setPromien(double r) { promien = r; }

  double getPromien() { return promien; }

  double pole() { return std::numbers::pi * pow(promien, 2); }

  double obwod() { return 2 * std::numbers::pi * promien; }

  double srednica() { return 2 * promien; }

  friend std::ostream &operator<<(std::ostream &out, Kolo &k) {
    std::cout << "Promien = " << k.promien << std::endl;
    std::cout << "Srednica = " << k.srednica() << std::endl;
    std::cout << "Pole = " << k.pole() << std::endl;
    std::cout << "Obwod = " << k.obwod() << std::endl;

    return out;
  }

 private:
  double promien;
};

int main() {
  Kolo kolo(3);
  std::cout << kolo;

  return 0;
}
