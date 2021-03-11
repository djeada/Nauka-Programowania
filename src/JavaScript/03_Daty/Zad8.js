var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var rl = require('readline-sync');
        var DD = rl.question('Podaj dzien:\n');
        var MM = rl.question('Podaj miesiac:\n');
        var rok = rl.question('Podaj rok:\n');
        var CC = (rok / 100 | 0);
        var YY = rok % 100;
        var A = ((CC / 4 | 0)) - 2 * CC - 1;
        var B = (5 * YY / 4 | 0);
        var C = (26 * (MM + 1) / 10 | 0);
        var wynik = (A + B + C + DD) % 7;
        switch ((wynik)) {
            case 1:
                console.info("pierwszym dniem tygodnia jest poniedzialek");
                break;
            case 2:
                console.info("drugim dniem tygodnia jest wtorek");
                break;
            case 3:
                console.info("trzecim dniem tygodnia jest sroda");
                break;
            case 4:
                console.info("czwartym dniem tygodnia jest czwartek");
                break;
            case 5:
                console.info("piatym dniem tygodnia jest piatek");
                break;
            case 6:
                console.info("szostym dniem tygodnia jest sobota");
                break;
            case 7:
                console.info("siodmym dniem tygodnia jest niedziela");
                break;
            default:
                console.info("bledne dane");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
