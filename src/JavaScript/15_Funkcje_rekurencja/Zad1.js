/*
Otrzymujesz liczbe N. Przy uzyciu rekurencji zbuduj napis skladajacy
sie z liczb naturalnych mniejszych od N oddzielonych przecinkami.
*/
 

var Main = /** @class */ (function () { 
    function Main() { }
    Main.zbudujNapis = function (n) {
        if (n === 0) {
            return "";
        }

        if (n === 1) {
            return "1";
        }

        return Main.zbudujNapis(n - 1) + "," + n;
    } 
    Main.test1 = function () {
        var n = 5;
        var oczekiwane = "1,2,3,4,5";
        var wynik = Main.zbudujNapis(n);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    }
    Main.main = function (args) {
        Main.test1();
    }
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
