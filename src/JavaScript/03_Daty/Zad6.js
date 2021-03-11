var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        console.info("Podaj dzien, miesiac i rok:");
        var rl = require('readline-sync');
        console.info(" ");
        var dzien = rl.question('');
        var miesiac = rl.question('');
        var rok = rl.question('');
        if (rok >= 1) {
            if (miesiac === 1 || miesiac === 3 || miesiac === 5 || miesiac === 7 || miesiac === 8 || miesiac === 10 || miesiac === 12) {
                if (dzien >= 1 && dzien <= 31) {
                    console.info("Podana data jest poprawna");
                } else {
                    console.info("Podano niepoprawna date");
                }
            } else if (miesiac === 4 || miesiac === 6 || miesiac === 9 || miesiac === 11) {
                if (dzien >= 1 && dzien <= 30) {
                    console.info("Podana data jest poprawna");
                } else {
                    console.info("Podano niepoprawna date");
                }
            } else if (miesiac === 2) {
                if (rok % 4 === 0) {
                    if (rok % 100 === 0) {
                        if (rok % 400 === 0 && dzien >= 1 && dzien <= 29) {
                            console.info("Podana data jest poprawna");
                        } else if (dzien >= 1 && dzien <= 28) {
                            console.info("Podana data jest poprawna");
                        } else {
                            console.info("Podano niepoprawna date");
                        }
                    } else if (dzien >= 1 && dzien <= 29) {
                        console.info("Podana data jest poprawna");
                    } else {
                        console.info("Podano niepoprawna date");
                    }
                } else if (dzien >= 1 && dzien <= 28) {
                    console.info("Podana data jest poprawna");
                }
            } else {
                console.info("Podano niepoprawna date");
            }
        } else {
            console.info("Podano niepoprawna date");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
