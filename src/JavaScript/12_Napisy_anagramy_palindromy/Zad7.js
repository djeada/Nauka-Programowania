/*
Dla dwoch slow, ile minimalnie znakow musimy usunac aby uzyskac anagramy.
Zwroc -1 dla slow o roznych dlugosciach.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.liczbaZnakow = function (slowoA, slowoB) {
        if (slowoA.length !== slowoB.length)
            return -1;
        var pom = new Array(256);
        for (var i = 0; i < 256; i++)
            pom[i] = 0;
        for (var i = 0; i < slowoA.length; i++) {
            pom[slowoA.charCodeAt(i)]++;
        }
        for (var i = 0; i < slowoB.length; i++) {
            pom[slowoB.charCodeAt(i)]--;
        }
        var wynik = 0;
        for (var i = 0; i < pom.length; i++) {
            wynik += Math.abs(pom[i]);
        }
        return wynik;
    };
    Main.test1 = function () {
        var slowoA = "adam";
        var slowoB = "mada";
        var oczekiwane = 0;
        var wynik = Main.liczbaZnakow(slowoA, slowoB);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 29: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.test2 = function () {
        var slowoA = "adam";
        var slowoB = "ada";
        var oczekiwane = -1;
        var wynik = Main.liczbaZnakow(slowoA, slowoB);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 29: ${wynik} === ${oczekiwane}`);
        }
    };
      Main.test3 = function () {
        var slowoA = "20ejdy0978oa";
        var slowoB = "akv81w39j1ob";
        var oczekiwane = 14;
        var wynik = Main.liczbaZnakow(slowoA, slowoB);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 29: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.main = function (args) {
        Main.test1();
        Main.test2();
        Main.test3();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
