var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var a = require('readline-sync').question('podaj liczbe:');
        a = 3;
        console.info("mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10: ");
        console.info("\n");
        for (var i = 0; i < a; i++) {
            {
                var pom_1 = i;
                var suma_1 = 0;
                while ((pom_1 > 0)) {
                    {
                        suma_1 += (pom_1 % 10);
                        pom_1 = (function(n) {
                            return n < 0 ? Math.ceil(n) : Math.floor(n);
                        })(pom_1 / 10);
                    }
                };
                if (suma_1 === 10) {
                    console.info(i);
                    console.info("\n");
                }
            };
        }
        console.info("dwucyfrowe mniejsze od pobranej liczby: ");
        console.info("\n");
        for (var i = 10; i < 100 && i < a; i++) {
            {
                console.info(i);
                console.info("\n");
            };
        }
        console.info("trzycyfrowe ktorych suma cyfr jest rowna pobranej liczbie");
        console.info("\n");
        for (var i = 100; i < 1000; i++) {
            {
                var pom_2 = i;
                var suma_2 = 0;
                while ((pom_2 > 0)) {
                    {
                        suma_2 += (pom_2 % 10);
                        pom_2 = (function(n) {
                            return n < 0 ? Math.ceil(n) : Math.floor(n);
                        })(pom_2 / 10);
                    }
                };
                if (suma_2 === a) {
                    console.info(i);
                    console.info("\n");
                }
            };
        }
        console.info("trzycyfrowe podzielne przez sume cyfr pobranej liczby");
        console.info("\n");
        var pom = a;
        var suma = 0;
        while ((pom > 0)) {
            {
                suma += (pom % 10);
                pom = (function(n) {
                    return n < 0 ? Math.ceil(n) : Math.floor(n);
                })(pom / 10);
            }
        };
        for (var i = 100; i < 1000; i++) {
            {
                if (i % suma === 0) {
                    console.info(i);
                    console.info("\n");
                }
            };
        }
        console.info("mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr");
        console.info("\n");
        for (var i = 0; i < a; i++) {
            {
                pom = i;
                var flaga = true;
                while ((pom > 0)) {
                    {
                        var cyfra = pom % 10;
                        if (cyfra % 2 === 1) {
                            flaga = false;
                            break;
                        }
                        pom = (function(n) {
                            return n < 0 ? Math.ceil(n) : Math.floor(n);
                        })(pom / 10);
                    }
                };
                if (flaga) {
                    console.info(i);
                    console.info("\n");
                }
            };
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
