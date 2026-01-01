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

*/

const Zwierz = (superclass) =>
  class extends superclass {
    jedz() {
      console.log(`${this.nazwa} je`);
    }
    spij() {
      console.log(`${this.nazwa} spi`);
    }
    wydajDzwiek() {
      console.log(`${this.nazwa} wydaje dzwiek`);
    }
  };

const ObiektLatajacy = (superclass) =>
  class extends superclass {
    lec() {
      console.log(`${this.nazwa} leci`);
    }
    laduj() {
      console.log(`${this.nazwa} laduje`);
    }
  };

class PtakBaza {
  constructor(nazwa) {
    this.nazwa = nazwa;
  }
}

class MixinBuilder {
  constructor(superclass) {
    this.superclass = superclass;
  }
  with(...mixins) {
    return mixins.reduce((c, mixin) => mixin(c), this.superclass);
  }
}

const mix = (superclass) => new MixinBuilder(superclass);
class Ptak extends mix(PtakBaza).with(Zwierz, ObiektLatajacy) {}

const main = function () {
  let ptak = new Ptak("Dziobak");
  ptak.jedz();
  ptak.spij();
  ptak.wydajDzwiek();
  ptak.lec();
  ptak.laduj();
};

main();

