var Main = /** @class */ (function() {
    function Main() {}
    Main.potega = function(a, b) {
        var wynik = 1;
        for (var i = 0; i < Math.abs(b); i++) {
            {
                wynik *= a;
            };
        }
        if (b < 0) {
            return (1 / wynik | 0);
        }
        return wynik;
    };
    Main.test1 = function() {
        var a = 2;
        var b = 3;
        var wynik = 8.0;
        if (!(Math.abs(Main.potega(a, b) - wynik) < 0.01)) {
            throw new Error("Assertion error line 17: assert Math.abs(potega(a, b) - wynik) < 0.01;");
        };
    };
    Main.test2 = function() {
        var a = 10;
        var b = -5;
        var wynik = 1.0E-5;
        if (!(Math.abs(Main.potega(a, b) - wynik) < 0.01)) {
            throw new Error("Assertion error line 24: assert Math.abs(potega(a, b) - wynik) < 0.01;");
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
