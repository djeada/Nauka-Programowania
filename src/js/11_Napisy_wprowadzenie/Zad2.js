    policzZnakV1 = function(slowo, znak) {
        var licznik = 0; {
            var tablica = (slowo).split('');
            for (var i = 0; i < tablica.length; i++) {
                var x = tablica[i]; {
                    if ((function(c) {
                            return c.charCodeAt == null ? c : c.charCodeAt(0);
                        })(x) == (function(c) {
                            return c.charCodeAt == null ? c : c.charCodeAt(0);
                        })(znak)) {
                        licznik++;
                    }
                }
            }
        }
        return licznik;
    };
    test1 = function() {
        var napis = "adam";
        var znak = 'a';
        var oczekiwane = 2;
        var wynik = policzZnakV1(napis, znak);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
    };

    main(null);