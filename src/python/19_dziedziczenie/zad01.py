"""
ZAD-01 — Wywołanie metody klasy bazowej w klasie potomnej

**Poziom:** ★☆☆
**Tagi:** `dziedziczenie`, `override`, `super`

### Treść

Zaprojektuj dwie klasy:

1. **Bazowa** — posiada metodę `przedstaw_sie()`, która wypisuje komunikat o klasie bazowej.
2. **Potomna** — dziedziczy po **Bazowej** i **nadpisuje** metodę `przedstaw_sie()`, ale w swojej implementacji:

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

"""


class Rodzic:
    def __init__(self):
        print("Jestem rodzicem")


class DzieckoA(Rodzic):
    def __init__(self):
        print("Jestem dzieckiem A")


class DzieckoB(Rodzic):
    def __init__(self):
        print("Jestem dzieckiem B")
        super().__init__()


if __name__ == "__main__":

    print("Tworze obiekt klasy Rodzic:")
    rodzic = Rodzic()

    print("\nTworze obiekt klasy DzieckoA:")
    dziecko_a = DzieckoA()

    print("\nTworze obiekt klasy DzieckoB:")
    dziecko_b = DzieckoB()
