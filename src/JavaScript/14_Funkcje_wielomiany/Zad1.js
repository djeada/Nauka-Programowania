/*
Otrzymujesz liste n wspolczynnikow wielomianu postaci: a_nx^n + a_(n-1)x^(n-1) +
... + a_0 oraz liczbe naturalna x. Znajdz wartosc wielomianu w zadanym punkcie.
*/
wartoscWielomianu = function(wspolczynniki, x) {
    var wynik = 0;
    for (var i = 0; i < wspolczynniki.length; i++) {
        wynik += wspolczynniki[i] * Math.pow(x, i);
    }
    return wynik;
}
test1 = function() {
    var wielomian = [3, 2, 1];
    var x = 1;
    var wynik = 6;
    if (wartoscWielomianu(wielomian, x) !== wynik) {
        throw new Error(`Assertion error line 22: oczekiwane: ${wynik}, obliczone: ${wartoscWielomianu(wielomian, x)}`);
    }
}
main = function(args) {
    test1();
}

main(null);