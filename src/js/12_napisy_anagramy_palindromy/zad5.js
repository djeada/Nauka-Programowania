/*
Otrzymujesz napis reprezentujacy zdanie oraz slowo. Znajdz wszystkie
anagramy  otrzymanego slowa w zdaniu. Roznice miedzy wielkimi i malymi
literami powinny byc zignorowane.
*/
czyAnagram = function(napis1, napis2) {
    if (napis1.length !== napis2.length)
        return false;
    var tab1 = zamienNaTab(napis1);
    var tab2 = zamienNaTab(napis2);
    for (var i = 0; i < tab1.length; i++) {
        var index = tab2.indexOf(tab1[i]);
        if (index === -1)
            return false;
        tab2.splice(index, 1);
    }
    return true;
}
zamienNaTab = function(napis) {
    var tab = [];
    for (var i = 0; i < napis.length; i++) {
        tab.push(napis[i]);
    }
    return tab;
}
rozdzielNaSlowa = function(napis) {
    var words = napis.split(/[\s,]+/);
    for (var i = 0; i < words.length; i++) {
        words[i] = words[i].replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "");
    }
    return words;
}
anagramy = function(napis, slowo) {
    var words = rozdzielNaSlowa(napis);
    var anagramy = [];
    for (var i = 0; i < words.length; i++) {
        if (czyAnagram(words[i], slowo))
            anagramy.push(words[i]);
    }
    return anagramy;
}
test1 = function() {
    var zdanie = "Za jego nikczemne uczynki, spotakla go wysoce sroga kara."
    var slowo = "arak";
    var oczekiwane = ["kara"];
    var wynik = anagramy(zdanie, slowo);
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
};
main = function(args) {
    test1();
}

main(null);