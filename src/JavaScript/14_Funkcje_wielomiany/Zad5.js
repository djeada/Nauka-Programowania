/*
Otrzymujesz liste n wspolczynnikow wielomianu postaci anxn+an-1xn-1+...+a0
oraz liczbe k. Oblicz wspolczynniki wielomianu bedacego k-ta pochodna
otrzymanego wielomianu.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.pochodnaWielomianu = function (wspolczynniki, k) {
        var wynik = [];
        var kopia = wspolczynniki.slice();
        for (var i = 0; i < k; i++) {
            wynik = [];
            var n = kopia.length;
            for (var j = 0; j < n - 1; j++)
                wynik.push(kopia[j] * (n - j - 1));
            kopia = wynik;
        }
        return wynik;
    }
    Main.test1 = function () {
        var wielomian = [4, -3, 2];
        var k = 1;
        var oczekiwane = [8, -3];
        var wynik = Main.pochodnaWielomianu(wielomian, k);
        if (wynik.length !== oczekiwane.length) {
            throw new Error("Assertion error line 24: assert pochodnaWielomianu(wielomian, k).length.equals(wynik.length);");
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error("Assertion error line 30: assert pochodnaWielomianu(wielomian, k)[i].equals(wynik[i]);");
            }
        }
    };
    Main.test2 = function () {
        var wielomian = [13, -6, 0, -1, -1];
        var k = 2;
        var oczekiwane = [156, -36, 0];
        var wynik = Main.pochodnaWielomianu(wielomian, k);
        if (wynik.length !== oczekiwane.length) {
            throw new Error("Assertion error line 24: assert pochodnaWielomianu(wielomian, k).length.equals(wynik.length);");
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error("Assertion error line 30: assert pochodnaWielomianu(wielomian, k)[i].equals(wynik[i]);");
            }
        }
    }
    Main.main = function (args) {
        Main.test1();
        Main.test2();
    }
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
