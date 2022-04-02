/*
Otrzymujesz dwie listy n wspolczynnikow wielomianu postaci a_nx^n +
a_(n-1)x^(n-1) + ... + a_0. Oblicz wspolczynniki wielomianu bedacego iloczynem
otrzymanych wielomianow.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.iloczyn = function (wspolczynniki1, wspolczynniki2) {
        var wynik = [];
        for (var i = 0; i < wspolczynniki1.length; i++) {
            for (var j = 0; j < wspolczynniki2.length; j++) {
                if (i + j >= wynik.length) {
                    wynik[i + j] = 0;
                }
                wynik[i + j] += wspolczynniki1[i] * wspolczynniki2[j];
            }
        }
        return wynik;
    }
    Main.test1 = function () {
        var wielomianA = [5, 0, 10, 6];
        var wielomianB = [1, 2, 4];
        var oczekiwane = [5, 10, 30, 26, 52, 24];
        var wynik = Main.iloczyn(wielomianA, wielomianB);
        if (wynik.length !== oczekiwane.length) {
            throw new Error("Assertion error line 24: assert iloczyn(wielomianA, wielomianB).length.equals(wynik.length);");
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error("Assertion error line 30: assert iloczyn(wielomianA, wielomianB)[i].equals(wynik[i]);");
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
//# sourceMappingURL=Zad4.js.m