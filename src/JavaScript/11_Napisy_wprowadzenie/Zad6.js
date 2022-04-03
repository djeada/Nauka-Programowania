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
        var oczekiwane = "p?cZk?!";
        var wynik = Main.zamienV1(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.test2 = function() {
        var napis = "pacZka!";
        var oczekiwane = "p?cZk?!";
        var wynik = Main.zamienV2(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
