/*
Otrzymujesz dwie listy n wspolczynnikow wielomianu postaci a_nx^n +
a_(n-1)x^(n-1) + ... + a_0. Oblicz wspolczynniki wielomianu bedacego suma
otrzymanych wielomianow.
*/

var Main = /** @class */ (function () { 
    function Main() { }
    Main.dodajWielomiany = function (wspolczynniki1, wspolczynniki2) {
        var wynik = [];
        for (var i = 0; i < wspolczynniki1.length; i++) {
            wynik[i] = wspolczynniki1[i] + wspolczynniki2[i];
        }
        return wynik;
    }
    Main.test1 = function () {
        var wielomian1 = [3, 2, 1];
        var wielomian2 = [1, 2, 3];
        var oczekiwane = [4, 4, 4];
        var wynik = Main.dodajWielomiany(wielomian1, wielomian2);
        if (wynik.length !== oczekiwane.length) {
            throw new Error("Assertion error line 24: assert dodajWielomiany(wielomian1, wielomian2).length.equals(wynik.length);");
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error("Assertion error line 30: assert dodajWielomiany(wielomian1, wielomian2)[i].equals(wynik[i]);");
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
