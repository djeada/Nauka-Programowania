var Main = /** @class */ (function() {
    function Main() {}
    Main.czyPierwsza = function(n) {
        if (n <= 1) {
            return false;
        }
        if (n % 2 === 0 && n !== 2) {
            return false;
        }
        for (var i = 3; i <= Math.sqrt(n); i += 2) {
            {
                if (n % i === 0) {
                    return false;
                }
            };
        }
        return true;
    };
    Main.test1 = function() {
        var a = 15;
        if (!(!Main.czyPierwsza(a))) {
            throw new Error("Assertion error line 19: assert !czyPierwsza(a);");
        };
    };
    Main.test2 = function() {
        var a = 7;
        if (!(Main.czyPierwsza(a))) {
            throw new Error("Assertion error line 24: assert czyPierwsza(a);");
        };
    };
    Main.test3 = function() {
        var a = -15;
        if (!(!Main.czyPierwsza(a))) {
            throw new Error("Assertion error line 29: assert !czyPierwsza(a);");
        };
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
        Main.test3();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
