    czyPierwsza = function(n) {
        if ((n % 2) === 0 && n !== 2) {
            return false;
        }
        for (var i = 3; i <= Math.sqrt(n); i += 2) {
            {
                if ((n % i) === 0) {
                    return false;
                }
            };
        }
        return true;
    };
    znaki = function(napis) {
        var znaki = ([]);
        for (var i = 0; i < napis.length; i++) {
            {
                if (czyPierwsza(i)) {
                    (znaki.push(napis.charAt(i)) > 0);
                }
            };
        }
        return (znaki.slice(0));
    };
    listyRowne = function(a1, a2) {
        if (a1 == null && a2 == null)
            return true;
        if (a1 == null || a2 == null)
            return false;
        if (a1.length != a2.length)
            return false;
        for (var i = 0; i < a1.length; i++) {
            if (a1[i] != a2[i])
                return false;
        }
        return true;
    };
    test1 = function() {
        var napis = "Kaczka lubi wiosne.";
        var wynik = (['a', 'c', 'z', 'a', 'l', ' ', 'i', 'e'].slice(0));
        if (!listyRowne(wynik, znaki(napis))) {
            throw new Error("Assertion error;");
        };
    };
    main = function(args) {
        test1();
    };

    main(null);