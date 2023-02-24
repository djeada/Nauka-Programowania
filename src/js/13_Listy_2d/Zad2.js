/*
Dla otrzymanej liczby, stworz macierz kwadratowa skladajaca sie
z liczby kolumn i wierszy rownej otrzymanej liczbie, ktorej kazdy
element jest iloczynem jego wspolrzednych.
*/
stworzMacierz = function(a) {
    var macierz = [];
    for (var i = 0; i < a; i++) {
        macierz[i] = [];
        for (var j = 0; j < a; j++) {
            macierz[i][j] = i * j;
        }
    }
    return macierz;
}
test1 = function() {
    var a = 3;
    var oczekiwane = [
        [0, 0, 0],
        [0, 1, 2],
        [0, 2, 4]
    ];
    var wynik = stworzMacierz(a);
    if (wynik.length !== oczekiwane.length) {
        throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (wynik[i].length !== oczekiwane[i].length) {
            throw new Error(`Assertion error line 29: ${wynik[i].length} != ${oczekiwane[i].length}`);
        }
        for (var j = 0; j < wynik[i].length; j++) {
            if (wynik[i][j] !== oczekiwane[i][j]) {
                throw new Error(`Assertion error line 29: ${wynik[i][j]} != ${oczekiwane[i][j]}`);
            }
        }
    }
}
main = function(args) {
    test1();
}

main(null);