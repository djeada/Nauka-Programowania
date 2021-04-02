var Main = /** @class */ (function() {
    function Main() {}
    Main.zwieksz = function(lista) {
        for (var i = 0; i < lista.length; i++) {
            {
                if (i % 2 === 0) {
                    (lista[i] = lista[i] + 1);
                }
            };
        }
        return lista;
    };
    Main.wyzeruj = function(lista) {
        for (var i = 0; i < lista.length; i++) {
            {
                if (lista[i] % 3 === 0) {
                    (lista[i] = 0);
                }
            };
        }
        return lista;
    };
    Main.kwadrat = function(lista) {
        for (var i = 0; i < lista.length; i++) {
            {
                if (lista[i] < 10) {
                    (lista[i] = (Math.pow(lista[i], 2) | 0));
                }
            };
        }
        return lista;
    };
    Main.czyPierwsza = function(n) {
        if ((n % 2 === 0 && n !== 2) || n < 1) {
            return false;
        }
        for (var i = 3; i <= Math.sqrt(n); i += 2) {
            {
                if ((n % i) === 0) {
                    return false;
                }
            };
        }
        return true;
    };
    Main.suma = function(lista) {
        var suma = 0;
        for (var i = 0; i < lista.length; i++) {
            var liczba = lista[i];
            suma += liczba;
        }
        for (var i = 0; i < lista.length; i++) {
            {
                if (Main.czyPierwsza(i)) {
                    (lista[i] = suma);
                }
            };
        }
        return lista;
    };
    Main.zamien = function(lista) {
        var iloczyny = ([]);
        for (var i = 0; i < lista.length; i++) {
            {
                var iloczyn = 1;
                for (var j = 0; j < lista.length; j++) {
                    {
                        if (j === i) {
                            continue;
                        }
                        iloczyn *= lista[j];
                    };
                }

                (iloczyny.push(iloczyn) > 0);
            };
        }
        return iloczyny;
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
        var lista = ([3, 5, -7, 4, 9, -11, 2].slice(0));
        var wynik = ([4, 5, -6, 4, 10, -11, 3].slice(0));
        if (!Main.listyRowne(wynik, Main.zwieksz(lista))) {
            throw new Error("Assertion error: assert wynik.equals(zwieksz(lista));");
        };
    };
    Main.test2 = function() {
        var lista = ([3, 5, -7, 4, 9, -11, 2].slice(0));
        var wynik = ([0, 5, -7, 4, 0, -11, 2].slice(0));
        if (!Main.listyRowne(wynik, Main.wyzeruj(lista))) {
            throw new Error("Assertion error: assert wynik.equals(wyzeruj(lista));");
        };
    };
    Main.test3 = function() {
        var lista = ([3, 5, -7, 4, 9, -11, 2].slice(0));
        var wynik = ([3, 5, 5, 5, 9, 5, 2].slice(0));
        if (!Main.listyRowne(wynik, Main.suma(lista))) {
            throw new Error("Assertion error: assert wynik.equals(suma(lista));");
        };
    };
    Main.test4 = function() {
        var lista = ([3, 5, -7, 4, 9, -11, 2].slice(0));
        var wynik = ([27720, 16632, -11880, 20790, 9240, -7560, 41580].slice(0));
        if (!Main.listyRowne(wynik, Main.zamien(lista))) {
            throw new Error("Assertion error: assert wynik.equals(zamien(lista));");
        };
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
        Main.test3();
        Main.test4();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
