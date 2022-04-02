/*
Otrzymujesz dwie macierze o tych samych wymiarach, zwroc macierz bedaca:
a) Wynikiem dodawania otrzymanych macierzy.
b) Wynikiem odejmowania pierwszej macierzy od drugiej.
*/

var Main = /** @class */ (function () { 
    function Main() { }
    Main.dodajWektory = function (wektorA, wektorB) {
        var wynik = [];
        if (wektorA.length !== wektorB.length) {
            return wynik;
        }
        for (var i = 0; i < wektorA.length; i++) {
            wynik[i] = wektorA[i] + wektorB[i];
        }
        return wynik;
    }
    Main.odejmijWektory = function (wektorA, wektorB) {
        var wynik = [];
        if (wektorA.length !== wektorB.length) {
            return wynik;
        }
        for (var i = 0; i < wektorA.length; i++) {
            wynik[i] = wektorA[i] - wektorB[i];
        }
        return wynik;
    }
    Main.test1 = function () {
        var wektorA = [1, 2, 3];
        var wektorB = [4, 5, 6];
        var wynik = [5, 7, 9];
        if (Main.dodajWektory(wektorA, wektorB).length !== wynik.length) {
            throw new Error("Assertion error line 24: assert dodajWektory(wektorA, wektorB).length.equals(wynik.length);");
        }
        for (var i = 0; i < wynik.length; i++) {
            if (Main.dodajWektory(wektorA, wektorB)[i] !== wynik[i]) {
                throw new Error("Assertion error line 30: assert dodajWektory(wektorA, wektorB)[i].equals(wynik[i]);");
            }
        }
    }
    Main.test2 = function () {
        var wektorA = [1, 2, 3];
        var wektorB = [4, 5, 6];
        var oczekiwane = [-3, -3, -3];
        var wynik = Main.odejmijWektory(wektorA, wektorB);
        if (wynik.length !== oczekiwane.length) {
            throw new Error("Assertion error line 24: assert odejmijWektory(wektorA, wektorB).length.equals(wynik.length);");
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error("Assertion error line 30: assert odejmijWektory(wektorA, wektorB)[i].equals(wynik[i]);");
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
