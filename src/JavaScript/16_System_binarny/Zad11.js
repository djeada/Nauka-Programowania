/*
Otrzymujesz dziesietna reprezentacje liczby naturalnej.
Sprawdz czy binarna reprezentacja otrzymanej liczby jest palindromem.
*/

const liczbaBitow = 8;

czyPalindrom = function(liczba) {
    var bity = liczba.toString(2);

    for (var i = 0; i < liczbaBitow / 2 - 1; i++) {
        if (bity[i] ^ bity[liczbaBitow - 1 - i])
            return false;
    }

    return true;
}

test1 = function() {
    var liczba = 231;
    var oczekiwane = true;
    var wynik = czyPalindrom(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test2 = function() {
    var liczba = 17;
    var oczekiwane = false;
    var wynik = czyPalindrom(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 89: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

main = function() {
    test1();
    test2();
}

main();