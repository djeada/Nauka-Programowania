/*
Otrzymujesz liczbe N. Oblicz wartosc N-tego wyrazu ciagu danego wzorem
rekurencyjnym: a_1 = 1 a_n = 1 + 2a_(n-1)
*/
wartoscWyrazu = function(n) {
    if (n <= 1) {
        return n;
    }
    return 1 + 2 * wartoscWyrazu(n - 1);
}
test1 = function() {
    var n = 5;
    var oczekiwane = 31;
    var wynik = wartoscWyrazu(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 20: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}
main = function(args) {
    test1();
}

}
main()