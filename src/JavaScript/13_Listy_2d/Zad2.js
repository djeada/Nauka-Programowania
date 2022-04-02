/*
Dla otrzymanej liczby, stworz macierz kwadratowa skladajaca sie
z liczby kolumn i wierszy rownej otrzymanej liczbie, ktorej kazdy
element jest iloczynem jego wspolrzednych.
*/

var Main = /** @class */ (function () { 
    function Main() { }
    Main.stworzMacierz = function (a) {
        var macierz = [];
        for (var i = 0; i < a; i++) {
            macierz[i] = [];
            for (var j = 0; j < a; j++) {
                macierz[i][j] = i * j;
            }
        }
        return macierz;
    }
    Main.test1 = function () {
        var a = 3;
        var oczekiwane = [[0, 0, 0], [0, 1, 2], [0, 2, 4]];
        var wynik = Main.stworzMacierz(a);
        if (wynik.length !== oczekiwane.length) {
            throw new Error("Assertion error line 24: assert stworzMacierz(a).length.equals(wynik.length);");
        }
        for (var i = 0; i < wynik.length; i++) {
            for (var j = 0; j < wynik[i].length; j++) {
                if (wynik[i][j] !== oczekiwane[i][j]) {
                    throw new Error("Assertion error line 30: assert stworzMacierz(a)[i][j].equals(wynik[i][j]);");
                }
            }
        }
    }
    Main.main = function (args) {
        Main.test1();
    }
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
