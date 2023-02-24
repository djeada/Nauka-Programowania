    liczby = function(lista) {
        var wynik = "";
        for (var i = 0; i < lista.length; i++) {
            var liczba = lista[i]; {
                wynik += String(liczba).toString();
            }
        }
        return wynik;
    };
    test1 = function() {
        var lista = ([2, 4, 7].slice(0));
        var oczekiwane = "247";
        var wynik = liczby(lista);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 29: ${wynik} != ${oczekiwane}`);
        }
    };
    test2 = function() {
        var lista = ([]);
        var oczekiwane = "";
        var wynik = liczby(lista);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 29: ${wynik} != ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
        test2();
    };

    main(null);