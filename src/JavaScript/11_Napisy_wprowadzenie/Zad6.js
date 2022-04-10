    zamienV1 = function(napis) {
        var wynik = ""; {
            var tablica = (napis).split('');
            for (var i = 0; i < tablica.length; i++) {
                var znak = tablica[i]; {
                    if ((function(c) {
                            return c.charCodeAt == null ? c : c.charCodeAt(0);
                        })(znak) == 'a'.charCodeAt(0)) {
                        wynik += '?';
                    } else {
                        wynik += znak;
                    }
                }
            }
        }
        return wynik;
    };
    zamienV2 = function(napis) {
        return napis.replace(new RegExp("a", 'g'), "?");
    };
    test1 = function() {
        var napis = "pacZka!";
        var oczekiwane = "p?cZk?!";
        var wynik = zamienV1(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    test2 = function() {
        var napis = "pacZka!";
        var oczekiwane = "p?cZk?!";
        var wynik = zamienV2(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
        test2();
    };

    main(null);