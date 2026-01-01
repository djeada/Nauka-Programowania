"""
ZAD-07 — Zliczanie instancji klasy

**Poziom:** ★☆☆
**Tagi:** `class`, `static`

### Treść

Zaprojektuj klasę **MojaKlasa**, która zlicza ile instancji utworzono:

* prywatne pole statyczne licznik,
* konstruktor zwiększa licznik,
* metoda statyczna zwraca licznik.

Program tworzy np. 3 obiekty i wypisuje liczbę instancji.

### Wejście

Brak.

### Wyjście

Jedna linia.

### Przykład

**Wyjście:**

```
Liczba utworzonych instancji: 3
```

"""


class Klasa:
    liczba_instancji = 0

    def __init__(self):
        Klasa.liczba_instancji += 1

    def __del__(self):
        Klasa.liczba_instancji -= 1


if __name__ == "__main__":
    a = Klasa()
    b = Klasa()
    print(Klasa.liczba_instancji)
    del a
    del b
    print(Klasa.liczba_instancji)
