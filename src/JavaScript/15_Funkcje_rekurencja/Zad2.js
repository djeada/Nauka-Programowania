/*
Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz
sume liczb naturalnych mniejszych od N.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.sumaLiczb = function (n) {
        if (n === 0) {
            return 0;
        }
        return n + Main.sumaLiczb(n - 1);
    }
    Main.test1 = function () {
        var n = 5;
        var oczekiwane = 15;
        var wynik = Main.sumaLiczb(n);
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
