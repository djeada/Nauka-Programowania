/*
Otrzymuejsz napis. Sprawdz przy pomocy rekurencji czy otrzymane slowo
jest slowem elfickim. Przez slowo elfickie rozumiemy taki napis, w
ktorym co najmniej raz wystepuje kazda z liter slowa elf.
*/
znajdz = function(slowo, znak, pozycja) {
    if (pozycja === void 0) {
        pozycja = 0;
    }
    if (pozycja >= slowo.length)
        return -1;
    if (slowo[pozycja] == znak)
        return pozycja;
    return znajdz(slowo, znak, pozycja + 1);
}
czySlowoElfickie = function(slowo, elf) {
    if (elf === void 0) {
        elf = "elf";
    }
    if (elf.length === 0)
        return true;
    if (slowo.length === 0)
        return false;
    var pozycja = znajdz(slowo, elf[0]);
    if (pozycja === -1)
        return false;

    slowo = slowo.substring(0, pozycja) + slowo.substring(pozycja + 1);
    return czySlowoElfickie(slowo, elf.substr(1));
}
test1 = function() {
    var slowo = "reflektor";
    var oczekiwane = true;
    var wynik = czySlowoElfickie(slowo);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 36: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}
test2 = function() {
    var slowo = "elzbieta";
    var oczekiwane = false;
    var wynik = czySlowoElfickie(slowo);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 43: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}
main = function(args) {
    test1();
    test2();
}

main(null);