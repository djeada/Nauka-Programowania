var Main = /** @class */ (function() {
    function Main() {}
    Main.indeksMin = function(lista) {
        var n = lista.length;
        for (var i = 0; i < n - 1; i++) {
            {
                if (lista[i] > lista[i + 1]) {
                    return i + 1;
                }
            };
        }
        return 0;
    };
    Main.test1 = function() {
        var lista = [7, 8, -1, 4, 5]
        var oczekiwane = 2;
        var wynik = Main.indeksMin(lista);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 19: ${wynik} != ${oczekiwane}`);
        }
    };
    Main.test2 = function() {
        var lista = [2, 3, 4, 5, 6]
        var oczekiwane = 0;
        var wynik = Main.indeksMin(lista);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 27: ${wynik} != ${oczekiwane}`);
        }
    };
    Main.test3 = function() {
        var lista = [8, 9, 10, 11, 1]
        var oczekiwane = 4;
        var wynik = Main.indeksMin(lista);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 35: ${wynik} != ${oczekiwane}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
        Main.test3();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
