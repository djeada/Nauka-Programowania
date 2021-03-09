var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var rl = require('readline-sync');
        var x = rl.question('podaj liczbe:');
        if (x > 5) {
            console.info(x);
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
