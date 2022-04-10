    usunSpacjeV1 = function(zdanie) {
        return zdanie.replace(new RegExp("\\s", 'g'), "");
    };
    test1 = function(args) {
        var zdanie = "lezy jezy na wierzy";
        var oczekiwane = "lezyjezynawierzy";
        var wynik = usunSpacjeV1(zdanie);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    test2 = function(args) {
        zdanie = "d";
        oczekiwane = "d";
        wynik = usunSpacjeV1(zdanie);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
        test2();
    };

    main(null);