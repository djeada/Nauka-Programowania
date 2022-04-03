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
        var oczekiwane = 6;
        var wynik = Main.znajdzKluczV1(tablica, klucz);
        if (!(oczekiwane === wynik)) {
            throw new Error(`Assertion error line 20: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        };
    };
    Main.test2 = function() {
        var tablica = [3, -2, 4, 9, -3, -40, 8, 5, -7, -1];
        var klucz = 2;
        var oczekiwane = -1;
        var wynik = Main.znajdzKluczV1(tablica, klucz);
        if (!(oczekiwane === wynik)) {
            throw new Error(`Assertion error line 29: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.test3 = function() {
        var tablica = [3, 5, -7, 4, 9, -11, 2];
        var klucz = 2;
        var oczekiwane = 6;
        var wynik = Main.znajdzKluczV2(tablica, klucz);
        if (!(oczekiwane === wynik)) {
            throw new Error(`Assertion error line 38: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.test4 = function() {
        var tablica = [3, -2, 4, 9, -3, -40, 8, 5, -7, -1];
        var klucz = 2;
        var oczekiwane = -1;
        var wynik = Main.znajdzKluczV2(tablica, klucz);
        if (!(oczekiwane === wynik)) {
            throw new Error(`Assertion error line 47: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
        Main.test3();
        Main.test4();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
