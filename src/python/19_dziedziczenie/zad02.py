"""
ZAD-02 — Klasa Kształt oraz klasy Koło i Kwadrat

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `math`

### Treść

Zaprojektuj hierarchię klas:

* **Kształt** — klasa bazowa (ogólna) dla kształtów.
* **Koło** — dziedziczy po `Kształt`.
* **Kwadrat** — dziedziczy po `Kształt`.

Każda klasa ma mieć:

* metodę obliczającą **pole**,
* metodę wypisującą informacje o obiekcie: typ, parametry i pole.

Program:

* wczytuje promień `r` koła oraz bok `a` kwadratu,
* tworzy obiekty `Koło(r)` i `Kwadrat(a)`,
* wypisuje informacje o obu.

**Uwaga do formatowania:**
*Pole koła wypisz do 4 miejsc po przecinku.*
*Pole kwadratu wypisz bez wymuszania miejsc po przecinku (jak w przykładzie).*

### Wejście

* 1 linia: `r` (liczba rzeczywista)
* 2 linia: `a` (liczba rzeczywista)

### Wyjście

Blok informacji o kole, pusta linia, blok informacji o kwadracie.

### Przykład

**Wejście:**

```
5
4
```

**Wyjście:**

```
Kształt: Koło
Promień: 5
Pole powierzchni: 78.5398

Kształt: Kwadrat
Długość boku: 4
Pole powierzchni: 16
```

"""

import math


class Ksztalt:
    def __init__(self):
        raise NotImplementedError("Nie zaimplementowano konstruktora")

    def pole(self):
        raise NotImplementedError("Nie zaimplementowano funkcji pole")

    def obwod(self):
        raise NotImplementedError("Nie zaimplementowano funkcji obwod")

    def __str__(self):
        raise NotImplementedError("Nie zaimplementowano funkcji __str__")


class Kolo(Ksztalt):
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return math.pi * self.promien**2

    def obwod(self):
        return 2 * math.pi * self.promien

    def __str__(self):
        return f"Kolo o promieniu {self.promien}"


class Kwadrat(Ksztalt):
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok**2

    def obwod(self):
        return 4 * self.bok

    def __str__(self):
        return f"Kwadrat o boku {self.bok}"


if __name__ == "__main__":

    kolo = Kolo(5)
    print(f"{kolo}")
    print(f"Pole: {kolo.pole():.2f}")
    print(f"Obwod: {kolo.obwod():.2f}")
    print()

    kwadrat = Kwadrat(5)
    print(f"{kwadrat}")
    print(f"Pole: {kwadrat.pole():.2f}")
    print(f"Obwod: {kwadrat.obwod():.2f}")
