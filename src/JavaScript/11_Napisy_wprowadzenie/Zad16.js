var Main = (function() {
    function Main() {}
    Main.odlegloscHammingaV1 = function(napisA, napisB) {
        if (napisA.length !== napisB.length) {
            return -1;
        }
        var wynik = 0;
        for (var i = 0; i < napisA.length; i++) {
            {
                if ((function(c) {
                        return c.charCodeAt == null ? c : c.charCodeAt(0);
                    })(napisA.charAt(i)) != (function(c) {
                        return c.charCodeAt == null ? c : c.charCodeAt(0);
                    })(napisB.charAt(i))) {
                    wynik++;
                }
            };
        }
        return wynik;
    };
    Main.test1 = function() {
        var napisA = "xxbab";
        var napisB = "bbabb";
        var wynik = 4;
        if (!(Main.odlegloscHammingaV1(napisA, napisB) === wynik)) {
            throw new Error("Assertion error line 19: assert odlegloscHammingaV1(napisA, napisB) == wynik;");
        };
    };
    Main.test2 = function() {
        var napisA = "xxbab";
        var napisB = "bbabb";
        var wynik = 4;
        if (!(Main.odlegloscHammingaV1(napisA, napisB) === wynik)) {
            throw new Error("Assertion error line 26: assert odlegloscHammingaV1(napisA, napisB) == wynik;");
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
