/*
Otrzymujesz macierz kwadratowa. Sprawdz, czy macierz jest kwadratem magicznym.
*/
sumujKolumny = function(macierz) {
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
sumujWiersze = function(macierz) {
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
sumujPrzekatne = function(macierz) {
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
czyKwadratMagiczny = function(macierz) {
    try {
        var sumaKolumn = sumujKolumny(macierz);
        var sumaWierszy = sumujWiersze(macierz);
        var sumaPrzekatnych = sumujPrzekatne(macierz);
    } catch (e) {
        return false;
    }
    if (sumaKolumn !== sumaWierszy || sumaKolumn !== sumaPrzekatnych) {
        return false;
    }
    return true;
};
test1 = function() {
    var a = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ];
    var oczekiwane = true;
    var wynik = czyKwadratMagiczny(a);
    if (wynik !== oczekiwane) {
        raiseError("Assertion error line 24: assert wynik.equals(oczekiwane);");
    }
}
test2 = function() {
    var a = [
        [1, 2],
        [-2, 0]
    ];
    var oczekiwane = false;
    var wynik = czyKwadratMagiczny(a);
    if (wynik !== oczekiwane) {
        raiseError("Assertion error line 24: assert wynik.equals(oczekiwane);");
    }
}
main = function(args) {
    test1();
    test2();
}

main(null);