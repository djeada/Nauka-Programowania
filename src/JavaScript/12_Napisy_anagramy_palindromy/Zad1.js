/*
Sprawdz czy slowo jest palindromem. Palindrom to slowo brzmiace tak samo
czytane od lewej do prawej i od prawej do lewej.
*/

var Main = /** @class */ (function () { 
    function Main() { } 
    Main.odwrocNapisV1 = function (slowo) {
        var rozdziel = slowo.split("");
        var odwroc = rozdziel.reverse();
        return odwroc.join("");
    }
    Main.odwrocNapisV2 = function (slowo) {
        if (slowo === "")
            return "";
        else
            return Main.odwrocNapisV2(slowo.substring(1)) + slowo.charAt(0);
    }
    Main.test1 = function () {
        var napis = "adam";
        var oczekiwane = "mada";
        var wynik = Main.odwrocNapisV1(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    }
    Main.test2 = function () {
        var napis = "adam";
        var oczekiwane = "mada";
        var wynik = Main.odwrocNapisV2(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 30: ${wynik} === ${oczekiwane}`);
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
