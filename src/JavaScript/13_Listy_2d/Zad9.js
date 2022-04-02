/*
Otrzymujesz liste list liczb naturalnych. Znajdz w macierzy klepsydre o
najwiekszej sumie. Klepsydra sklada sie z dokladnie 7 elementow. Trzy pierwsze
elementy sa kolejnymi elementami dowolnego wiersza macierzy. Nastepny element
znajduje sie w tej samej kolumnie co drugi element i w dokladnie jednym wierszu
nizej. Trzy nastepne znajduja sie w tych samych kolumnach co trzy pierwsze i
dokladnie dwa wiersze nizej.
*/

var Main = /** @class */ (function () { 
    function Main() { }
    Main.klepsydraNajwiekszaSuma = function (macierz) {
        var wynik = Number.MIN_SAFE_INTEGER;
        var N = macierz.length;
        for (var wiersz = 0; wiersz < N; wiersz++) {
            for (var kolumna = 0; kolumna < N; kolumna++) {
                if (!(wiersz == 0 || wiersz == N - 1 || kolumna == 0 || kolumna == N - 1)) {
                    var suma = macierz[wiersz - 1][kolumna - 1] + macierz[wiersz - 1][kolumna] + macierz[wiersz - 1][kolumna + 1] + macierz[wiersz][kolumna] + macierz[wiersz + 1][kolumna - 1] + macierz[wiersz + 1][kolumna] + macierz[wiersz + 1][kolumna + 1];
                    wynik = Math.max(wynik, suma);
                }
            }
        }
        return wynik;
    }
    Main.test1 = function () {
        var macierz = [[10, 99, 28, 21, 78], [35, 78, 31, 56, 24], [7, 18, 2, 50, 87], [59, 67, 9, 82, 53], [23, 26, 76, 62, 36]];
        var wynik = 395;
        if (Main.klepsydraNajwiekszaSuma(macierz) !== wynik) {
            throw new Error("Assertion error line 24: assert klepsydraNajwiekszaSuma(macierz) == wynik;");
        }
    }
    Main.main = function (args) {
        Main.test1();
    }
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
