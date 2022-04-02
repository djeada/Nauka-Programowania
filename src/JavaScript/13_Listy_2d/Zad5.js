/*
Otrzymujesz macierz kwadratowa. Sprawdz, czy macierz jest kwadratem magicznym.
*/

var Main = /** @class */ (function () { 
    function Main() { }
    Main.sumujKolumny = function (macierz) {
        var sumy = [];
        for (var i = 0; i < macierz.length; i++) {
            sumy[i] = 0;
            for (var j = 0; j < macierz[i].length; j++) {
                sumy[i] += macierz[i][j];
            }
        }
    
        for (var i = 0; i < sumy.length; i++) {
            if (sumy[i] !== sumy[(i + 1) % sumy.length]) {
                raiseError("Assertion error line 24: assert sumy[i].equals(sumy[(i + 1) % sumy.length]);");
            }
        }
        return sumy[0];
    };

    Main.sumujWiersze = function (macierz) {
        var sumy = [];
        for (var i = 0; i < macierz.length; i++) {
            sumy[i] = 0;
            for (var j = 0; j < macierz[i].length; j++) {
                sumy[i] += macierz[j][i];
            }
        }

        for (var i = 0; i < sumy.length; i++) {
            if (sumy[i] !== sumy[(i + 1) % sumy.length]) {
                raiseError("Assertion error line 24: assert sumy[i].equals(sumy[(i + 1) % sumy.length]);");
            }
        }
        return sumy[0];
    };

    Main.sumujPrzekatne = function (macierz) {
        var sumy = [];
        for (var i = 0; i < 2; i++) {
            sumy[i] = 0;
            for (var j = 0; j < macierz.length; j++) {
                sumy[i] += macierz[j][j];
            }
        }

        if (sumy[0] !== sumy[1]) {
            raiseError("Assertion error line 24: assert sumy[0].equals(sumy[1]);");
        }

        return sumy[0];
    };

    Main.czyKwadratMagiczny = function (macierz) {
        try {
            var sumaKolumn = Main.sumujKolumny(macierz);
            var sumaWierszy = Main.sumujWiersze(macierz);
            var sumaPrzekatnych = Main.sumujPrzekatne(macierz);
        }
        catch (e) {
            return false;
        }

        if (sumaKolumn !== sumaWierszy || sumaKolumn !== sumaPrzekatnych) {
            return false;
        }

        return true;
    };
    Main.test1 = function () {
        var a = [[2, 7, 6], [9, 5, 1], [4, 3, 8]];
        if (!Main.czyKwadratMagiczny(a)) {
            throw new Error("Assertion error linde 24: assert czyKwadratMagiczny(a);");
        }
    }
    Main.test2 = function () {
        var a = [[1, 2], [-2, 0]];
        if (Main.czyKwadratMagiczny(a)) {
            throw new Error("Assertion error line 30: assert !czyKwadratMagiczny(a);");
        }
    }
    Main.main = function (args) {
        Main.test1();
        Main.test2();
    }
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
