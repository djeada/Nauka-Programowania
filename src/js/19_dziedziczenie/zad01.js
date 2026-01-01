/*
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

*/

class Zwierze {
  constructor(imie) {
    this.imie = imie;
  }

  dajGlos() {
    console.log("Jestem zwierzeciem!");
  }
}

class Pies extends Zwierze {
  constructor(imie) {
    super(imie);
  }

  dajGlos() {
    super.dajGlos();
    console.log("Jestem psem!");
  }
}

const zwierze = new Zwierze("Bajka");
zwierze.dajGlos(); // wyswietli "Jestem zwierzeciem!"

const pies = new Pies("Burek");
pies.dajGlos(); // wyswietli "Jestem zwierzeciem!" oraz "Jestem psem!"

