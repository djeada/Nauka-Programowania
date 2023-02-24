    policzSlowaV1 = function(slowo) {
        var spacja = true;
        var licznik = 0;
        for (const znak of slowo) {
            if (znak === " ") {
                spacja = true;
            } else if (znak.toLowerCase() != znak.toUpperCase() && spacja) {
                licznik += 1;
                spacja = false;
            }
        }
        return licznik;
    };
    test1 = function() {
        var napis = "Ile to   ma :  slow w swoim zdaniu na   koniec?";
        var oczekiwane = 9;
        var wynik = policzSlowaV1(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
    };

    main(null);