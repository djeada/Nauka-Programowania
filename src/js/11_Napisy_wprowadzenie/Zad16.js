    odlegloscHammingaV1 = function(napisA, napisB) {
        if (napisA.length !== napisB.length) {
            return -1;
        }
        var wynik = 0;
        for (var i = 0; i < napisA.length; i++) {
            {
                if ((function(c) {
                        return c.charCodeAt == null ? c : c.charCodeAt(0);
                    })(napisA.charAt(i)) != (function(c) {
                        return c.charCodeAt == null ? c : c.charCodeAt(0);
                    })(napisB.charAt(i))) {
                    wynik++;
                }
            };
        }
        return wynik;
    };
    test1 = function() {
        var napisA = "xxbab";
        var napisB = "bbabb";
        var oczekiwane = 4;
        var wynik = odlegloscHammingaV1(napisA, napisB);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 29: ${wynik} === ${oczekiwane}`);
        }
    };
    test2 = function() {
        var napisA = "xxbab";
        var napisB = "bbabb";
        var oczekiwane = 4;
        var wynik = odlegloscHammingaV1(napisA, napisB);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 29: ${wynik} === ${oczekiwane}`);
        }
    };
    main = function(args) {
        test1();
        test2();
    };

    main(null);