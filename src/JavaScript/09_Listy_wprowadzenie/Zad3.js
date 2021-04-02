var Main = /** @class */ (function() {
    function Main() {}
    Main.znajdzKluczV1 = function(tablica, klucz) {
        for (var i = 0; i < tablica.length; i++) {
            if (tablica[i] === klucz)
                return i;;
        }
        return -1;
    };
    Main.znajdzKluczV2 = function(tablica, klucz) {
        return tablica.indexOf(klucz);
    };

    Main.test1 = function() {
        var tablica = [3, 5, -7, 4, 9, -11, 2];
        var klucz = 2;
        var wynik = 6;
        if (!(Main.znajdzKluczV1(tablica, klucz) === wynik)) {
            throw new Error("Assertion error line 15: assert znajdzKluczV1(tablica, klucz) == wynik;");
        };
        if (!(Main.znajdzKluczV2(tablica, klucz) === wynik)) {
            throw new Error("Assertion error line 16: assert znajdzKluczV2(tablica, klucz) == wynik;");
        };
    };

    Main.test2 = function() {
        var tablica = [3, -2, 4, 9, -3, -40, 8, 5, -7, -1];
        var klucz = 2;
        var wynik = -1;
        if (!(Main.znajdzKluczV1(tablica, klucz) === wynik)) {
            throw new Error("Assertion error line 23: assert znajdzKluczV1(tablica, klucz) == wynik;");
        };
        if (!(Main.znajdzKluczV2(tablica, klucz) === wynik)) {
            throw new Error("Assertion error line 24: assert znajdzKluczV2(tablica, klucz) == wynik;");
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
