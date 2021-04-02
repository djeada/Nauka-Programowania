var Main = /** @class */ (function() {
    function Main() {}
    Main.policzSamochodyV1 = function(lista) {
        var licznik = 0;
        for (var i = 0; i < lista.length; i++) {
            {
                if ((function(c) {
                        return c.charCodeAt == null ? c : c.charCodeAt(0);
                    })(lista[i]) == 'A'.charCodeAt(0)) {
                    for (var j = i + 1; j < lista.length; j++) {
                        {
                            if ((function(c) {
                                    return c.charCodeAt == null ? c : c.charCodeAt(0);
                                })(lista[j]) == 'B'.charCodeAt(0)) {
                                licznik++;
                            }
                        };
                    }
                } else if ((function(c) {
                        return c.charCodeAt == null ? c : c.charCodeAt(0);
                    })(lista[i]) == 'B'.charCodeAt(0)) {
                    for (var j = i - 1; j > -1; j--) {
                        {
                            if ((function(c) {
                                    return c.charCodeAt == null ? c : c.charCodeAt(0);
                                })(lista[j]) == 'A'.charCodeAt(0)) {
                                licznik++;
                            }
                        };
                    }
                }
            };
        }
        return (licznik / 2 | 0);
    };
    Main.policzSamochodyV2 = function(lista) {
        var licznik = 0;
        var pom = 0;
        for (var index8217 = 0; index8217 < lista.length; index8217++) {
            var x = lista[index8217]; {
                if ((function(c) {
                        return c.charCodeAt == null ? c : c.charCodeAt(0);
                    })(x) == 'A'.charCodeAt(0)) {
                    pom++;
                } else if ((function(c) {
                        return c.charCodeAt == null ? c : c.charCodeAt(0);
                    })(x) == 'B'.charCodeAt(0)) {
                    licznik += pom;
                }
            }
        }
        return licznik;
    };
    Main.test1 = function() {
        var lista = (['A', 'B', 'A', 'B', 'B'].slice(0));
        var wynik = 5;
        if (!(Main.policzSamochodyV1(lista) === wynik)) {
            throw new Error("Assertion error line 41: assert policzSamochodyV1(lista) == wynik;");
        };
        if (!(Main.policzSamochodyV2(lista) === wynik)) {
            throw new Error("Assertion error line 42: assert policzSamochodyV2(lista) == wynik;");
        };
    };
    Main.test2 = function() {
        var lista = (['A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A'].slice(0));
        var wynik = 15;
        if (!(Main.policzSamochodyV1(lista) === wynik)) {
            throw new Error("Assertion error line 48: assert policzSamochodyV1(lista) == wynik;");
        };
        if (!(Main.policzSamochodyV2(lista) === wynik)) {
            throw new Error("Assertion error line 49: assert policzSamochodyV2(lista) == wynik;");
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
