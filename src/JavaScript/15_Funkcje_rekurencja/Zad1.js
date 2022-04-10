/*
Otrzymujesz liczbe N. Przy uzyciu rekurencji zbuduj napis skladajacy
sie z liczb naturalnych mniejszych od N oddzielonych przecinkami.
*/
zbudujNapis = function(n) {
    if (n === 0) {
        return "";
    }
    if (n === 1) {
        return "1";
    }
    return zbudujNapis(n - 1) + "," + n;
}
test1 = function() {
    var n = 5;
    var oczekiwane = "1,2,3,4,5";
    var wynik = zbudujNapis(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}
main = function(args) {
    test1();
}

main(null);