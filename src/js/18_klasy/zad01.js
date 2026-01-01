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

*/

class Kolo {
  constructor(promien = 1) {
    this.promien = promien;
  }

  obwod() {
    return 2 * Math.PI * this.promien;
  }

  pole() {
    return Math.PI * this.promien ** 2;
  }

  wypiszInfo() {
    console.log(
      `Kolo o promieniu ${
        this.promien
      }, obwod: ${this.obwod()}, pole: ${this.pole()}`
    );
  }
}

const mojeKolo = new Kolo(3);
mojeKolo.wypiszInfo();

