"""
ZAD-01 — Klasa Koło

**Poziom:** ★★☆
**Tagi:** `class`, `metody`, `float`, `math`

### Treść

Zaprojektuj klasę **Koło**:

1. Konstruktor przyjmuje promień `r` (domyślnie 1).
2. Metoda licząca **obwód**: ( 2\pi r )
3. Metoda licząca **pole**: ( \pi r^2 )
4. Metoda wypisująca informacje: promień, obwód i pole.

Program ma utworzyć koło o promieniu wczytanym z wejścia (np. 3) i wypisać informacje.

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

"""

import math


class Kolo:
    def __init__(self, promien=1):
        self.promien = promien

    def obwod(self):
        return 2 * math.pi * self.promien

    def pole(self):
        return math.pi * self.promien * self.promien

    def __str__(self):
        return f"Kolo o promieniu {self.promien:.2f}\nObwod: {self.obwod():.2f}\nPole: {self.pole():.2f}"


if __name__ == "__main__":
    kolo = Kolo(3)
    print(kolo)
