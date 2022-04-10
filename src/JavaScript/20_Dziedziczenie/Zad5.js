/*
Napisz klase Ptak, dziedziczaca po klasach Zwierz oraz ObiektLatajacy. 
a) W sklad klasy Zwierz powinny wchodzic funkcje wypisujace na standardowe 
wyjscie komunikaty odpowiadajace ich nazwom. Funkcje powinny miec 
nastepujace nazwy: jedz(), spij(), wydaj_dzwiek(). 
b) W sklad klasy ObiektLatajacy powinny wchodzic funkcje wypisujace na 
standardowe wyjscie komunikaty odpowiadajace ich nazwom. Funkcje powinny 
miec nastepujace nazwy: lec(), wyladuj().
*/

const Zwierz = (superclass) => class extends superclass {
    jedz() {
        console.log(`${this.nazwa} je`);
    }
    spij() {
        console.log(`${this.nazwa} spi`);
    }
    wydajDzwiek() {
        console.log(`${this.nazwa} wydaje dzwiek`);
    }
}

const ObiektLatajacy = (superclass) => class extends superclass {
    lec() {
        console.log(`${this.nazwa} leci`);
    }
    laduj() {
        console.log(`${this.nazwa} laduje`);
    }
}

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

main = function() {
    let ptak = new Ptak('Dziobak');
    ptak.jedz();
    ptak.spij();
    ptak.wydajDzwiek();
    ptak.lec();
    ptak.laduj();
}

main();