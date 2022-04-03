/*
Otrzymuje dwie liczby a i b. Przy uzyciu rekurencji
oblicz ile wynosi a podniesione do b.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.potega = function (a, b) {
        if (b === 0) {
            return 1;
        }
        return a * Main.potega(a, b - 1);
    }
    Main.test1 = function () {
        var a = 2;
        var b = 3;
        var oczekiwane = 8;
        var wynik = Main.potega(a, b);
        if (wynik !== oczekiwane) {
            throw new Error("Assertion error line " + (__LINE__ - 1) + ": " + "oczekiwane: " + oczekiwane + ", " + "obliczone: " + wynik);
        }
    }
    Main.main = function (args) {
        Main.test1();
    }
    return Main;
}
());
Main["__class"] = "Main";
Main.main(null);
