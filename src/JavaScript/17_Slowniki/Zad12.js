/*
Otrzymujesz dwa slowniki skladajace sie z par napisow i list liczb calkowitych.
Listy sa nieuporzadkowane. Sprawdz czy slowniki skladaja sie z tych samych par.
Dwie listy uznajemy za identyczne jesli zawieraja te same elementy, przy
czym kolejnosc elementow moze byc zmieniona.
*/

slownikiIdentyczne = function(slownik1, slownik2) {
    if (Object.keys(slownik1).length !== Object.keys(slownik2).length) {
        return false;
    }
    for (const key in slownik1) {
        lista1 = slownik1[key]
        lista2 = slownik2[key]
        if (lista1.length !== lista2.length) {
            return false;
        }
        lista1.sort();
        lista2.sort();
        for (var i = 0; i < lista1.length; i++) {
            if (lista1[i] !== lista2[i]) {
                return false;
            }
        }
    }
    return true;
}

test1 = function() {
    var slownikA = {
        "c": [3, 2, 1],
        "x": [-2, 9, 11],
        "a": [4, 6, 7]
    }

    var slownikB = {
        "a": [7, 4, 6],
        "c": [2, 3, 1],
        "x": [-2, 11, 9]
    }

    oczekiwane = true;
    wynik = slownikiIdentyczne(slownikA, slownikB);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 34: ${wynik} != ${oczekiwane}`);
    }
}

test2 = function() {
    var slownikA = {
        "abc": [1, 2, 3],
        "123": [9, 0, 0],
        "xxx": [5, 5, 5]
    }

    var slownikB = {
        "abc": [1, 2, 3],
        "xxx": [0, 0, 9],
        "123": [5, 5, 5]
    }

    oczekiwane = false;
    wynik = slownikiIdentyczne(slownikA, slownikB);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 38: ${wynik} != ${oczekiwane}`);
    }
}

main = function() {
    test1();
    test2();
}

main();