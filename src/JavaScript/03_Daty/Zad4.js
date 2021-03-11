var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var dzien = require('readline-sync').question('Podaj dzien:');
        switch ((dzien)) {
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
                console.info("podano niepoprawna liczbe");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
