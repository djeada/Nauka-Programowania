var Main = /** @class */ (function() {
    function Main() {}
    Main.sumaCiaguArt = function(lista) {
        var minimum = Math.min.apply(Math, lista);
        var maksimum = Math.max.apply(Math, lista);

        return ((lista.length + 1) * (minimum + maksimum) / 2);
    };
    Main.znajdzBrakujacyElement = function(lista) {
        var suma = 0;
        for (var i = 0; i < lista.length; i++) {
            var liczba = lista[i]; {
                suma += liczba;
            }
        }
        var sumaPrzedzialu = Main.sumaCiaguArt(lista);
        return sumaPrzedzialu - suma;
    };
    Main.test1 = function() {
        var lista = ([6, 8, 4, 10, 14, 2].slice(0));
        var wynik = 12;
        if (!(Main.znajdzBrakujacyElement(lista) === wynik)) {
            throw new Error("Assertion error line 23: assert znajdzBrakujacyElement(lista) == wynik;");
        };
    };
    Main.test2 = function() {
        var lista = ([1, 2, 4, 5, 6].slice(0));
        var wynik = 3;
        if (!(Main.znajdzBrakujacyElement(lista) === wynik)) {
            throw new Error("Assertion error line 29: assert znajdzBrakujacyElement(lista) == wynik;");
        };
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
