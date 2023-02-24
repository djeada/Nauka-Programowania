/*
Dla dowolnych dwoch klas, dla ktorych jedna jest klasa bazowa, 
a druga klasa potomna wywolaj metode klasy bazowej w metodzie 
klasy potomnej nadpisujacej ta metode.
*/


class Bazowa {

    wypisz() {
        console.log('Bazowa');
    }

}

class Potomna extends Bazowa {

    wypisz() {
        super.wypisz();
        console.log('Potomna');
    }

}


main = function() {
    b = new Bazowa();
    p = new Potomna();
    b.wypisz();
    p.wypisz();
}

main();