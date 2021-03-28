var Main = /** @class */ (function() {
    function Main() {}
    Main.czyPierwsza = function(n) {
        if (n % 2 === 0 && n !== 2) {
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
    Main.liczbyPierwszeV1 = function(n) {
        for (var i = 2; i <= n; i++) {
            {
                if (Main.czyPierwsza(i)) {
                    console.info(i);
                }
            };
        }
    };
    Main.sitoEratostenesa = function(pierwsze, liczba) {
        for (var p = 2; p <= liczba; p++) {
            {
                if (pierwsze[p] === -1) {
                    continue;
                }
                var n = 2;
                for (var i = p * n; i <= liczba; n++, i = p * n) {
                    {
                        pierwsze[i] = -1;
                    };
                }
            };
        }
    };
    Main.liczbyPierwszeV2 = function(liczba) {
        var pierwsze = (function(s) {
            var a = [];
            while (s-- > 0)
                a.push(0);
            return a;
        })(liczba + 1);
        Main.sitoEratostenesa(pierwsze, liczba);
        for (var i = 2; i <= liczba; i++) {
            {
                if (pierwsze[i] === 0) {
                    console.info(i);
                }
            };
        }
    };
    Main.main = function(args) {
        var a = 15;
        Main.liczbyPierwszeV1(a);
        Main.liczbyPierwszeV2(a);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);

