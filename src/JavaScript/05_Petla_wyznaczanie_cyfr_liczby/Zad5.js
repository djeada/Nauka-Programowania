var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var a = require('readline-sync').question('podaj liczbe:');
        var odwrocona = 0;
        var pom = a;
        while ((pom > 0)) {
            {
                var cyfra = pom % 10;
                odwrocona = (odwrocona * 10 + cyfra);
                pom = (function(n) {
                    return n < 0 ? Math.ceil(n) : Math.floor(n);
                })(pom / 10);
            }
        };
        if (odwrocona === a) {
            console.info("podana liczba jest palindromem");
            console.info("\n");
        } else {
            console.info("podana liczba nie jest palindromem");
            console.info("\n");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
