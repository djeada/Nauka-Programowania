    wyczysc = function(napis) {
        napis = napis.trim();
        return napis.replace(/[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, "");
    };
    najdluzsze = function(napis) {
        var wynik = null;
        var dlugosc = 0;
        var pocz = 0;
        var konc = 0;
        while (((konc = napis.indexOf(' ', pocz)) !== -1)) {
            {
                if (konc !== pocz) {
                    var slowo = napis.substring(pocz, konc);
                    slowo = wyczysc(slowo);
                    if (slowo.length > dlugosc) {
                        wynik = slowo;
                        dlugosc = slowo.length;
                    }
                }
                pocz = konc + 1;
            }
        };
        if (konc !== pocz) {
            var slowo = napis.substring(pocz);
            slowo = wyczysc(slowo);
            if (slowo.length > dlugosc) {
                wynik = slowo;
                dlugosc = slowo.length;
            }
        }
        return wynik;
    };
    najkrotsze = function(napis) {
        var wynik = null;
        var dlugosc = napis.length;
        var pocz = 0;
        var konc = 0;
        while (((konc = napis.indexOf(' ', pocz)) !== -1)) {
            {
                if (konc !== pocz) {
                    var slowo = napis.substring(pocz, konc);
                    slowo = wyczysc(slowo);
                    if (slowo.length < dlugosc) {
                        wynik = slowo;
                        dlugosc = slowo.length;
                    }
                }
                pocz = konc + 1;
            }
        };
        if (konc !== pocz) {
            var slowo = napis.substring(pocz);
            slowo = wyczysc(slowo);
            if (slowo.length < dlugosc) {
                wynik = slowo;
                dlugosc = slowo.length;
            }
        }
        return wynik;
    };
    test1 = function() {
        var napis = "Kaczka lubi wiosne.";
        var oczekiwane = "Kaczka";
        var wynik = najdluzsze(napis);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    test2 = function() {
        var napis = "Kaczka lubi wiosne.";
        var oczekiwane = "lubi";
        var wynik = najkrotsze(napis);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 30: ${wynik} === ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
        test2();
    };

    main(null);