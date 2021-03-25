var Main = /** @class */ (function() {
    function Main() {}
    Main.czyWieksza = function(a, b) {
        return a > b;
    };
    Main.czySumaMniejsza = function(a, b) {
        var suma = a + b;
        return suma < 10;
    };
    Main.czyObieNieparzyste = function(a, b) {
        return a % 2 === 1 && b % 2 === 1;
    };
    Main.wieksza = function(a, b) {
        return a > b ? a : b;
    };
    Main.czyWiekszaNizKwad = function(a, b) {
        return Main.wieksza(a, b) < Math.pow(a, 2);
    };
    Main.main = function(args) {
        console.info("Podaj dwie liczby: ");
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');
        console.info("Pierwsza liczba jest wieksza od drugiej: ");
        console.info(czyWieksza(a, b));
        console.info("\n");
        console.info("Suma liczb jest mniejsza od 10: ");
        console.info(czySumaMniejsza(a, b));
        console.info("\n");
        console.info("Obie liczby nieparzyste: ");
        console.info(czyObieNieparzyste(a, b));
        console.info("\n");
        console.info("Wieksza liczba jest mniejsza od pierwszej podniesionej do kwadratu ");
        console.info(czyWiekszaNizKwad(a, b));
        console.info("\n");
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
