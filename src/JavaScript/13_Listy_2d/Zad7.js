/*
Otrzymujesz liste list liczb naturalnych reprezentujaca macierz.
Jesli element macierzy jest rowny zero, zamien wszystkie elementy
w tej samej kolumnie i tym samym wierszu na zera.
*/

var Main = /** @class */ (function () { 
    function Main() { }
    Main.zamienNaZero = function (macierz) {
        var M = macierz.length;
        var N = macierz[0].length;
        var wiersze = new Array(M);
        var kolumny = new Array(N);
        for (var i = 0; i < M; i++) {
            wiersze[i] = 0;
            for (var j = 0; j < N; j++) {
                if (macierz[i][j] == 0) {
                    wiersze[i] = 1;
                    kolumny[j] = 1;
                }
            }
        }
        for (var i = 0; i < M; i++) {
            for (var j = 0; j < N; j++) {
                if (wiersze[i] == 1 || kolumny[j] == 1)
                    macierz[i][j] = 0;
            }
        }
        return macierz;
    }
    Main.test1 = function () {
        var macierz = [[1, 2, 3], [4, 0, 6], [7, 8, 9]];
        var oczekiwane = [[1, 0, 3], [0, 0, 0], [7, 0, 9]];
        var wynik = Main.zamienNaZero(macierz);
        if (wynik.length !== oczekiwane.length) {
            throw new Error("Assertion error line 24: assert zamienNaZero(macierz).length.equals(wynik.length);");
        }
        for (var i = 0; i < wynik.length; i++) {
            for (var j = 0; j < wynik[i].length; j++) {
                if (wynik[i][j] !== oczekiwane[i][j]) {
                    throw new Error("Assertion error line 30: assert zamienNaZero(macierz)[i][j].equals(wynik[i][j]);");
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
