/*
Otrzymujesz dwie liczby naturalne. Oblicz ile bitow
nalezy odwrocic, aby zamienic liczbe A w liczbe B.
*/

bityDoZmiany = function(a, b) {
    var n = a ^ b;
    var licznik = 0;
    while (n != 0) {
        n &= (n - 1);
        licznik++;
    }
    return licznik;
}


test1 = function() {
    var a = 34;
    var b = 73;
    var oczekiwane = 5;
    var wynik = bityDoZmiany(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

main = function() {
    test1();
}

main();