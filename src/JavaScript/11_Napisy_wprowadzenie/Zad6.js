var Main = (function() {
    function Main() {}
    Main.zamienV1 = function(napis) {
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
    Main.zamienV2 = function(napis) {
        return napis.replace(new RegExp("a", 'g'), "?");
    };
    Main.test1 = function() {
        var napis = "pacZka!";
        var wynik = "p?cZk?!";
        if (!(Main.zamienV1(napis) === wynik)) {
            throw new Error("Assertion error line 27: assert zamienV1(napis).equals(wynik);");
        };
    };
    Main.test2 = function() {
        var napis = "pacZka!";
        var wynik = "p?cZk?!";
        if (!(Main.zamienV2(napis) === wynik)) {
            throw new Error("Assertion error line 33: assert zamienV2(napis).equals(wynik);");
        };
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
