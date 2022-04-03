var Main = /** @class */ (function() {
    function Main() {}
    Main.znajdzMaksV1 = function(tablica) {
        var maks = tablica[0];
        for (var i = 0; i < tablica.length; i++) {
            var elem = tablica[i];
            if (elem > maks)
                maks = elem;
        }
        return maks;
    };
    Main.znajdzMaksV2 = function(tablica) {
        var maks = tablica[0];
        for (var i = 0; i < tablica.length; i++) {
            var elem = tablica[i];
            maks = Math.max(maks, elem);
        }
        return maks;
    };

    Main.test1 = function() {
        var tablica = [3, 5, -7, 4, 9, -11, 2];
        var oczekiwane = 9;
        var wynik = Main.znajdzMaksV1(tablica);
        if (!(oczekiwane === wynik)) {
            throw new Error(`Assertion error line 26: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };

    Main.test2 = function() {
        var tablica = [3, -2, 4, 29, -3, -40, 8, 5, -7, -1];
        var oczekiwane = 29;
        var wynik = Main.znajdzMaksV1(tablica);
        if (!(oczekiwane === wynik)) {
            throw new Error(`Assertion error line 35: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.test3 = function() {
        var tablica = [3, 5, -7, 4, 9, -11, 2];
        var oczekiwane = 9;
        var wynik = Main.znajdzMaksV2(tablica);
        if (!(oczekiwane === wynik)) {
            throw new Error(`Assertion error line 43: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.test4 = function() {
        var tablica = [3, -2, 4, 29, -3, -40, 8, 5, -7, -1];
        var oczekiwane = 29;
        var wynik = Main.znajdzMaksV2(tablica);
        if (!(oczekiwane === wynik)) {
            throw new Error(`Assertion error line 51: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
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
