    zamienV1 = function(napis) {
        if (napis.length === 0) {
            return "";
        }
        var wynik = ""; {
            var tablica = (napis).split('');
            for (var i = 0; i < tablica.length; i++) {
                var numer = tablica[i]; {
                    wynik += numer.charCodeAt(0) + ", ";
                }
            }
        }
        return wynik.substring(0, wynik.length - 2);
    };
    test1 = function() {
        var napis = "pacZka!";
        var oczekiwane = "112, 97, 99, 90, 107, 97, 33";
        var wynik = zamienV1(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    test2 = function() {
        var napis = "";
        var oczekiwane = "";
        var wynik = zamienV1(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
        test2();
    };

    main(null);