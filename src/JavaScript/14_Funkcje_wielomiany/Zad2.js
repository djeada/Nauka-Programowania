/*
Otrzymujesz liste n wspolczynnikow wielomianu postaci a_nx^n + a_(n-1)x^(n-1) +
... + a_0 oraz liczbe x. Oblicz wspolczynniki wielomianu bedacego wynikiem
przemnozenia otrzymanego wielomianu przez liczbe x.
*/

var Main = /** @class */ (function () { 
    function Main() { }
    Main.przemnozWielomian = function (wspolczynniki, x) {
        var wynik = [];
        for (var i = 0; i < wspolczynniki.length; i++) {
            wynik[i] = wspolczynniki[i] * x;
        }
        return wynik;
    }
    Main.test1 = function () {
        var wielomian = [3, 2, 1];
        var x = 2;
        var oczekiwane = [6, 4, 2];
        var wynik = Main.przemnozWielomian(wielomian, x);
        if (wynik.length !== oczekiwane.length) {
            throw new Error("Assertion error line 24: assert przemnozWielomian(wielomian, x).length.equals(wynik.length);");
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error("Assertion error line 30: assert przemnozWielomian(wielomian, x)[i].equals(wynik[i]);");
            }
        }
    }
    Main.main = function (args) {
        Main.test1();
    }
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);

