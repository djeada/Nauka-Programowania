/*
Otrzymuje dwie liczby a i b. Przy uzyciu rekurencji
oblicz ile wynosi a podniesione do b.
*/
potega = function(a, b) {
    if (b === 0) {
        return 1;
    }
    return a * potega(a, b - 1);
}
test1 = function() {
    var a = 2;
    var b = 3;
    var oczekiwane = 8;
    var wynik = potega(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 21: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}
main = function(args) {
    test1();
}

}
main()