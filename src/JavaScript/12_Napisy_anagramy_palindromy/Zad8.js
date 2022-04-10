/*
Znajdz wszystkie wyjatkowe palindromy jakie mozna utworzyc ze znakow w slowie
(bez zmiany kolejnosci wystepowania). Nie uwzgledniaj duplikatow w liscie.
Wyjatkowy palindrom musi spelniac jeden z dwoch warunkow:
1. Wszystkie znaki sa identyczne, np. “xxx”.
2. Wszystkie znaki poza srodkowym znakiem sa identyczne, np. “ccdcc”.
Pojedynczy znak jest rowniez uznawany za wyjatkowy palindrom.
*/
wyjatkowePalindromy = function(slowo) {
    var wynik = new Set();
    for (var i = 0; i < slowo.length; i++) {
        wynik.add(slowo[i]);
        var j = i + 1;
        var k = 0;
        while (j < slowo.length && slowo[i] == slowo[j])
            j++;
        if (j > i + 1)
            wynik.add(slowo.substr(i, i - j));
        if (j + 1 < slowo.length && slowo[i] == slowo[j + 1])
            k = j + 1;
        while (k > i && slowo[i] == slowo[k])
            k--;
        if (i + 1 == k)
            wynik.add(slowo.substr(i, 2 * (j - i) + 1));
    }
    return wynik;
};
test1 = function() {
    var slowo = "xxx";
    var oczekiwane = new Set(["x", "xx", "xxx", "xxxx"]);
    var wynik = wyjatkowePalindromy(slowo);
    if (wynik.size !== oczekiwane.size) {
        throw new Error(`Assertion error line 29: ${wynik.size} != ${oczekiwane.size}`);
    }
    oczekiwane.forEach(function(element) {
        if (!wynik.has(element)) {
            throw new Error(`Assertion error line 29: ${element} not found`);
        }
    });
};
test2 = function() {
    var slowo = "ccdcc";
    var oczekiwane = new Set(["cc", "d", "ccdcc", "c", "cdc"]);
    var wynik = wyjatkowePalindromy(slowo);
    if (wynik.size !== oczekiwane.size) {
        throw new Error(`Assertion error line 29: ${wynik.size} != ${oczekiwane.size}`);
    }
    oczekiwane.forEach(function(element) {
        if (!wynik.has(element)) {
            throw new Error(`Assertion error line 29: ${element} not found`);
        }
    });
}
test3 = function() {
    var slowo = "abc";
    var oczekiwane = new Set(["a", "b", "c"]);
    var wynik = wyjatkowePalindromy(slowo);
    if (wynik.size !== oczekiwane.size) {
        throw new Error(`Assertion error line 29: ${wynik.size} != ${oczekiwane.size}`);
    }
    oczekiwane.forEach(function(element) {
        if (!wynik.has(element)) {
            throw new Error(`Assertion error line 29: ${element} not found`);
        }
    });
}
main = function(args) {
    test1();
    test2();
    test3();
};

main(null);