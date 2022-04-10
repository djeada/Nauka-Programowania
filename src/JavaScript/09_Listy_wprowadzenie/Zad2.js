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
    zwieksz = function(lista) {
        for (var i = 0; i < lista.length; i++) {
            (lista[i] = eval(lista[i]) + 1);
        }
    };
    pomnoz = function(lista) {
        for (var i = 0; i < lista.length; i++) {
            (lista[i] = lista[i] * i);
        }
    };
    zastap = function(lista) {
        if ((lista.length == 0)) {
            return;
        }
        for (var i = 1; i < lista.length; i++) {
            {
                (lista[i] = lista[0]);
            };
        }
    };
    wypisz = function(lista) {
        for (var i = 0; i < lista.length; i++) {
            process.stdout.write(lista[i] + ", ");
        }
        process.stdout.write("\n");
    };
    main = function(args) {
        var lista = ([]);
        var n = require('readline-sync').question('podaj liczbe:');
        wczytaj(lista, n);
        var kopia = (lista.slice(0));
        zwieksz(kopia);
        wypisz(kopia);
        kopia = (lista.slice(0));
        pomnoz(kopia);
        wypisz(kopia);
        kopia = (lista.slice(0));
        zastap(kopia);
        wypisz(kopia);
    };

    main(null);