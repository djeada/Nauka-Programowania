/*
Otrzymujesz liczbe N. Przy uzyciu rekurencji
oblicz wartosc N-tego wyrazu ciagu Fibonacciego.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.fibonacci = function (n) {
        if (n <= 1) {
            return n;
        }
        return Main.fibonacci(n - 1) + Main.fibonacci(n - 2);
    }
    Main.test1 = function () {
        var n = 5;
        var oczekiwane = 5;
        var wynik = Main.fibonacci(n);
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
