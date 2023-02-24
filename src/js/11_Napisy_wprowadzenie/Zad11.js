    wyczysc = function(napis) {
        napis = napis.trim();
        return napis.replace(/[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, "");
    };
    srednia = function(napis) {
        var calk_dlugosc = 0;
        var n = 0;
        var pocz = 0;
        var konc = 0;
        while (((konc = napis.indexOf(' ', pocz)) !== -1)) {
            {
                if (konc !== pocz) {
                    var slowo = napis.substring(pocz, konc);
                    slowo = wyczysc(slowo);
                    if (!(slowo.length === 0)) {
                        n++;
                        calk_dlugosc += slowo.length;
                    }
                }
                pocz = konc + 1;
            }
        };
        if (konc !== pocz) {
            var slowo = napis.substring(pocz);
            slowo = wyczysc(slowo);
            if (!(slowo.length === 0)) {
                n++;
                calk_dlugosc += slowo.length;
            }
        }
        return (calk_dlugosc / n | 0);
    };
    test1 = function() {
        var napis = "Kaczka lubi wiosne.";
        var oczekiwane = 5;
        var wynik = srednia(napis);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    test2 = function() {
        var napis = "Kaczka lubi wiosne.";
        var oczekiwane = 5;
        var wynik = srednia(napis);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
        test2();
    };

    main(null);