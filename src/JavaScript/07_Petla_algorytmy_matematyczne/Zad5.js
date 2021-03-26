var Main = /** @class */ (function() {
    function Main() {}
    Main.nwdV1 = function(a, b) {
        if (b === 0) {
            return a;
        }
        return Main.nwdV1(b, a % b);
    };
    Main.nwdV2 = function(a, b) {
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
    Main.test1 = function() {
        var a = 14;
        var b = 21;
        var wynik = 7;
        if (!(Main.nwdV1(a, b) === wynik)) {
            throw new Error("Assertion error line 26: assert nwdV1(a, b) == wynik;");
        };
    };
    Main.test2 = function() {
        var a = 14;
        var b = 21;
        var wynik = 7;
        if (!(Main.nwdV2(a, b) === wynik)) {
            throw new Error("Assertion error line 33: assert nwdV2(a, b) == wynik;");
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
