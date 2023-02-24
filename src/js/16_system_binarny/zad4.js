/*
Otrzymujesz dziesietna reprezentacje liczby naturalnej.
a) Oblicz z ilu zer sklada sie binarna reprezentacja otrzymanej liczby.
b) Oblicz z ilu jedynek sklada sie binarna reprezentacja otrzymanej liczby.
*/

zera = function(liczba) {
    var zera = 0;
    while (liczba > 0) {
        if (liczba & 1 == 0)
            zera++;
        liczba >>= 1;
    }
    return zera;
}

jedynki = function(liczba) {
    var jedynki = 0;
    while (liczba > 0) {
        if (liczba & 1 == 1)
            jedynki++;
        liczba >>= 1;
    }
    return jedynki;
}

test1 = function() {
    var a = -2;
    var oczekiwane = 0;
    var wynik = zera(a);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test2 = function() {
    var a = 3;
    var oczekiwane = 2;
    var wynik = jedynki(a);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 89: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test3 = function() {
    var a = 3;
    var oczekiwane = 0;
    var wynik = zera(a);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 99: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test4 = function() {
    var a = 7;
    var oczekiwane = 3;
    var wynik = jedynki(a);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 109: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

main = function() {
    test1();
    test2();
    test3();
    test4();
}

main();