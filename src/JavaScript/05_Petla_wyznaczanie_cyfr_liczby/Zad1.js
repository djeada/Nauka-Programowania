var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var a = require('readline-sync').question('podaj liczbe:');
        var licznik = 0;
        while ((a > 0)) {
            {
                a = (a / 10 | 0);
                licznik++;
            }
        };
        console.info("Podana liczba sklada sie z " + licznik + " cyfr.\n");
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
