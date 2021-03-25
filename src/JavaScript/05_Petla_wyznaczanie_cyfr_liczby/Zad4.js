var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var a = require('readline-sync').question('podaj liczbe:');
        var pom = a;
        console.info("Cyfry liczby badace liczbami parzystymi: ");
        console.info("\n");
        while ((pom > 0)) {
            {
                var cyfra = pom % 10;
                if (cyfra % 2 === 0) {
                    console.info(cyfra);
                    console.info("\n");
                }
                pom = (function(n) {
                    return n < 0 ? Math.ceil(n) : Math.floor(n);
                })(pom / 10);
            }
        };
        pom = a;
        console.info("Cyfry liczby mniejsze niz 5: ");
        console.info("\n");
        while ((pom > 0)) {
            {
                var cyfra = pom % 10;
                if (cyfra < 5) {
                    console.info(cyfra);
                    console.info("\n");
                }
                pom = (function(n) {
                    return n < 0 ? Math.ceil(n) : Math.floor(n);
                })(pom / 10);
            }
        };
        pom = a;
        console.info("Cyfry liczby rozne od 0: ");
        console.info("\n");
        while ((pom > 0)) {
            {
                var cyfra = pom % 10;
                if (cyfra !== 0) {
                    console.info(cyfra);
                    console.info("\n");
                }
                pom = (function(n) {
                    return n < 0 ? Math.ceil(n) : Math.floor(n);
                })(pom / 10);
            }
        };
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
