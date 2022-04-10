/*
Otrzymujesz dwie liczby naturalne. Uzywajac jedynie operatorow
bitowych zaimplementuj:
a) Dodawanie.
b) Odejmowanie.
c) Mnozenie
d) Dzielenie.
*/

suma = function(a, b) {
    while (b != 0) {
        var pom = a & b;
        a = a ^ b;
        b = pom << 1;
    }
    return a;
}

roznica = function(a, b) {
    while (b != 0) {
        var pom = (~a) & b;
        a = a ^ b;
        b = pom << 1;
    }
    return a;
}

iloczyn = function(a, b) {
    var znak = (a < 0 && b >= 0) || (b < 0 && a >= 0) ? -1 : 1;
    if (a < 0)
        a *= -1;
    if (b < 0)
        b *= -1;
    var pom = 0;
    while (b != 0) {
        if (b & 1)
            pom += a;
        a <<= 1;
        b >>= 1;
    }
    return znak * pom;
}

wew_iloraz = function(dzielna, dzielnik, org_b, reszta) {
    var wynik = 1;
    if (dzielna == dzielnik) {
        reszta = 0;
        return 1;
    } else if (dzielna < dzielnik) {
        reszta = dzielna;
        return 0;
    }

    while (dzielnik <= dzielna) {
        dzielnik = dzielnik << 1;
        wynik = wynik << 1;
    }
    if (dzielna < dzielnik) {
        dzielnik >>= 1;
        wynik >>= 1;
    }
    wynik = wynik + wew_iloraz(dzielna - dzielnik, org_b, org_b, reszta);
    return wynik;
}

iloraz = function(a, b) {
    var znak = (a < 0 && b >= 0) || (b < 0 && a >= 0) ? -1 : 1;
    if (a < 0) {
        a *= -1;
    }
    if (b < 0) {
        b *= -1;
    }
    var reszta = 0;

    return znak * wew_iloraz(a, b, b, reszta);
}

test1 = function() {
    var a = -2;
    var b = 2;
    var oczekiwane = 0;
    var wynik = suma(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test2 = function() {
    var a = 3;
    var b = 2;
    var oczekiwane = 5;
    var wynik = suma(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 89: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test3 = function() {
    var a = 3;
    var b = 2;
    var oczekiwane = 1;
    var wynik = roznica(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 99: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test4 = function() {
    var a = 10;
    var b = 15;
    var oczekiwane = -5;
    var wynik = roznica(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 109: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test5 = function() {
    var a = 3;
    var b = 2;
    var oczekiwane = 6;
    var wynik = iloczyn(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 119: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test6 = function() {
    var a = 10;
    var b = -2;
    var oczekiwane = -20;
    var wynik = iloczyn(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 129: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test7 = function() {
    var a = 9;
    var b = 3;
    var oczekiwane = 3;
    var wynik = iloraz(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 139: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test8 = function() {
    var a = 25;
    var b = -5;
    var oczekiwane = -5;
    var wynik = iloraz(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

main = function() {
    test1();
    test2();
    test3();
    test4();
    test5();
    test6();
    test7();
    test8();
}

main();