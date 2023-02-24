    liczby = function(n) {
        var wynik = "";
        for (var i = 1; i <= n; i++) {
            {
                wynik += String(i).toString();
            };
        }
        return wynik;
    };
    test1 = function() {
        var n = 5;
        var oczekiwane = "12345";
        var wynik = liczby(n);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 24: ${wynik} != ${oczekiwane}`);
        }
    };
    test2 = function() {
        var n = -1;
        var oczekiwane = "";
        var wynik = liczby(n);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 24: ${wynik} != ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
        test2();
    };

    main(null);