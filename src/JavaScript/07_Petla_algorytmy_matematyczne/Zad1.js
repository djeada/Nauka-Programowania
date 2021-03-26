var Main = /** @class */ (function() {
    function Main() {}
    Main.srednia = function(n) {
        var suma = 0.0;
        var x;
        for (var i = 0; i < n; i++) {
            {
                var x = require('readline-sync').question('podaj liczbe:');
                suma += parseFloat(x);
            };
        }
        return suma / n;
    };
    Main.main = function(args) {
        var n = require('readline-sync').question('podaj liczbe n:');
        var wynik = Main.srednia(n);
        console.info("Srednia z podanych liczb to: ");
        console.info(wynik);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
