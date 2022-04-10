/*
Znajdz permutacje danego slowa bedace palindromami.
*/
permutacje = function(napis) {
    if (napis.length === 1)
        return [napis];
    var permutacje = [];
    for (var i = 0; i < napis.length; i++) {
        var znak = napis.charAt(i);
        var reszta = permutacje(napis.substring(0, i) + napis.substring(i + 1));
        for (var j = 0; j < reszta.length; j++) {
            permutacje.push(znak + reszta[j]);
        }
    }
    return permutacje;
}
czyPalindrom = function(napis) {
    var odwroc = odwrocNapis(napis);
    return (odwroc === napis);
}
odwrocNapis = function(napis) {
    if (napis.length === 1)
        return napis;
    return odwrocNapis(napis.substring(1)) + napis.charAt(0);
}
permutacjePalindomiczne = function(napis) {
    var permutacje = permutacje(napis);
    var wynik = new Set();
    for (var i = 0; i < permutacje.length; i++) {
        if (czyPalindrom(permutacje[i])) {
            wynik.add(permutacje[i]);
        }
    }
    return Array.from(wynik);
}
test1 = function() {
    var napis = "adamm";
    var oczekiwane = ["madam", "amdma"];
    var wynik = permutacjePalindomiczne(napis);
    if (wynik.length !== oczekiwane.length) {
        throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
    }
    oczekiwane.sort();
    wynik.sort();
    for (var i = 0; i < oczekiwane.length; i++) {
        if (wynik[i] !== oczekiwane[i]) {
            throw new Error(`Assertion error line 29: ${wynik[i]} != ${oczekiwane[i]}`);
        }
    }
}
main = function(args) {
    test1();
}

main(null);