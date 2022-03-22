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
        var wynik = Main.liczbaZnakow(slowoA, slowoB);
        if (wynik !== 0) {
            throw new Error("Assertion error line 24: assert wynik === 0;");
        };
    };
    Main.test2 = function () {
        var slowoA = "adam";
        var slowoB = "ada";
        var wynik = Main.liczbaZnakow(slowoA, slowoB);
        if (wynik !== -1) {
            throw new Error("Assertion error line 30: assert wynik === -1;");
        };
    };
      Main.test3 = function () {
        var slowoA = "20ejdy0978oa";
        var slowoB = "akv81w39j1ob";
        var wynik = Main.liczbaZnakow(slowoA, slowoB);
        if (wynik !== 14) {
            throw new Error("Assertion error line 67: assert wynik === 14;");
        };
    };
    Main.main = function (args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
