/*
ZAD-05 — Dziedziczenie wielokrotne: Ptak

**Poziom:** ★★☆
**Tagi:** `multiple inheritance`, `dziedziczenie`, `metody`

### Treść

Zaprojektuj klasy:

* **Zwierz** — metody:

  * `jedz()` → wypisuje `Ptak je.`
  * `spij()` → wypisuje `Ptak śpi.`
  * `wydaj_dzwiek()` → wypisuje `Ptak wydaje dźwięk.`

* **ObiektLatajacy** — metody:

  * `lec()` → wypisuje `Ptak leci.`
  * `wyladuj()` → wypisuje `Ptak ląduje.`

* **Ptak** — dziedziczy po `Zwierz` oraz `ObiektLatajacy`.

Program testowy:

* tworzy obiekt `Ptak`,
* wywołuje metody w kolejności: `jedz`, `spij`, `wydaj_dzwiek`, `lec`,
`wyladuj`.

### Wejście

Brak.

### Wyjście

Pięć linii jak w przykładzie.

### Przykład

**Wyjście:**

```
Ptak je.
Ptak śpi.
Ptak wydaje dźwięk.
Ptak leci.
Ptak ląduje.
```

*/

#include <iostream>

class Zwierz {
 private:
  std::string nazwa;
  std::string pokarm;
  std::string dzwiek;

 public:
  Zwierz(std::string nazwa, std::string pokarm, std::string dzwiek)
      : nazwa(nazwa), pokarm(pokarm), dzwiek(dzwiek) {}

  void jedz() {
    std::cout << nazwa << " spozywa " << pokarm << "." << std::endl;
  }

  void spij() { std::cout << nazwa << " idzie spac." << std::endl; }

  void wydajDzwiek() { std::cout << dzwiek << std::endl; }
};

class ObiektLatajacy {
 private:
  std::string nazwa;

 public:
  ObiektLatajacy(std::string nazwa) : nazwa(nazwa) {}

  void lec() { std::cout << nazwa << " wznosi sie w powietrze." << std::endl; }

  void laduj() { std::cout << nazwa << " laduje." << std::endl; }
};

class Ptak : public Zwierz, public ObiektLatajacy {
 public:
  Ptak(std::string nazwa)
      : Zwierz(nazwa, "robaki", "Aww!Aww!"), ObiektLatajacy(nazwa) {}
};

int main() {
  Ptak koliber("Koliberek");
  koliber.jedz();
  koliber.lec();
  koliber.laduj();
  koliber.wydajDzwiek();
  koliber.spij();

  return 0;
}
