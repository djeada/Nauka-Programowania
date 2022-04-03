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
        var oczekiwne = 6;
        var wynik = Main.mnozenie(a, b);
        if (!(oczekiwne === wynik)) {
            throw new Error(`Assertion error line 28: oczekiwane: ${oczekiwne}, obliczone: ${wynik}`);
        };
    };
    Main.test2 = function() {
        var a = 30;
        var b = 6;
        var wynik = 5;
        var oczekiwne = Main.dzielenie(a, b);
        if (!(oczekiwne === wynik)) {
            throw new Error(`Assertion error line 37: oczekiwane: ${oczekiwne}, obliczone: ${wynik}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
