/*
Zaprojektuj klase Zwierz oraz klasy pochodne Pies oraz Kot. 
Obie klasy potomne powinny nadpisywac metode odglos() klasy 
zdefiniowana w klasie bazowej. Nastepnie w programie 
testujacym napisane klasy, nalezy w jednej liscie zebrac 
obiekty wszystkich trzech klas. Nalezy przy pomocy petli 
przejsc przez wszystkie elementy listy i dla kazdego z nich 
wywolac funkcje odglos().
*/

class Zwierz {
    constructor(imie) {
        this.imie = imie;
    }

    odglos() {
        console.log(`Odglos zwierzecia ${this.imie}`);
    }
}

class Pies extends Zwierz {
    odglos() {
        console.log(`Hau hau!`);
    }
}

class Kot extends Zwierz {
    odglos() {
        console.log(`Miau miau!`);
    }
}


main = function() {
    let zwierz1 = new Zwierz('Zwierz');
    let zwierz2 = new Pies('Burek');
    let zwierz3 = new Kot('Mruczek');

    let zwierzaki = [zwierz1, zwierz2, zwierz3];

    for (let i = 0; i < zwierzaki.length; i++) {
        zwierzaki[i].odglos();
    }
}

main();