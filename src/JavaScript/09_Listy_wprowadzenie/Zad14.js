var Main = /** @class */ (function() {
    function Main() {}
    Main.elementBezParyV1 = function(lista) {
        var pom = ([]);
        var _loop_1 = function(i) {
            var liczba = lista[i]; {
                if ((pom.indexOf((liczba)) >= 0)) {

                    (function(a) {
                        var index = a.indexOf(liczba);
                        if (index >= 0) {
                            a.splice(index, 1);
                            return true;
                        } else {
                            return false;
                        }
                    })(pom);
                } else {

                    (pom.push(liczba) > 0);
                }
            }
        };
        for (var i = 0; i < lista.length; i++) {
            _loop_1(i);
        }
        return pom[0];
    };
    Main.elementBezParyV2 = function(lista) {
        var wynik = 0;
        for (var i = 0; i < lista.length; i++) {
            var liczba = lista[i]; {
                wynik ^= liczba;
            }
        }
        return wynik;
    };
    Main.test1 = function() {
        var lista = ([1, 3, 1, 7, 3, 1, 1].slice(0));
        var wynik = 7;
        if (!(Main.elementBezParyV1(lista) === wynik)) {
            throw new Error("Assertion error line 31: assert elementBezParyV1(lista) == wynik;");
        };
    };
    Main.test2 = function() {
        var lista = ([1, 3, 1, 7, 3, 1, 1].slice(0));
        var wynik = 7;
        if (!(Main.elementBezParyV2(lista) === wynik)) {
            throw new Error("Assertion error line 37: assert elementBezParyV2(lista) == wynik;");
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
