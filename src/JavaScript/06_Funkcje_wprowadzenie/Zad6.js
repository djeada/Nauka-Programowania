var Main = /** @class */ (function() {
    function Main() {}
    Main.sumaCyfr = function(a) {
        var suma = 0;
        while ((a > 0)) {
            {
                suma += (a % 10);
                a = (function(n) {
                    return n < 0 ? Math.ceil(n) : Math.floor(n);
                })(a / 10);
            }
        };
        return suma;
    };
    Main.main = function(args) {
        var a = require('readline-sync').question('podaj liczbe:');
        console.info("Suma cyfr liczby to: ");
        console.info(Main.sumaCyfr(a));
        console.info("\n");
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
