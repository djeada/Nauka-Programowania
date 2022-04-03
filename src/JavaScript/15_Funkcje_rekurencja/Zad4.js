/*
Otrzymujesz liczbe N. Przy uzyciu rekurencji
oblicz silnie z otrzymanej liczby.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.silnia = function (n) {
        if (n <= 0) {
            return 1;
        }
        return n * Main.silnia(n - 1);
    }
    Main.test1 = function () {
        var n = 5;
        var oczekiwane = 120;
        var wynik = Main.silnia(n);
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
