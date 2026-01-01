/*
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

*/

class Klasa {
  constructor() {
    if (typeof Klasa.liczbaInstancji === "undefined") {
      Klasa.liczbaInstancji = 0;
    }
    Klasa.liczbaInstancji++;
  }

  static podajLiczbeInstancji() {
    return Klasa.liczbaInstancji;
  }
}

for (let i = 0; i < 3; i++) {
  new Klasa();
}

console.log(Klasa.podajLiczbeInstancji()); // wyswietli 3

