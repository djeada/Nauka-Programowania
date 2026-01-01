"""
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
* wywołuje metody w kolejności: `jedz`, `spij`, `wydaj_dzwiek`, `lec`, `wyladuj`.

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

"""


class Zwierz:
    def __init__(self, name):
        self.name = name

    def jedz(self):
        print(f"{self.name} jedzie")

    def spij(self):
        print(f"{self.name} spi")

    def wydaj_dzwiek(self):
        print(f"{self.name} wydaje dzwiek")


class ObiektLatajacy:
    def __init__(self, name):
        self.name = name

    def lec(self):
        print(f"{self.name} leci")

    def wyladuj(self):
        print(f"{self.name} wylada")


class Ptak(Zwierz, ObiektLatajacy):
    def __init__(self, name):
        Zwierz.__init__(self, name)
        ObiektLatajacy.__init__(self, name)


if __name__ == "__main__":

    ptak = Ptak("Dziobak")
    ptak.jedz()
    ptak.spij()
    ptak.wydaj_dzwiek()
    ptak.lec()
    ptak.wyladuj()
