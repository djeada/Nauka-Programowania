/*
Otrzymujesz napis. Znajdz czestosc wystepowania znakow w otrzymanym
napisie. Inaczej, zwroc histogram znakow w otrzymanym napisie.
*/

histogram = function(napis) {
    var histogram = {};
    for (const znak of napis) {
        if (histogram[znak] === undefined) {
            histogram[znak] = 1;
        } else {
            histogram[znak]++;
        }
    }
    return histogram;
}

test1 = function() {
    var slowo = "klasa";
    var oczekiwane = {
        'k': 1,
        'l': 1,
        'a': 2,
        's': 1
    };
    var wynik = histogram(slowo);
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
    var slowo = "robot";
    var oczekiwane = {
        'r': 1,
        'o': 2,
        'b': 1,
        't': 1
    };
    var wynik = histogram(slowo);
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