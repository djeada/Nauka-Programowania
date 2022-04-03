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

    Main.test1 = function() {
        var lista = [6, 7, 2, 1, 8]
        var klucz = 2;
        var oczekiwane = [6, 7, 1, 8]
        var wynik = Main.usunWszystkieWystapieniaV1(lista, klucz);
        if (oczekiwane.length !== wynik.length) {
            throw new Error(`Assertion error line 37: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
        }
        for (var i = 0; i < oczekiwane.length; i++) {
            if (oczekiwane[i] !== wynik[i]) {
                throw new Error(`Assertion error line 40: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
            }
        }
    };
    Main.test2 = function() {
        var lista = [6, 7, 2, 1, 8]
        var klucz = 2;
        var oczekiwane = [6, 7, 1, 8]
        var wynik = Main.usunWszystkieWystapieniaV2(lista, klucz);
        if (oczekiwane.length !== wynik.length) {
            throw new Error(`Assertion error line 50: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
        }
        for (var i = 0; i < oczekiwane.length; i++) {
            if (oczekiwane[i] !== wynik[i]) {
                throw new Error(`Assertion error line 54: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
            }
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
