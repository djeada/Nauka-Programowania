    wczytaj = function(lista, n) {
        console.info("podaj " + n + " liczb:");
        var rl = require('readline-sync');
        for (var i = 0; i < n; i++) {
            {
                var liczba = rl.question('');
                (lista.push(liczba) > 0);
            };
        }
    };
    wypiszOdPoczatku = function(lista) {
        for (var i = 0; i < lista.length; i++) {
            console.info(lista[i]);
        }
    };
    wypiszOdKonca = function(lista) {
        for (var i = lista.length - 1; i >= 0; i--) {
            {
                process.stdout.write(lista[i] + ", ");
            };
        }
        console.info("\n");
    };
    main = function(args) {
        var lista = ([]);
        var n = require('readline-sync').question('podaj liczbe:');
        wczytaj(lista, n);
        wypiszOdPoczatku(lista);
        wypiszOdKonca(lista);
    };

    main(null);