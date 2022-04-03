/*
Otrzymujesz liste list liczb naturalnych. Obroc otrzymana liste o 90 stopni.
Tzn. zamien miejscami ostatnia kolumne z ostatnim wierszem, przedostatnia
kolumne z przedostatnim wierszem itd.
*/

var Main = /** @class */ (function () { 
    function Main() { }
    Main.obroc = function (macierz) {
        var N = macierz.length;
        for (var i = 0; i < N / 2; i++) {
            var pierwszy = i + 1;
            var ostatni = N - 1 - i;
            for (var j = pierwszy; j < ostatni; j++) {
                var pom = macierz[i][j];
                macierz[i][j] = macierz[N - 1 - j][i];
                macierz[N - 1 - j][i] = macierz[N - 1 - i][N - 1 - j];
                macierz[N - 1 - i][N - 1 - j] = macierz[j][N - 1 - i];
                macierz[j][N - 1 - i] = pom;
            }
            var pom = macierz[i][i];
            macierz[i][i] = macierz[N - 1 - i][i];
            macierz[N - 1 - i][i] = macierz[N - 1 - i][N - 1 - i];
            macierz[N - 1 - i][N - 1 - i] = macierz[i][N - 1 - i];
            macierz[i][N - 1 - i] = pom;
        }
        return macierz;
    }
    Main.test1 = function () {
        var macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
        var oczekiwane = [[7, 4, 1], [8, 5, 2], [9, 6, 3]];
        var wynik = Main.obroc(macierz);
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