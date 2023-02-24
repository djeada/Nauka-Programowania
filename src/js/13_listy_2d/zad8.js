/*
Otrzymujesz liste list liczb naturalnych. Zbierz spiralnie
elementy otrzymanej macierzy i zapisz je w liscie.
*/
zbierzSpiralnie = function(macierz) {
    var wynik = new Array();
    var x = macierz[0].length;
    var y = macierz.length;
    var k = 0;
    var l = 0;
    while (k < y && l < x) {
        for (var i = l; i < x; i++)
            wynik.push(macierz[k][i]);
        k++;
        for (var i = k; i < y; i++)
            wynik.push(macierz[i][x - 1]);
        x--;
        if (k < x) {
            for (var i = x - 1; i > l - 1; i--)
                wynik.push(macierz[y - 1][i]);
            y--;
        }
        if (l < y) {
            for (var i = y - 1; i > k - 1; i--)
                wynik.push(macierz[i][l]);
            l++;
        }
    }
    return wynik;
}
test1 = function() {
    var macierz = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ];
    var oczekiwane = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25];
    var wynik = zbierzSpiralnie(macierz);
    if (wynik.length != oczekiwane.length) {
        throw new Error(`Assertion error line 24: ${wynik.length} != ${oczekiwane.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (wynik[i] != oczekiwane[i]) {
            throw new Error(`Assertion error line 24: ${wynik[i]} != ${oczekiwane[i]}`);
        }
    }
}
main = function(args) {
    test1();
    test2();
}

main(null);