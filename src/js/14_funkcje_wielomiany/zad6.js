/*
Otrzymujesz liste wspolczynnikow rownania kwadratowego ax^2 + bx + c.
Znajdz rzeczywiste miejsca zerowe rownania kwadratowego.
*/
miejscaZerowe = function(wspolczynniki) {
    var a = wspolczynniki[0];
    var b = wspolczynniki[1];
    var c = wspolczynniki[2];
    var delta = Math.pow(b, 2) - 4 * a * c;
    var wynik = [];
    if (delta < 0) {
        return wynik;
    } else if (delta === 0) {
        wynik[0] = -b / (2 * a);
        return wynik;
    } else {
        wynik[0] = (-b - Math.sqrt(delta)) / (2 * a);
        wynik[1] = (-b + Math.sqrt(delta)) / (2 * a);
        return wynik;
    }
}
test1 = function() {
    var wspolczynniki = [1, 2, 1];
    var oczekiwane = [-1];
    var wynik = miejscaZerowe(wspolczynniki);
    if (wynik.length !== oczekiwane.length) {
        throw new Error(`Assertion error line 33: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (wynik[i] !== oczekiwane[i]) {
            throw new Error(`Assertion error line 37: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
        }
    }
}
main = function(args) {
    test1();
}

main(null);