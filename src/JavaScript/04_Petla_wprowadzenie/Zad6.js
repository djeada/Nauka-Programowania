var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var n = require('readline-sync').question('podaj liczbe:');
        var suma = 0.0;
        for (var i = 1.0; i <= n; i++) {
            {
                var a = i / (i + 1);
                suma += a;
            };
        }
        console.info(suma);
        suma = 0.0;
        for (var i = 1; i <= n; i++) {
            {
                var a = (Math.pow(i, 2) + 5) / i;
                suma += a;
            };
        }
        console.info(suma);
        suma = 0.0;
        for (var i = 1; i <= n; i++) {
            {
                var a = i + (Math.pow(2, i) | 0);
                suma += a;
            };
        }
        console.info(suma);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
