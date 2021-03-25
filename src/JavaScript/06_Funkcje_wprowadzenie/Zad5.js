var Main = /** @class */ (function() {
    function Main() {}
    Main.min2 = function(a, b) {
        return a < b ? a : b;
    };
    Main.maks2 = function(a, b) {
        return a > b ? a : b;
    };
    Main.min3 = function(a, b, c) {
        var minAB = a < b ? a : b;
        return minAB < c ? minAB : c;
    };
    Main.maks3 = function(a, b, c) {
        var maksAB = a > b ? a : b;
        return maksAB > c ? maksAB : c;
    };
    Main.main = function(args) {
        console.info("Podaj dwie liczby: ");
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');
        console.info("mniejsza liczba to: ");
        console.info(Main.min2(a, b));
        console.info("\n");
        console.info("wieksza liczba to: ");
        console.info(Main.maks2(a, b));
        console.info("\n");

        console.info("Podaj trzy liczby: ");
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');
        var c = rl.question('');
        console.info("najmniejsza liczba to: ");
        console.info(Main.min3(a, b, c));
        console.info("\n");
        console.info("najwieksza liczba to ");
        console.info(Main.maks3(a, b, c));
        console.info("\n");
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
