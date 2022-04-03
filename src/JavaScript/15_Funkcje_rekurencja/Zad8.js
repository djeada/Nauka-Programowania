/*
N krazkow o roznych srednicach ulozone jest na jednym z trzech slupkow
(A, B lub C). Na spodzie znajduje sie krazek o najwiekszej srednicy.
Kazdy nastepny krazek jest mniejszy od poprzedniego. Znajdz sposob na
przelozenie wszystkich krazkow na inny slupek. Pamietaj, ze nie wolno
klasc krazka o wiekszej srednicy na krazek o mniejszej srednicy, ani
przekladac kilku krazkow jednoczesnie.
*/

var Pair = /** @class */ (function () {
    function Pair(a, b) {
        this.first = a;
        this.second = b;
    }
    return Pair;
}());

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.hanoi = function (n) {
        var hanoiWew = function (n, a, b, c, wynik) {
            if (n == 1) {
                wynik.push(new Pair(a, b));
                return;
            }
            hanoiWew(n - 1, a, c, b, wynik);
            wynik.push(new Pair(a, b));
            hanoiWew(n - 1, c, b, a, wynik);
        };
        var wynik = new Array();
        hanoiWew(n, 'A', 'B', 'C', wynik);
        return wynik;
    };
    Main.test1 = function () {
        var n = 3;
        var oczekiwane = [
            new Pair('A', 'B'),
            new Pair('A', 'C'),
            new Pair('B', 'C'),
            new Pair('A', 'B'),
            new Pair('C', 'A'),
            new Pair('C', 'B'),
            new Pair('A', 'B')
        ];
        var wynik = Main.hanoi(n);
        if (wynik.length !== oczekiwane.length) {
            throw new Error("Assertion error line " + (__LINE__ - 1) + ": " + "oczekiwane: " + oczekiwane.length + ", " + "obliczone: " + wynik.length);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i].first !== oczekiwane[i].first || wynik[i].second !== oczekiwane[i].second) {
                throw new Error("Assertion error line " + (__LINE__ - 1) + ": " + "oczekiwane: " + oczekiwane[i] + ", " + "obliczone: " + wynik[i]);
            }
        }
    };
    Main.main = function (args) {
        Main.test1();
    };
    return Main;
}
());
Main["__class"] = "Main";
Main.main(null);
