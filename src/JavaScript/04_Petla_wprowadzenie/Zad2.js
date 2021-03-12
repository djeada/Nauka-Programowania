var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var a = require('readline-sync').question('podaj liczbe:');
        for (var i = 1; i < a; i++) {
            {
                console.info(i);
                console.info(" ");
            };
        }
        console.info("\n");
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
