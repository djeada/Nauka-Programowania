/*
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

*/
class Ksztalt {
  pobierzNazwe() {
    return "Ksztalt";
  }
}

class Kolo extends Ksztalt {
  constructor(promien) {
    super();
    this.promien = promien;
  }

  pobierzNazwe() {
    return "Kolo";
  }

  pobierzPole() {
    return Math.PI * this.promien * this.promien;
  }

  pobierzObwod() {
    return 2 * Math.PI * this.promien;
  }
}

class Kwadrat extends Ksztalt {
  constructor(bok) {
    super();
    this.bok = bok;
  }

  pobierzNazwe() {
    return "Kwadrat";
  }

  pobierzPole() {
    return this.bok * this.bok;
  }

  pobierzObwod() {
    return 4 * this.bok;
  }
}

const kolo = new Kolo(5);
console.log(kolo.pobierzNazwe()); // wyswietli "Kolo"
console.log(kolo.pobierzPole()); // wyswietli 78.53981633974483
console.log(kolo.pobierzObwod()); // wyswietli 31.41592653589793

const kwadrat = new Kwadrat(4);
console.log(kwadrat.pobierzNazwe()); // wyswietli "Kwadrat"
console.log(kwadrat.pobierzPole()); // wyswietli 16
console.log(kwadrat.pobierzObwod()); // wyswietli 16

