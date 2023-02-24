/*
Otrzymujesz liczbe naturalna. Zwroc binarna
reprezentacje otrzymanej liczby jesli:
a) Otrzymana liczba jest liczba parzysta.
b) Otrzymana liczba jest liczba pierwsza.
W przeciwnym wypadku zwroc pusty napis.
*/

binarnaReprezentacja = function(n) {
    if (n === 0) {
        return "0";
    }
    if (n === 1) {
        return "1";
    }
    return binarnaReprezentacja(Math.floor(n / 2)) + n % 2;
}
zwrocParzysta = function(n) {
    if (n % 2 === 0) {
        return binarnaReprezentacja(n);
    }
    return "";
}
czyPierwsza = function(n) {
    if (n <= 1) {
        return false;
    }
    if (n % 2 === 0 && n !== 2) {
        return false;
    }
    for (var i = 3; i <= Math.sqrt(n); i += 2) {
        {
            if (n % i === 0) {
                return false;
            }
        };
    }
    return true;
}
zwrocPierwsza = function(n) {
    if (czyPierwsza(n)) {
        return binarnaReprezentacja(n);
    }
    return "";
}

test1 = function() {
    var n = 3;
    var oczekiwane = "";
    var wynik = zwrocParzysta(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test2 = function() {
    var n = 124;
    var oczekiwane = "1111100";
    var wynik = zwrocParzysta(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test3 = function() {
    var n = 124;
    var oczekiwane = "";
    var wynik = zwrocPierwsza(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test4 = function() {
    var n = 3;
    var oczekiwane = "11";
    var wynik = zwrocPierwsza(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

main = function() {
    test1();
    test2();
    test3();
    test4();
}
main();