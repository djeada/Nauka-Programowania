/*

Tytuł: Dziedziczenie wielokrotne

Treść: Napisz klasę Ptak, dziedziczącą po klasach Zwierz i ObiektLatający. W skład klasy Zwierz powinny wchodzić funkcje o nazwach 'jedz()', 'spij()', 'wydaj_dźwięk()', które wypisują odpowiednie komunikaty na standardowe wyjście. W skład klasy ObiektLatający powinny wchodzić funkcje o nazwach 'leć()', 'wyląduj()', które wypisują odpowiednie komunikaty na standardowe wyjście. Napisz program testujący tę klasę.
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
