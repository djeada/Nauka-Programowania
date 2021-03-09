var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        console.info("podaj x");

        var rl = require('readline-sync');
        var x = rl.question('');
        console.info("3*x+10");

        console.info(3 * x + 10);

        console.info("podaj a");
        var a = rl.question('');

        console.info("podaj b");
        var b = rl.question('');

        console.info("podaj x");
        var x = rl.question('');

        console.info("a*x+b");

        console.info(a * x + b);

        console.info("podaj x");
        var x = rl.question('');

        console.info("y = x**3 + 2x**2 - 20");

        console.info(Math.pow(x, 3) + 2 * Math.pow(x, 2) - 20);

        console.info("podaj a");
        var a = rl.question('');

        console.info("podaj b");
        var b = rl.question('');

        console.info("podaj c");
        var c = rl.question('');

        console.info("podaj d");
        var d = rl.question('');

        console.info("podaj m");
        var m = rl.question('');

        console.info("podaj n");
        var n = rl.question('');

        console.info("podaj x");
        var x = rl.question('');

        console.info("a*x**m + b*x**n + c - a");

        console.info(a * Math.pow(x, m) + b * Math.pow(x, n) + c - a);

        console.info("podaj x");
        var x = rl.question('');

        console.info("sin(3*x)*cos(2*X) + e**x**2 + log(x**3 + 2*x**2 - x - 3)");

        console.info(Math.sin(3 * x) * Math.cos(2 * x) + Math.exp(Math.pow(x, 2)) + Math.log(Math.pow(x, 3) + 2 * Math.pow(x, 2) - x - 3));

    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
