/*
Otrzymujesz dziesietna reprezentacje liczby naturalnej.
Zamien miejscami sasiadujace bity w zapisie binarnym
otrzymanej liczbie. Zwroc dziesietna reprezentacje wyniku.
*/

zamienMiejscami = function(liczba) {
    var parzyste = liczba & 0xAAAAAAAA;
    var nieparzyste = liczba & 0x55555555;

    parzyste >>= 1;
    nieparzyste <<= 1;

    return parzyste | nieparzyste;
}


test1 = function() {
    var liczba = 9131;
    var oczekiwane = 4951;
    var wynik = zamienMiejscami(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

main = function(args) {
    test1();
}

main(null);