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
        var wynik = 9;
        if (!(Main.znajdzMaksV1(tablica) === wynik)) {
            throw new Error("Assertion error line 23: assert znajdzMaksV1(tablica) == wynik;");
        };
        if (!(Main.znajdzMaksV2(tablica) === wynik)) {
            throw new Error("Assertion error line 24: assert znajdzMaksV2(tablica) == wynik;");
        };
    };

    Main.test2 = function() {
        var tablica = [3, -2, 4, 29, -3, -40, 8, 5, -7, -1];
        var wynik = 29;
        if (!(Main.znajdzMaksV1(tablica) === wynik)) {
            throw new Error("Assertion error line 30: assert znajdzMaksV1(tablica) == wynik;");
        };
        if (!(Main.znajdzMaksV2(tablica) === wynik)) {
            throw new Error("Assertion error line 31: assert znajdzMaksV2(tablica) == wynik;");
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
