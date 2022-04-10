/*
Dla otrzymanych dwoch list, stworz dwukolumnowa macierz, ktorej pierwsza
kolumna sklada sie z elementow pierwszej listy, a druga kolumna elementow
drugiej listy. Jesli otrzymane listy nie sa rownej dlugosci zwroc pusta macierz.
*/
stworzMacierz = function(listaA, listaB) {
    var macierz = [];
    if (listaA.length !== listaB.length) {
        return macierz;
    }
    for (var i = 0; i < listaA.length; i++) {
        macierz[i] = [];
        macierz[i][0] = listaA[i];
        macierz[i][1] = listaB[i];
    }
    return macierz;
}
test1 = function() {
    var listaA = [1, 2, 3];
    var listaB = [4, 5, 6];
    var oczekiwane = [
        [1, 4],
        [2, 5],
        [3, 6]
    ];
    var wynik = stworzMacierz(listaA, listaB);
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