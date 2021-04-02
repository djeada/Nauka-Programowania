var Main = /** @class */ (function() {
    function Main() {}
    Main.rotacjaV1 = function(lista, kierunek, liczba) {
        if (kierunek === ("prawo")) {
            for (var i = 0; i < liczba; i++) {
                {

                    lista.splice(0, 0, lista[lista.length - 1]);

                    lista.splice(lista.length - 1, 1)[0];
                };
            }
        } else {
            for (var i = 0; i < liczba; i++) {
                {

                    (lista.push(lista[0]) > 0);

                    lista.splice(0, 1)[0];
                };
            }
        }
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
        var lista = ([5, 27, 6, 2, 1, 10, 8].slice(0));
        var wynik = ([6, 2, 1, 10, 8, 5, 27].slice(0));
        var kierunek = "lewo";
        var liczba = 2;
        if (!Main.listyRowne(Main.rotacjaV1(lista, kierunek, liczba), wynik)) {
            throw new Error("Assertion error;");
        };
    };
    Main.test2 = function() {
        var lista = ([9, 9, 42, 47, 5, 6, 19, 7].slice(0));
        var wynik = ([6, 19, 7, 9, 9, 42, 47, 5].slice(0));
        var kierunek = "prawo";
        var liczba = 3;
        if (!Main.listyRowne(Main.rotacjaV1(lista, kierunek, liczba), wynik)) {
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
