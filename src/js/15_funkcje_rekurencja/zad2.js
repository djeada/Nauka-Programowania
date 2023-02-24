/*
Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz
sume liczb naturalnych mniejszych od N.
*/

sumaLiczb = function(n) {
    if (n === 0) {
        return 0;
    }
    return n + sumaLiczb(n - 1);
}
test1 = function() {
    var n = 5;
    var oczekiwane = 15;
    var wynik = sumaLiczb(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 20: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}
main = function(args) {
    test1();
}

main()