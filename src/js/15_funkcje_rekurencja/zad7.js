/*
Otrzymujesz liste liczb naturalnych oraz klucz.
Przy uzyciu rekurencji znajdz indeks odpowiadajacy
pierwszemu wystapieniu klucza w liscie. Jesli
klucz nie wysteþuje w liscie, zwroc -1.
*/
znajdzIndeks = function(lista, klucz, indeks = 0) {
    if (lista.length === 0) {
        return -1;
    }
    if (lista[0] === klucz) {
        return indeks;
    }
    return znajdzIndeks(lista.slice(1), klucz, indeks + 1);
}
test1 = function() {
    var lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    var klucz = 5;
    var oczekiwane = 4;
    var wynik = znajdzIndeks(lista, klucz);
    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 26: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}
main = function(args) {
    test1();
}

main(null);