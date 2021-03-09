var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {

        var a = require('readline-sync').question('podaj liczbe:');

        if (a < 0) {
            console.info("liczba jest ujemna");
        } else if (a > 0) {
            console.info("liczba jest dodatnia");
        } else {
            console.info("liczba jest zerem");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
