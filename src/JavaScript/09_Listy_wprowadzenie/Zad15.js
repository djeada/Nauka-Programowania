var Main = /** @class */ (function() {
    function Main() {}
    Main.elementDominujacyV1 = function(lista) {
        var n = lista.length;
        for (var i = 0; i <= (n / 2); i++) {
            {
                var licznik = 1;
                for (var j = i + 1; j < n; j++) {
                    {
                        if (lista[j] === lista[i]) {
                            licznik++;
                        }
                    };
                }
                if (licznik > (n / 2)) {
                    return lista[i];
                }
            };
        }
        return -1;
    };
    Main.elementDominujacyV2 = function(lista) {
        var histo = ({});
        for (var i = 0; i < lista.length; i++) {
            var liczba = lista[i]; {
                if ((function(m, k) {
                        if (m.entries == null)
                            m.entries = [];
                        for (var i = 0; i < m.entries.length; i++)
                            if (m.entries[i].key == null && k == null || m.entries[i].key.equals != null && m.entries[i].key.equals(k) || m.entries[i].key === k) {
                                return true;
                            } return false;
                    })(histo, liczba))
                    (function(m, k, v) {
                        if (m.entries == null)
                            m.entries = [];
                        for (var i = 0; i < m.entries.length; i++)
                            if (m.entries[i].key == null && k == null || m.entries[i].key.equals != null && m.entries[i].key.equals(k) || m.entries[i].key === k) {
                                m.entries[i].value = v;
                                return;
                            } m.entries.push({
                            key: k,
                            value: v,
                            getKey: function() {
                                return this.key;
                            },
                            getValue: function() {
                                return this.value;
                            }
                        });
                    })(histo, liczba, (function(m, k) {
                        if (m.entries == null)
                            m.entries = [];
                        for (var i = 0; i < m.entries.length; i++)
                            if (m.entries[i].key == null && k == null || m.entries[i].key.equals != null && m.entries[i].key.equals(k) || m.entries[i].key === k) {
                                return m.entries[i].value;
                            } return null;
                    })(histo, liczba) + 1);
                else
                    (function(m, k, v) {
                        if (m.entries == null)
                            m.entries = [];
                        for (var i = 0; i < m.entries.length; i++)
                            if (m.entries[i].key == null && k == null || m.entries[i].key.equals != null && m.entries[i].key.equals(k) || m.entries[i].key === k) {
                                m.entries[i].value = v;
                                return;
                            } m.entries.push({
                            key: k,
                            value: v,
                            getKey: function() {
                                return this.key;
                            },
                            getValue: function() {
                                return this.value;
                            }
                        });
                    })(histo, liczba, 1);
            }
        } {
            var tablica = (function(m) {
                if (m.entries == null)
                    m.entries = [];
                return m.entries;
            })(histo);
            for (var i = 0; i < tablica.length; i++) {
                var para = tablica[i]; {
                    if (para.getValue() > (lista.length / 2)) {
                        return para.getKey();
                    }
                }
            }
        }
        return -1;
    };
    Main.test1 = function() {
        var lista = ([4, 7, 4, 4, 2].slice(0));
        var wynik = 4;
        if (!(Main.elementDominujacyV1(lista) === wynik)) {
            throw new Error("Assertion error line 43: assert elementDominujacyV1(lista) == wynik;");
        };
        if (!(Main.elementDominujacyV2(lista) === wynik)) {
            throw new Error("Assertion error line 44: assert elementDominujacyV2(lista) == wynik;");
        };
    };
    Main.test2 = function() {
        var lista = ([1, 2, 4, 5, 6].slice(0));
        var wynik = -1;
        if (!(Main.elementDominujacyV1(lista) === wynik)) {
            throw new Error("Assertion error line 50: assert elementDominujacyV1(lista) == wynik;");
        };
        if (!(Main.elementDominujacyV2(lista) === wynik)) {
            throw new Error("Assertion error line 51: assert elementDominujacyV2(lista) == wynik;");
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
