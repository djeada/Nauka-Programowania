/*
Otrzymuejsz napis. Sprawdz przy pomocy rekurencji czy otrzymane slowo
jest slowem elfickim. Przez slowo elfickie rozumiemy taki napis, w
ktorym co najmniej raz wystepuje kazda z liter slowa elf.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.znajdz = function (slowo, znak, pozycja) {
        if (pozycja === void 0) { pozycja = 0; }
        if (pozycja >= slowo.length)
            return -1;
        if (slowo[pozycja] == znak)
            return pozycja;
        return Main.znajdz(slowo, znak, pozycja + 1);
    }
    Main.czySlowoElfickie = function (slowo, elf) {
        if (elf === void 0) { elf = "elf"; }
        if (elf.length === 0)
            return true;
        if (slowo.length === 0)
            return false;
        var pozycja = Main.znajdz(slowo, elf[0]);
        if (pozycja === -1)
            return false;
        
        slowo = slowo.substring(0, pozycja) + slowo.substring(pozycja + 1);
        return Main.czySlowoElfickie(slowo, elf.substr(1));
    }
    Main.test1 = function () {
        var slowo = "reflektor";
        var oczekiwane = true;
        var wynik = Main.czySlowoElfickie(slowo);
        if (wynik !== oczekiwane) {
            throw new Error("Assertion error line " + (__LINE__ - 1) + ": " + "oczekiwane: " + oczekiwane + ", " + "obliczone: " + wynik);
        }
    }
    Main.test2 = function () {
        var slowo = "elzbieta";
        var oczekiwane = false;
        var wynik = Main.czySlowoElfickie(slowo);
        if (wynik !== oczekiwane) {
            throw new Error("Assertion error line " + (__LINE__ - 1) + ": " + "oczekiwane: " + oczekiwane + ", " + "obliczone: " + wynik);
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
