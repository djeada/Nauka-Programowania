var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var rl = require('readline-sync');
        var a = rl.question('podaj liczbe:');
        if (a >= 1 && a <= 7) {
            console.info("Liczba jest poprawnym numerem tygodnia");
            console.info("\n");
        } else {
            console.info("Liczba nie jest poprawnym numerem tygodnia");
            console.info("\n");
        }
        if (a >= 1 && a <= 12) {
            console.info("Liczba jest poprawnym numerem miesiaca");
            console.info("\n");
        } else {
            console.info("Liczba nie jest poprawnym numerem miesiaca");
            console.info("\n");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
