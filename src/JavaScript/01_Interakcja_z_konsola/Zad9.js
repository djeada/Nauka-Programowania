var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        console.info("Podaj: stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc udzielonego kredytu");
        var rl = require('readline-sync');
        var stopa = rl.question('');
        var lata = rl.question('');
        var kredyt = rl.question('');
        var r = stopa / 12 * 0.01;
        var n = lata * 12;
        var rata = (kredyt * r * Math.pow((1 + r), n) / (Math.pow((1 + r), n) - 1));
        var calkKoszt = rata * n;
        console.info("rata mieieczna to " + rata);
        console.info("calkowity koszt to " + calkKoszt);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
