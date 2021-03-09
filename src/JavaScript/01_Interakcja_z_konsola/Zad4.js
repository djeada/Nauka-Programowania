var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var rl = require('readline-sync');
        var x = rl.question('Podaj dwie liczby:\n');
        var y = rl.question('');
        console.info("Suma " + x + " oraz " + y + " wynosi " + (eval(x) + eval(y)));
        console.info("Roznica " + x + " i " + y + " wynosi " + (x - y));
        console.info("Iloczyn " + x + " i " + y + " wynosi " + (x * y));
        console.info("Iloraz " + x + " przez " + y + " wynosi " + ((x / y | 0)));
        console.info("Reszta z dzielenia " + x + " przez " + y + " wynosi " + (x % y));
        console.info(x + " podniesione do " + y + " wynosi " + Math.pow(x, y));
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
