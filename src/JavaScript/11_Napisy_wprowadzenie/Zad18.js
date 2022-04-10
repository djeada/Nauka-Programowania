    odwroc = function(slowo) {
        var rozdziel = slowo.split("");
        var odwroc = rozdziel.reverse();
        return odwroc.join("");
    };
    odwrocNapisyV1 = function(napis) {
        var slowa = napis.split(" ");
        for (var i = 0; i < slowa.length; i++) {
            slowa[i] = odwroc(slowa[i]);
        }
        return slowa.join(" ").trim();
    };
    test1 = function() {
        var napis = "Cameron Diaz";
        var oczekiwane = "noremaC zaiD";
        var wynik = odwrocNapisyV1(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
    };

    main(null);