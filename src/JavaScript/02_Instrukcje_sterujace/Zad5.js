var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        console.info("podaj trzy liczby:");
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');
        var c = rl.question('');
        if (a >= b && a >= c) {
            if (b >= c) {
                console.info(c);
                console.info(b);
                console.info(a);
            } else {
                console.info(b);
                console.info(c);
                console.info(a);
            }
        } else if (c >= b && c >= a) {
            if (a >= b) {
                console.info(b);
                console.info(a);
                console.info(c);
            } else {
                console.info(a);
                console.info(b);
                console.info(c);
            }
        } else {
            if (a >= c) {
                console.info(c);
                console.info(a);
                console.info(b);
            } else {
                console.info(a);
                console.info(c);
                console.info(b);
            }
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
