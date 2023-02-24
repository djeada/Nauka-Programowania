/*
Otrzymujesz liste list liczb naturalnych reprezentujaca macierz.
Jesli element macierzy jest rowny zero, zamien wszystkie elementy
w tej samej kolumnie i tym samym wierszu na zera.
*/
zamienNaZero = function(macierz) {
    var M = macierz.length;
    var N = macierz[0].length;
    var wiersze = new Array(M);
    var kolumny = new Array(N);
    for (var i = 0; i < M; i++) {
        wiersze[i] = 0;
        for (var j = 0; j < N; j++) {
            if (macierz[i][j] == 0) {
                wiersze[i] = 1;
                kolumny[j] = 1;
            }
        }
    }
    for (var i = 0; i < M; i++) {
        for (var j = 0; j < N; j++) {
            if (wiersze[i] == 1 || kolumny[j] == 1)
                macierz[i][j] = 0;
        }
    }
    return macierz;
}
test1 = function() {
    var macierz = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ];
    var oczekiwane = [
        [1, 0, 3],
        [0, 0, 0],
        [7, 0, 9]
    ];
    var wynik = zamienNaZero(macierz);
    if (wynik.length != oczekiwane.length) {
        throw new Error(`Assertion error line 24: ${wynik.length} != ${oczekiwane.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (wynik[i].length != oczekiwane[i].length) {
            throw new Error(`Assertion error line 24: ${wynik[i].length} != ${oczekiwane[i].length}`);
        }
        for (var j = 0; j < wynik[i].length; j++) {
            if (wynik[i][j] != oczekiwane[i][j]) {
                throw new Error(`Assertion error line 24: ${wynik[i][j]} != ${oczekiwane[i][j]}`);
            }
        }
    }
}
main = function(args) {
    test1();
}

main(null);