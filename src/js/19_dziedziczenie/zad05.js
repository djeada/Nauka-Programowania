/*

Tytul: Dziedziczenie wielokrotne

Tresc: Napisz klase Ptak, dziedziczaca po klasach Zwierz i ObiektLatajacy. W sklad klasy Zwierz powinny wchodzic funkcje o nazwach 'jedz()', 'spij()', 'wydaj_dzwiek()', ktore wypisuja odpowiednie komunikaty na standardowe wyjscie. W sklad klasy ObiektLatajacy powinny wchodzic funkcje o nazwach 'lec()', 'wyladuj()', ktore wypisuja odpowiednie komunikaty na standardowe wyjscie. Napisz program testujacy te klase.
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

