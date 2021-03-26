var Main = /** @class */ (function() {
    function Main() {}
    Main.silnia = function(a) {
        var wynik = 1;
        while ((a > 0)) {
            {
                wynik *= a;
                a--;
            }
        };
        return wynik;
    };
    Main.test1 = function() {
        var a = 4;
        var wynik = 24;
        if (!(Main.silnia(a) === wynik)) {
            throw new Error("Assertion error line 14: assert silnia(a) == wynik;");
        };
    };
    Main.test2 = function() {
        var a = -5;
        var wynik = 1;
        if (!(Main.silnia(a) === wynik)) {
            throw new Error("Assertion error line 20: assert silnia(a) == wynik;");
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
