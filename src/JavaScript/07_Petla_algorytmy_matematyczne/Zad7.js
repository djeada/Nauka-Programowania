var Main = /** @class */ (function() {
    function Main() {}
    Main.nwd = function(a, b) {
        var c;
        while ((b !== a % b)) {
            {
                c = b;
                b = a % b;
                a = c;
                if (b === 0) {
                    break;
                }
            }
        };
        return a;
    };
    Main.nww = function(a, b) {
        return (a * b / Main.nwd(a, b) | 0);
    };
    Main.test1 = function() {
        var a = 14;
        var b = 21;
        var wynik = 42;
        if (!(Main.nww(a, b) === wynik)) {
            throw new Error("Assertion error line 23: assert nww(a, b) == wynik;");
        };
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
