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
    Main.zwieksz = function(lista) {
        for (var i = 0; i < lista.length; i++) {

            (lista[i] = eval(lista[i]) + 1);

        }
    };
    Main.pomnoz = function(lista) {
        for (var i = 0; i < lista.length; i++) {

            (lista[i] = lista[i] * i);

        }
    };
    Main.zastap = function(lista) {
        if ((lista.length == 0)) {
            return;
        }
        for (var i = 1; i < lista.length; i++) {
            {
                (lista[i] = lista[0]);
            };
        }
    };
    Main.wypisz = function(lista) {
        for (var i = 0; i < lista.length; i++) {
            process.stdout.write(lista[i] + ", ");
        }
        process.stdout.write("\n");
    };
    Main.main = function(args) {
        var lista = ([]);
        var n = require('readline-sync').question('podaj liczbe:');
        Main.wczytaj(lista, n);
        var kopia = (lista.slice(0));
        Main.zwieksz(kopia);
        Main.wypisz(kopia);
        kopia = (lista.slice(0));
        Main.pomnoz(kopia);
        Main.wypisz(kopia);
        kopia = (lista.slice(0));
        Main.zastap(kopia);
        Main.wypisz(kopia);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
