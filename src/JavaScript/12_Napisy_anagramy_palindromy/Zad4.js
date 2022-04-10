/*
Otrzymujesz napis reprezentujacy zdanie. Znajdz wszystkie palindromy
w zdaniu. Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.
*/
czyPalindrom = function(napis) {
    var napis1 = napis.toLowerCase();
    var napis2 = napis.toLowerCase();
    napis2 = napis2.split("").reverse().join("");
    if (napis1 === napis2)
        return true;
    return false;
}
rozdzielNaSlowa = function(napis) {
    var words = napis.split(/[\s,]+/);
    for (var i = 0; i < words.length; i++) {
        words[i] = words[i].replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "");
    }
    return words;
}
palindromy = function(napis) {
    var words = rozdzielNaSlowa(napis);
    var palindromy = [];
    for (var i = 0; i < words.length; i++) {
        if (czyPalindrom(words[i]))
            palindromy.push(words[i]);
    }
    return palindromy;
}
test1 = function() {
    var zdanie = "Tata zbaral kajak na wycieczke i uderzyl sie w oko.";
    var oczekiwane = ["kajak", "i", "w", "oko"];
    var wynik = palindromy(zdanie);
    if (oczekiwane.length != wynik.length) {
        throw new Error(`Assertion error line 24: ${oczekiwane.length} != ${wynik.length}`);
    }
    oczekiwane.sort();
    wynik.sort();
    for (var i = 0; i < oczekiwane.length; i++) {
        if (oczekiwane[i] != wynik[i]) {
            throw new Error(`Assertion error line 24: ${oczekiwane[i]} != ${wynik[i]}`);
        }
    }
};
main = function(args) {
    test1();
}

main(null);