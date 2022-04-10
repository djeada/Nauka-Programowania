/*
Otrzymujesz dwie listy n wspolczynnikow wielomianu postaci a_nx^n +
a_(n-1)x^(n-1) + ... + a_0. Oblicz wspolczynniki wielomianu bedacego iloczynem
otrzymanych wielomianow.
*/
iloczyn = function(wspolczynniki1, wspolczynniki2) {
    var wynik = [];
    for (var i = 0; i < wspolczynniki1.length; i++) {
        for (var j = 0; j < wspolczynniki2.length; j++) {
            if (i + j >= wynik.length) {
                wynik[i + j] = 0;
            }
            wynik[i + j] += wspolczynniki1[i] * wspolczynniki2[j];
        }
    }
    return wynik;
}
test1 = function() {
    var wielomianA = [5, 0, 10, 6];
    var wielomianB = [1, 2, 4];
    var oczekiwane = [5, 10, 30, 26, 52, 24];
    var wynik = iloczyn(wielomianA, wielomianB);
    if (wynik.length !== oczekiwane.length) {
        throw new Error(`Assertion error line 28: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (wynik[i] !== oczekiwane[i]) {
            throw new Error(`Assertion error line 32: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
        }
    }
}
main = function(args) {
    test1();
}

main(null);
//# sourceMappingURL=Zad4.js.m