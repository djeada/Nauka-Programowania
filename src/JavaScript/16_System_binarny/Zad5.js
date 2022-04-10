/*
Otrzymujesz dwie liczby naturalne.
a) Zwroc mniejsza liczbe. Zabronione jest uzycie instrukcji
warunkowej i zewnetrznych bibliotek.
b) Zwroc wieksza liczbe. Zabronione jest uzycie instrukcji
warunkowej i zewnetrznych bibliotek.
*/

znak = function(n) {
    return (n >> 31) & 0x01;
}

maks = function(a, b) {
    var znakB = znak(a - b);
    var znakA = znakB ^ 1;
    return znakA * a + znakB * b;
}

min = function(a, b) {
    var znakB = znak(a - b);
    var znakA = znakB ^ 1;
    return znakB * a + znakA * b;
}

test1 = function() {
    var a = -2;
    var b = 8;
    var oczekiwane = 8;
    var wynik = maks(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test2 = function() {
    var a = 3;
    var b = 8;
    var oczekiwane = 3;
    var wynik = min(a, b);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 89: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

main = function() {
    test1();
    test2();
}

main();