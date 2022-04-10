/*
Otrzymujesz liczbe N. Przy uzyciu rekurencji
oblicz wartosc N-tego wyrazu ciagu Fibonacciego.
*/
fibonacci = function(n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}
test1 = function() {
    var n = 5;
    var oczekiwane = 5;
    var wynik = fibonacci(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 20: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}
main = function(args) {
    test1();
}

}
main()