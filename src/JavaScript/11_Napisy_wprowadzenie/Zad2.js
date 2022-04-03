var Main = (function() {
    function Main() {}
    Main.policzZnakV1 = function(slowo, znak) {
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
    Main.test1 = function() {
        var napis = "adam";
        var znak = 'a';
        var oczekiwane = 2;
        var wynik = Main.policzZnakV1(napis, znak);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
