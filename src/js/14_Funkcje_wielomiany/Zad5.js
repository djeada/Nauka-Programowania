/*
Otrzymujesz liste n wspolczynnikow wielomianu postaci anxn+an-1xn-1+...+a0
oraz liczbe k. Oblicz wspolczynniki wielomianu bedacego k-ta pochodna
otrzymanego wielomianu.
*/
pochodnaWielomianu = function(wspolczynniki, k) {
    var wynik = [];
    var kopia = wspolczynniki.slice();
    for (var i = 0; i < k; i++) {
        wynik = [];
        var n = kopia.length;
        for (var j = 0; j < n - 1; j++)
            wynik.push(kopia[j] * (n - j - 1));
        kopia = wynik;
    }
    return wynik;
}
test1 = function() {
    var wielomian = [4, -3, 2];
    var k = 1;
    var oczekiwane = [8, -3];
    var wynik = pochodnaWielomianu(wielomian, k);
    if (wynik.length !== oczekiwane.length) {
        throw new Error(`Assertion error line 28: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (wynik[i] !== oczekiwane[i]) {
            throw new Error(`Assertion error line 32: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
        }
    }
};
test2 = function() {
    var wielomian = [13, -6, 0, -1, -1];
    var k = 2;
    var oczekiwane = [156, -36, 0];
    var wynik = pochodnaWielomianu(wielomian, k);
    if (wynik.length !== oczekiwane.length) {
        throw new Error(`Assertion error line 42: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (wynik[i] !== oczekiwane[i]) {
            throw new Error(`Assertion error line 46: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
        }
    }
}
main = function(args) {
    test1();
    test2();
}

main(null);