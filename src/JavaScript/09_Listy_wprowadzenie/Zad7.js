var Main = /** @class */ (function() {
    function Main() {}
    Main.wieksza = function(lista) {
        if ((lista.length == 0)) {
            return 0.0;
        }
        if (lista.length === 1) {
            return lista[0] - 1;
        }
        var maks = -2147483648;
        var maks2 = -2147483648;
        for (var i = 0; i < lista.length; i++) {
            var liczba = lista[i]; {
                if (liczba > maks) {
                    maks2 = maks;
                    maks = liczba;
                } else if (liczba > maks2) {
                    maks2 = liczba;
                }
            }
        }
        return (maks + maks2) / 2.0;
    };
    Main.main = function(args) {
        var lista = ([3, 5, -7, 4, 9, -11, 2].slice(0));
        console.info(Main.wieksza(lista));
        lista = ([3, -2, 4, 9, -3, -40, 8, 5, -7, -1].slice(0));
        console.info(Main.wieksza(lista));
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
