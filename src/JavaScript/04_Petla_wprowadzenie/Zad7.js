var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var n = require('readline-sync').question('podaj liczbe:');
        var wynik = 1.0;
        for (var i = 0; i < n; i++) {
            {
                wynik *= 3.14;
            };
        }
        console.info(wynik);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
