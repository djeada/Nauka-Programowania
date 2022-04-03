/*
Otrzymujesz dwie liczby, a oraz b. Stworz macierz a identycznych
wierszy skladajacych sie z liczb od 0 do b.
*/

var Main = /** @class */ (function () { 
    function Main() { }
    Main.stworzMacierz = function (a, b) {
        var macierz = [];
        for (var i = 0; i < a; i++) {
            macierz[i] = [];
            for (var j = 0; j <= b; j++) {
                macierz[i][j] = j;
            }
        }
        return macierz;
    };
    Main.test1 = function () {
        var a = 2;
        var oczekiwane = [[0, 1, 2, 3], [0, 1, 2, 3]];
        var wynik = Main.stworzMacierz(a);
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
    }
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
