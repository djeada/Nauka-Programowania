/*
Otrzymujesz dwie macierze o tych samych wymiarach, zwroc macierz bedaca:
a) Wynikiem dodawania otrzymanych macierzy.
b) Wynikiem odejmowania pierwszej macierzy od drugiej.
*/

var Main = /** @class */ (function () { 
    function Main() { }
    Main.dodajMacierze = function (macierzA, macierzB) {
        var wynik = [];
        for (var i = 0; i < macierzA.length; i++) {
            wynik[i] = [];
            for (var j = 0; j < macierzA[i].length; j++) {
                wynik[i][j] = macierzA[i][j] + macierzB[i][j];
            }
        }
        return wynik;
    }
    Main.odejmijMacierze = function (macierzA, macierzB) {
        var wynik = [];
        for (var i = 0; i < macierzA.length; i++) {
            wynik[i] = [];
            for (var j = 0; j < macierzA[i].length; j++) {
                wynik[i][j] = macierzA[i][j] - macierzB[i][j];
            }
        }
        return wynik;
    }
    Main.test1 = function () {
        var macierzA = [[1, 2, 3], [4, 5, 6]];
        var macierzB = [[7, 8, 9], [10, 11, 12]];
        var oczekiwane = [[8, 10, 12], [14, 16, 18]];
        var wynik = Main.dodajMacierze(macierzA, macierzB);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i].length !== oczekiwane[i].length) {
                throw new Error(`Assertion error line 29: ${wynik[i].length} != ${oczekiwane[i].length}`);
            }
            for (var j = 0; j < wynik[i].length; j++) {
                if (wynik[i][j] !== oczekiwane[i][j]) {
                    throw new Error(`Assertion error line 29: ${wynik[i][j]} != ${oczekiwane[i][j]}`);
                }
            }
        }
    };
    Main.test2 = function () {
        var macierzA = [[1, 2, 3], [4, 5, 6]];
        var macierzB = [[7, 8, 9], [10, 11, 12]];
        var oczekiwane = [[-6, -6, -6], [-6, -6, -6]];
        var wynik = Main.odejmijMacierze(macierzA, macierzB);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i].length !== oczekiwane[i].length) {
                throw new Error(`Assertion error line 29: ${wynik[i].length} != ${oczekiwane[i].length}`);
            }
            for (var j = 0; j < wynik[i].length; j++) {
                if (wynik[i][j] !== oczekiwane[i][j]) {
                    throw new Error(`Assertion error line 29: ${wynik[i][j]} != ${oczekiwane[i][j]}`);
                }
            }
        }
    };
    Main.main = function (args) {
        Main.test1();
        Main.test2();
    }
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
