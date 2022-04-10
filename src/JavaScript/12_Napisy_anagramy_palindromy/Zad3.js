/*
Dla podanych dwoch napisow sprawdz czy sa swoimi anagramami.
Dwa napisy sa anagramami jesli jeden z nich mozna zbudowac
poprzez przestawienie znakow w drugim.
*/
anagramy = function(napis1, napis2) {
    if (napis1.length !== napis2.length)
        return false;
    var tab1 = zamienNaTab(napis1);
    var tab2 = zamienNaTab(napis2);
    for (var i = 0; i < tab1.length; i++) {
        var index = tab2.indexOf(tab1[i]);
        if (index === -1)
            return false;
        tab2[index] = -1;
    }
    return true;
};
zamienNaTab = function(napis) {
    var tab = [];
    for (var i = 0; i < napis.length; i++) {
        tab.push(napis.charAt(i));
    }
    return tab;
};
test1 = function() {
    var napis1 = "adam";
    var napis2 = "mada";
    var oczekiwane = true;
    var wynik = anagramy(napis1, napis2);
    if (!(wynik === oczekiwane)) {
        throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
    }
};
test2 = function() {
    var napis1 = "adam";
    var napis2 = "ada";
    var oczekiwane = false;
    var wynik = anagramy(napis1, napis2);
    if (!(wynik === oczekiwane)) {
        throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
    }
};
main = function(args) {
    test1();
    test2();
};

main(null);