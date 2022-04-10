/*
Otrzymujesz dziesietna reprezentacje liczby naturalnej. Znajdz potege
dwojki wieksza badz rowna otrzymanej liczbie. Inaczej: zaokraglij liczbe
do nastepnej potegi dwojki.
*/


nastepnaPotegaDwojkiV1 = function(liczba) {
    if (liczba <= 0)
        return 0;

    if (liczba == 1)
        return 2;

    liczba--;

    while (liczba & (liczba - 1))
        liczba &= liczba - 1;

    return liczba << 1;
}


nastepnaPotegaDwojkiV2 = function(liczba) {
    if (liczba <= 0)
        return 0;

    var potega = 2;

    while (liczba > 2) {
        liczba >>= 1;
        potega <<= 1;
    }

    return potega;
}


test1 = function() {
    var liczba = 111;
    var oczekiwane = 128;
    var wynik = nastepnaPotegaDwojkiV1(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test2 = function() {
    var liczba = -30;
    var oczekiwane = 0;
    var wynik = nastepnaPotegaDwojkiV1(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 35: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


test3 = function() {
    var liczba = 1;
    var oczekiwane = 2;
    var wynik = nastepnaPotegaDwojkiV1(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 45: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


test4 = function() {
    var liczba = 111;
    var oczekiwane = 128;
    var wynik = nastepnaPotegaDwojkiV2(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


test5 = function() {
    var liczba = -30;
    var oczekiwane = 0;
    var wynik = nastepnaPotegaDwojkiV2(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 35: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test6 = function() {
    var liczba = 1;
    var oczekiwane = 2;
    var wynik = nastepnaPotegaDwojkiV2(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 45: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

main = function() {
    test1();
    test2();
    test3();
    test4();
    test5();
    test6();
}

main();