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
        var oczekiwane = 24;
        var wynik = Main.silnia(a);
        if (!(oczekiwane === wynik)) {
            throw new Error(`Assertion error line 33: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.test2 = function() {
        var a = -5;
        var wynik = 1;
        var oczekiwane = Main.silnia(a);
        if (!(oczekiwane === wynik)) {
            throw new Error(`Assertion error line 33: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
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
