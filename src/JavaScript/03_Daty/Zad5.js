var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var numer = require('readline-sync').question('Podaj numer miesiaca:');
        switch ((numer)) {
            case 1:
                console.info("Styczen ma 31 dni");
                break;
            case 2:
                console.info("Luty ma 28 lub 29 dni");
                break;
            case 3:
                console.info("Marzec ma 31 dni");
                break;
            case 4:
                console.info("Kwiecien ma 30 dni");
                break;
            case 5:
                console.info("Maj ma 31 dni");
                break;
            case 6:
                console.info("Czerwiec ma 30 dni");
                break;
            case 7:
                console.info("Lipiec ma 31 dni");
                break;
            case 8:
                console.info("Sierpien ma 31 dni");
                break;
            case 9:
                console.info("Wrzesien ma 30 dni");
                break;
            case 10:
                console.info("Pazdziernik ma 31 dni");
                break;
            case 11:
                console.info("Listopad ma 30 dni");
                break;
            case 12:
                console.info("Grudzien ma 31 dni");
                break;
            default:
                console.info("Podano niepoprawny numer miesiaca");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
