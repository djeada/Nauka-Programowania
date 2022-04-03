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
        var oczekiwane = false;
        var wynik = Main.czyPierwsza(a);
        if (wynik) {
            throw new Error(`Assertion error line 24: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.test2 = function() {
        var a = 7;
        var oczekiwane = true;
        var wynik = Main.czyPierwsza(a);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 32: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.test3 = function() {
        var a = -15;
        var oczekiwane = false; 
        var wynik = Main.czyPierwsza(a);
        if (wynik) {
            throw new Error(`Assertion error line 24: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
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
