var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        console.info("podaj dwie liczby:");
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');
        if (a > b) {
            console.info(a);
            console.info(b);
            console.info("pierwsza liczba jest wieksza od drugiej\n");
        } else {
            console.info(b);
            console.info(a);
            console.info("pierwsza liczba nie jest wieksza od drugiej\n");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
