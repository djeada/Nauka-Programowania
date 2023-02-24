/*
Otrzymujesz liczbe N. Przy uzyciu rekurencji
oblicz silnie z otrzymanej liczby.
*/
silnia = function(n) {
    if (n <= 0) {
        return 1;
    }
    return n * silnia(n - 1);
}
test1 = function() {
    var n = 5;
    var oczekiwane = 120;
    var wynik = silnia(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 20: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}
main = function(args) {
    test1();
}

}
main()