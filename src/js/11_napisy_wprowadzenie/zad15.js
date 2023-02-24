    wyczysc = function(napis) {
        napis = napis.trim();
        return napis.replace(/[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, "");
    };
    slowaV1 = function(napis) {
        var wynik = ([]);
        var pocz = 0;
        var konc = 0;
        while (((konc = napis.indexOf(' ', pocz)) !== -1)) {
            {
                if (konc !== pocz) {
                    var slowo = napis.substring(pocz, konc);
                    slowo = wyczysc(slowo);
                    if (!(slowo.length === 0)) {
                        (wynik.push(slowo) > 0);
                    }
                }
                pocz = konc + 1;
            }
        };
        if (konc !== pocz) {
            var slowo = napis.substring(pocz);
            slowo = wyczysc(slowo);
            if (!(slowo.length === 0)) {
                (wynik.push(slowo) > 0);
            }
        }
        return (wynik.slice(0));
    };
    test1 = function() {
        var napis = "We think in generalities, but we live in details";
        var oczekiwane = (["We", "think", "in", "generalities", "but", "we", "live", "in", "details"].slice(0));
        var wynik = slowaV1(napis);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 31: ${wynik[i]} != ${oczekiwane[i]}`);
            }
        }
    };
    test2 = function() {
        var napis = "";
        var oczekiwane = ([]);
        var wynik = slowaV1(napis);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 39: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 41: ${wynik[i]} != ${oczekiwane[i]}`);
            }
        }
    };
    main = function(args) {
        test1();
        test2();
    };

    main(null);