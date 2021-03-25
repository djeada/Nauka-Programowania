var Main = /** @class */ (function() {
    function Main() {}
    Main.podziel = function(a, b) {
        var znak = 1;
        var licznik = 0;
        if (b === 0) {
            return Number.NaN;
        }
        if (a === 0) {
            return 0;
        }
        if (a < 0) {
            znak = -1;
            a = -a;
        }
        if (b < 0) {
            znak *= -1;
            b = -b;
        }
        if (znak === 1) {
            licznik = 0;
            while ((a >= b)) {
                {
                    a -= b;
                    licznik += 1;
                }
            };
        } else {
            licznik = 1;
            while ((a > b)) {
                {
                    a -= b;
                    licznik += 1;
                }
            };
        }
        return licznik * znak;
    };
    Main.main = function(args) {
        console.info("Podaj dwie liczby: ");
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');
        console.info("iloraz pierwszej przez druga to: ");
        console.info(Main.podziel(a, b));
        console.info("\n");
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
