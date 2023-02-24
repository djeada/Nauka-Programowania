/*
Otrzymujesz dwie listy liczb calkowitych. Zbuduj slownik skladajacy sie z
kluczy bedacych elementami pierwszej listy i wartosciami bedacymi elementami
drugiej listy. Jesli listy sa roznej dlugosci zwroc pusty slownik.
*/

zbudujSlownik = function(listaA, listaB) {
    var slownik = {};
    if (listaA.length !== listaB.length) {
        return slownik;
    }
    for (var i = 0; i < listaA.length; i++) {
        slownik[listaA[i]] = listaB[i];
    }
    return slownik;
}

test1 = function() {
    var listaA = [3, 5, 8];
    var listaB = [1, 2, -1];
    var oczekiwane = {
        3: 1,
        5: 2,
        8: -1
    };
    var wynik = zbudujSlownik(listaA, listaB);
    if (oczekiwane.length !== wynik.length) {
        throw new Error(`Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`);
    }

    for (const key in oczekiwane) {
        if (oczekiwane[key] !== wynik[key]) {
            throw new Error(`Assertion error line 34: ${wynik[key]} != ${oczekiwane[key]}`);
        }
    }
}


test2 = function() {
    var listaA = [0, 1];
    var listaB = [1, 0];
    var oczekiwane = {
        0: 1,
        1: 0
    };
    var wynik = zbudujSlownik(listaA, listaB);
    if (oczekiwane.length !== wynik.length) {
        throw new Error(`Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`);
    }

    for (const key in oczekiwane) {
        if (oczekiwane[key] !== wynik[key]) {
            throw new Error(`Assertion error line 34: ${wynik[key]} != ${oczekiwane[key]}`);
        }
    }
}

main = function() {
    test1();
    test2();
}

main();