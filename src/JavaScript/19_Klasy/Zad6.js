/*
Napisz klase Zespolona reprezentujaca liczbe zespolona. W sklad klasy powinny wchodzic funkcje:
a) Konstruktor pobierajacy dwie liczby jako argumenty. Pierwsza liczba reprezentuje czesc 
rzeczywista, a druga czesc urojona liczby zespolonej. Domyslne wartosci dla obu argumentow to 0.
b) Funkcje zwracajace wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnozenie, 
dzielenie). Jesli jest to mozliwe nalezy przeciazyc operatory: +, -, *, /.
c) Funkcja wypisujaca informacje o liczbie zespolonej na standardowe wyjscie.
d) Funkcje umozliwiajace porownanie dwoch obiektow klasy Zespolona. Jesli jest to mozliwe nalezy 
przeciazyc operatory ==, !=.
e) Funkcja modul, zwracajaca modul liczby zespolonej. 
Napisz program testujacy twoja klase. Stworz liczby zespolone: A(9, 12) i B(-3, -3). Wypisz na 
standardowe wyjscie informacje o utworzonych liczbach zespolonych oraz ich sume, roznice pierwszej 
i drugiej, iloraz pierwszej przez druga oraz iloczyn liczb zespolonych.
*/

class Zespolona {
    constructor(rzeczywista, urojona) {
        this.rzeczywista = rzeczywista || 0;
        this.urojona = urojona || 0;
    }

    static dodaj(p1, p2) {
        return new Zespolona(p1.rzeczywista + p2.rzeczywista, p1.urojona + p2.urojona);
    }

    static odejmij(p1, p2) {
        return new Zespolona(p1.rzeczywista - p2.rzeczywista, p1.urojona - p2.urojona);
    }

    static mnoz(p1, p2) {
        return new Zespolona(p1.rzeczywista * p2.rzeczywista - p1.urojona * p2.urojona, p1.rzeczywista * p2.urojona + p1.urojona * p2.rzeczywista);
    }

    static dziel(p1, p2) {
        return new Zespolona((p1.rzeczywista * p2.rzeczywista + p1.urojona * p2.urojona) / (Math.pow(p2.rzeczywista, 2) + Math.pow(p2.urojona, 2)), (p1.urojona * p2.rzeczywista - p1.rzeczywista * p2.urojona) / (Math.pow(p2.rzeczywista, 2) + Math.pow(p2.urojona, 2)));
    }

    toString() {
        return `Liczba zespolona o wspolrzednych (${this.rzeczywista}, ${this.urojona})`;
    }

    wypisz() {
        console.log(this.toString());
    }

    equals(p2) {
        return this.rzeczywista === p2.rzeczywista && this.urojona === p2.urojona;
    }

    notEquals(p2) {
        return !this.equals(p2);
    }

    modul() {
        return Math.sqrt(Math.pow(this.rzeczywista, 2) + Math.pow(this.urojona, 2));
    }
}


main = function() {

    let A = new Zespolona(9, 12);
    let B = new Zespolona(-3, -3);

    console.log((`Liczba zespolona A: ${A.toString()}`));
    console.log((`Liczba zespolona B: ${B.toString()}`));

    let C = Zespolona.dodaj(A, B);
    let D = Zespolona.odejmij(A, B);
    let E = Zespolona.mnoz(A, B);
    let F = Zespolona.dziel(A, B);

    console.log((`Suma A + B: ${C.toString()}`));
    console.log((`Roznica A - B: ${D.toString()}`));
    console.log((`Iloczyn A * B: ${E.toString()}`));
    console.log((`Iloczyn A / B: ${F.toString()}`));

    console.log(`Modul liczby zespolonej A: ${A.modul()}`);
    console.log(`Modul liczby zespolonej B: ${B.modul()}`);
}

main();