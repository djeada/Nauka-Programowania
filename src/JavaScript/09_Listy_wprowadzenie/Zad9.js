var Main = /** @class */ (function() {
    function Main() {}
    Main.usunDuplikatyV1 = function(lista) {
        var wynik = ([]);
        for (var i = 0; i < lista.length; i++) {
            var x = lista[i];
            if (!(wynik.indexOf((x)) >= 0))
                (wynik.push(x) > 0);
        }
        return wynik;
    };
    Main.usunDuplikatyV2 = function(lista) {
        var wynik = ([]);
        var zbior = ([]);
        for (var i = 0; i < lista.length; i++) {
            var x = lista[i];
            if ((function(s, e) {
                    if (s.indexOf(e) == -1) {
                        s.push(e);
                        return true;
                    } else {
                        return false;
                    }
                })(zbior, x))
                (wynik.push(x) > 0);
        }
        return wynik;
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
    Main.main = function(args) {
        var lista = ([2, 1, 2, 2, 3, 3].slice(0));
        var wynik = ([2, 1, 3].slice(0));

        if (!Main.listyRowne(Main.usunDuplikatyV1(lista), wynik)) {
            throw new Error("Assertion error;");
        };

    };
    Main.main = function(args) {
        var lista = ([2, 1, 2, 2, 3, 3].slice(0));
        var wynik = ([2, 1, 3].slice(0));

        if (!Main.listyRowne(Main.usunDuplikatyV2(lista), wynik)) {
            throw new Error("Assertion error;");
        };

    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
