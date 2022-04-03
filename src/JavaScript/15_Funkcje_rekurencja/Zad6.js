/*
Otrzymujesz liczbe N. Oblicz wartosc N-tego wyrazu ciagu danego wzorem
rekurencyjnym: a_1 = 1 a_n = 1 + 2a_(n-1)
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.wartoscWyrazu = function (n) {
        if (n <= 1) {
            return n;
        }
        return 1 + 2 * Main.wartoscWyrazu(n - 1);
    }
    Main.test1 = function () {
        var n = 5;
        var oczekiwane = 31;
        if (Main.wartoscWyrazu(n) !== oczekiwane) {
            throw new Error("Assertion error line 24: assert zbudujNapis(n).equals(wynik);");
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
