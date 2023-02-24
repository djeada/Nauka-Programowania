/*
Otrzymujesz liste list liczb naturalnych. Znajdz w macierzy klepsydre o
najwiekszej sumie. Klepsydra sklada sie z dokladnie 7 elementow. Trzy pierwsze
elementy sa kolejnymi elementami dowolnego wiersza macierzy. Nastepny element
znajduje sie w tej samej kolumnie co drugi element i w dokladnie jednym wierszu
nizej. Trzy nastepne znajduja sie w tych samych kolumnach co trzy pierwsze i
dokladnie dwa wiersze nizej.
*/
klepsydraNajwiekszaSuma = function(macierz) {
    var wynik = Number.MIN_SAFE_INTEGER;
    var N = macierz.length;
    for (var wiersz = 0; wiersz < N; wiersz++) {
        for (var kolumna = 0; kolumna < N; kolumna++) {
            if (!(wiersz == 0 || wiersz == N - 1 || kolumna == 0 || kolumna == N - 1)) {
                var suma = macierz[wiersz - 1][kolumna - 1] + macierz[wiersz - 1][kolumna] + macierz[wiersz - 1][kolumna + 1] + macierz[wiersz][kolumna] + macierz[wiersz + 1][kolumna - 1] + macierz[wiersz + 1][kolumna] + macierz[wiersz + 1][kolumna + 1];
                wynik = Math.max(wynik, suma);
            }
        }
    }
    return wynik;
}
test1 = function() {
    var macierz = [
        [10, 99, 28, 21, 78],
        [35, 78, 31, 56, 24],
        [7, 18, 2, 50, 87],
        [59, 67, 9, 82, 53],
        [23, 26, 76, 62, 36]
    ];
    var oczekiwane = 395;
    var wynik = klepsydraNajwiekszaSuma(macierz);
    if (wynik != oczekiwane) {
        throw new Error(`Assertion error line 24: ${wynik} != ${oczekiwane}`);
    }
}
main = function(args) {
    test1();
}

main(null);