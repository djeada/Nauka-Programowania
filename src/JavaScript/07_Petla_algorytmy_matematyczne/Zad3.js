var Main = /** @class */ (function() {
    function Main() {}
    Main.mnozenie = function(a, b) {
        var wynik = 0;
        for (var i = 0; i < b; i++) {
            {
                wynik += a;
            };
        }
        return wynik;
    };
    Main.dzielenie = function(a, b) {
        var wynik = 0;
        while ((a >= b)) {
            {
                a -= b;
                wynik++;
            }
        };
        return wynik;
    };
    Main.test1 = function() {
        var a = 2;
        var b = 3;
        var wynik = 6;
        if (!(Main.mnozenie(a, b) === wynik)) {
            throw new Error("Assertion error line 23: assert mnozenie(a, b) == wynik;");
        };
    };
    Main.test2 = function() {
        var a = 30;
        var b = 6;
        var wynik = 5;
        if (!(Main.dzielenie(a, b) === wynik)) {
            throw new Error("Assertion error line 30: assert dzielenie(a, b) == wynik;");
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
