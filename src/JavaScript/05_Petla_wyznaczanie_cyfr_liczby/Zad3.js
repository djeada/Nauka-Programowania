var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var a = require('readline-sync').question('podaj liczbe:');
        var suma = 0;
        while ((a > 0)) {
            {
                suma += (a % 10);
                a = (a / 10 | 0);
            }
        };
        console.info("Suma cyfr podanej liczby wynosi " + suma + "\n");
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
