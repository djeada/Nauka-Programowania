/*
a) Otrzymujesz dziesietna reprezentacje liczby naturalnej, zwroc jej binarna
reprezentacje. 
b) Otrzymujesz binarna reprezentacje liczby naturalnej, zwroc jej
dziesietna reprezentacje.
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

dziesietnaReprezentacja = function(n) {
    if (n === "0") {
        return 0;
    }
    if (n === "1") {
        return 1;
    }
    return dziesietnaReprezentacja(n.substring(0, n.length - 1)) * 2 + parseInt(n.charAt(n.length - 1));
}

test1 = function() {
    var n = 5;
    var oczekiwane = "101";
    var wynik = binarnaReprezentacja(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

test2 = function() {
    var n = "101";
    var oczekiwane = 5;
    var wynik = dziesietnaReprezentacja(n);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}

main = function(args) {
    test1();
    test2();
}

main(null);