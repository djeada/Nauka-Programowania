var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var n = require('readline-sync').question('podaj liczbe:');
        for (var i = 0; i < n; i++) {
            {
                console.info(Math.PI);
            };
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
