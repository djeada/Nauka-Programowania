    wypiszDane = function(napis) {
        var wynik = (napis.split(";").slice(0).slice(0));
        if (!(wynik.length === 5)) {
            throw new Error("Assertion error line 4: assert wynik.size() == 5;");
        };
        console.info("Imie: " + wynik[0]);
        console.info("Nazwisko: " + wynik[1]);
        console.info("Miejsce urodzenia: " + wynik[2]);
        console.info("Zawod: " + wynik[3]);
        console.info("Zarobki: " + wynik[4]);
    };
    main = function(args) {
        var napis = "Jan; Kowalski; Warszawa; Programista; 1000";
        wypiszDane(napis);
    };

    main(null);