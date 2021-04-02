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
        var lista = ([7, 8, -1, 4, 5].slice(0));
        var wynik = 2;
        if (!(Main.indeksMin(lista) === wynik)) {
            throw new Error("Assertion error line 15: assert indeksMin(lista) == wynik;");
        };
    };
    Main.test2 = function() {
        var lista = ([2, 3, 4, 5, 6].slice(0));
        var wynik = 0;
        if (!(Main.indeksMin(lista) === wynik)) {
            throw new Error("Assertion error line 21: assert indeksMin(lista) == wynik;");
        };
    };
    Main.test3 = function() {
        var lista = ([8, 9, 10, 11, 1].slice(0));
        var wynik = 4;
        if (!(Main.indeksMin(lista) === wynik)) {
            throw new Error("Assertion error line 27: assert indeksMin(lista) == wynik;");
        };
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
