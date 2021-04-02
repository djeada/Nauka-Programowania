var Main = /** @class */ (function() {
    function Main() {}
    Main.usunWszystkieWystapieniaV1 = function(lista, klucz) {
        for (var i = 0; i < lista.length; i++) {
            {
                if (lista[i] === klucz) {

                    lista.splice(i--, 1)[0];
                }
            };
        }
        return lista;
    };
    Main.usunWszystkieWystapieniaV2 = function(lista, klucz) {

        (function(a, r) {
            var b = false;
            for (var i = 0; i < r.length; i++) {
                var ndx = a.indexOf(r[i]);
                if (ndx >= 0) {
                    a.splice(ndx, 1);
                    b = true;
                }
            }
            return b;
        })(lista, [klucz]);
        return lista;
    };
    Main.listyRowne = function(a1, a2) {
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

    Main.test1 = function() {
        var lista = ([6, 7, 2, 1, 8].slice(0));
        var wynik = ([6, 7, 1, 8].slice(0));
        var klucz = 2;
        if (!Main.listyRowne(wynik, Main.usunWszystkieWystapieniaV1(lista, klucz))) {
            throw new Error("Assertion error;");
        };

    };
    Main.test2 = function() {
        var lista = ([6, 7, 2, 1, 8].slice(0));
        var wynik = ([6, 7, 1, 8].slice(0));
        var klucz = 2;
        if (!Main.listyRowne(wynik, Main.usunWszystkieWystapieniaV2(lista, klucz))) {
            throw new Error("Assertion error;");
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
