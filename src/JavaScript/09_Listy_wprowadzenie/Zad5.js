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
    Main.test1 = function() {
        var lista = [3, 5, -7, 4, 9, -11, 2]
        var oczekiwane = [4, 5, -6, 4, 10, -11, 3]
        var wynik = Main.zwieksz(lista)
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 85: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 89: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
            }
        }
    };
    Main.test2 = function() {
        var lista = [3, 5, -7, 4, 9, -11, 2]
        var oczekiwane = [0, 5, -7, 4, 0, -11, 2]
        var wynik = Main.wyzeruj(lista)
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 98: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 102: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
            }
        }
    };
    Main.test3 = function() {
        var lista = [3, 5, -7, 4, 9, -11, 2]
        var oczekiwane = [3, 5, 5, 5, 9, 5, 2]
        var wynik = Main.suma(lista)
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 111: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 115: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
            }
        }
    };
    Main.test4 = function() {
        var lista = [3, 5, -7, 4, 9, -11, 2]
        var oczekiwane = [27720, 16632, -11880, 20790, 9240, -7560, 41580]
        var wynik = Main.zamien(lista)
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 124: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 128: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
            }
        }
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
