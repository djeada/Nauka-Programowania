var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        console.info("Podaj trzy liczby reprezentujace dzien, miesiac i rok urodzenia osoby:");
        var rl = require('readline-sync');
        var dzien = rl.question('');
        var miesiac = rl.question('');
        var rok = rl.question('');
        console.info("Podaj trzy liczby reprezentujace dzisiejsza date:");
        var dzienAktualny = rl.question('');
        var miesiacAktualny = rl.question('');
        var rokAktualny = rl.question('');
        var roznicaLata = rokAktualny - rok;
        var roznicaMiesiace = miesiacAktualny - miesiac;
        var roznicaDni = dzienAktualny - dzien;
        if (roznicaLata > 18) {
            console.info("osoba jest pelnoletnia");
        } else if (roznicaLata === 18) {
            if (roznicaMiesiace > 0) {
                console.info("osoba jest pelnoletnia");
            } else if (roznicaMiesiace === 0) {
                if (roznicaDni >= 0) {
                    console.info("osoba jest pelnoletnia");
                } else {
                    console.info("osoba nie jest pelnoletnia");
                }
            } else {
                console.info("osoba nie jest pelnoletnia");
            }
        } else {
            console.info("osoba nie jest pelnoletnia");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
