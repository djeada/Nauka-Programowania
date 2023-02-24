/*
Dla dwoch slow, ile minimalnie znakow musimy usunac aby uzyskac anagramy.
Zwroc -1 dla slow o roznych dlugosciach.
*/
liczbaZnakow = function(slowoA, slowoB) {
    if (slowoA.length !== slowoB.length)
        return -1;
    var pom = new Array(256);
    for (var i = 0; i < 256; i++)
        pom[i] = 0;
    for (var i = 0; i < slowoA.length; i++) {
        pom[slowoA.charCodeAt(i)]++;
    }
    for (var i = 0; i < slowoB.length; i++) {
        pom[slowoB.charCodeAt(i)]--;
    }
    var wynik = 0;
    for (var i = 0; i < pom.length; i++) {
        wynik += Math.abs(pom[i]);
    }
    return wynik;
};
test1 = function() {
    var slowoA = "adam";
    var slowoB = "mada";
    var oczekiwane = 0;
    var wynik = liczbaZnakow(slowoA, slowoB);
    if (!(wynik === oczekiwane)) {
        throw new Error(`Assertion error line 29: ${wynik} === ${oczekiwane}`);
    }
};
test2 = function() {
    var slowoA = "adam";
    var slowoB = "ada";
    var oczekiwane = -1;
    var wynik = liczbaZnakow(slowoA, slowoB);
    if (!(wynik === oczekiwane)) {
        throw new Error(`Assertion error line 29: ${wynik} === ${oczekiwane}`);
    }
};
test3 = function() {
    var slowoA = "20ejdy0978oa";
    var slowoB = "akv81w39j1ob";
    var oczekiwane = 14;
    var wynik = liczbaZnakow(slowoA, slowoB);
    if (!(wynik === oczekiwane)) {
        throw new Error(`Assertion error line 29: ${wynik} === ${oczekiwane}`);
    }
};
main = function(args) {
    test1();
    test2();
    test3();
};

main(null);