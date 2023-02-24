/*
Otrzymujesz slownik par napisow i liczb calkowitych oraz pojedyncza
liczbe calkowita. Usun ze slownika pary, dla ktorych wartosc rowna
jest otrzymanej liczbie.
*/

usun = function(slownik, liczba) {
    for (var klucz in slownik) {
        if (slownik[klucz] === liczba) {
            delete slownik[klucz];
        }
    }
    return slownik;
}


test1 = function() {
    var slownik = {
        "aaa": 5,
        "abc": 1,
        "xxx": 5,
        "cba": 3
    };
    var liczba = 5;

    var oczekiwane = {
        "abc": 1,
        "cba": 3
    };

    var wynik = usun(slownik, liczba);

    if (slownik !== wynik) {
        throw new Error(`Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test2 = function() {
    var slownik = {
        "slownik": 3,
        "word": 3,
        "lll": 3,
        "mmn": 1
    };
    var liczba = 3;

    var oczekiwane = {
        "mmn": 1
    };

    var wynik = usun(slownik, liczba);

    if (slownik !== wynik) {
        throw new Error(`Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


main = function() {
    test1();
    test2();
}

main();