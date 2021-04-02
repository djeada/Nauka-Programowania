var Main = (function() {
    function Main() {}
    Main.wczytaj = function(lista, n) {
        console.info("podaj " + n + " liczb:");
        var rl = require('readline-sync');
        for (var i = 0; i < n; i++) {
            {
                var liczba = rl.question('');
                (lista.push(liczba) > 0);
            };
        }
    };
    Main.wypiszOdPoczatku = function(lista) {
        for (var i = 0; i < lista.length; i++) {

            console.info(lista[i]);

        }
    };
    Main.wypiszOdKonca = function(lista) {
        for (var i = lista.length - 1; i >= 0; i--) {
            {
                process.stdout.write(lista[i] + ", ");

            };
        }
        console.info("\n");
    };
    Main.main = function(args) {
        var lista = ([]);
        var n = require('readline-sync').question('podaj liczbe:');
        Main.wczytaj(lista, n);
        Main.wypiszOdPoczatku(lista);
        Main.wypiszOdKonca(lista);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
