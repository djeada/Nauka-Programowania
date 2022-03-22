/*
Znajdz wszystkie wyjatkowe palindromy jakie mozna utworzyc ze znakow w slowie
(bez zmiany kolejnosci wystepowania). Nie uwzgledniaj duplikatow w liscie.
Wyjatkowy palindrom musi spelniac jeden z dwoch warunkow:
1. Wszystkie znaki sa identyczne, np. “xxx”.
2. Wszystkie znaki poza srodkowym znakiem sa identyczne, np. “ccdcc”.
Pojedynczy znak jest rowniez uznawany za wyjatkowy palindrom.
*/

var Main = /** @class */ (function () {
    function Main() {}
    Main.wyjatkowePalindromy = function (slowo) {
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
    Main.test1 = function () {
        var slowo = "xxx";
        var wynik = new Set(["x", "xx", "xxx", "xxxx"]);
        var wynik2 = Main.wyjatkowePalindromy(slowo);
        if (!(wynik.size === wynik2.size)) {
            throw new Error("Assertion error line 24: assert wynik.size === wynik2.size;");
        }
        for (var _i = 0, _a = Array.from(wynik); _i < _a.length; _i++) {
            var x = _a[_i];
            if (!(wynik2.has(x))) {
                throw new Error("Assertion error line 26: assert wynik2.has(x);");
            }
        }
    };
    Main.test2 = function () {
        var slowo = "ccdcc";
        var wynik = new Set(["cc", "d", "ccdcc", "c", "cdc"]);
        var wynik2 = Main.wyjatkowePalindromy(slowo);
        if (!(wynik.size === wynik2.size)) {
            throw new Error("Assertion error line 34: assert wynik.size === wynik2.size;");
        }
        for (var _i = 0, _a = Array.from(wynik); _i < _a.length; _i++) {
            var x = _a[_i];
            if (!(wynik2.has(x))) {
                throw new Error("Assertion error line 36: assert wynik2.has(x);");
            }
        }
    }
    Main.test3 = function () {
        var slowo = "abc";
        var wynik = new Set(["a", "b", "c"]);
        var wynik2 = Main.wyjatkowePalindromy(slowo);
        if (!(wynik.size === wynik2.size)) {
            throw new Error("Assertion error line 44: assert wynik.size === wynik2.size;");
        }
        for (var _i = 0, _a = Array.from(wynik); _i < _a.length; _i++) {
            var x = _a[_i];
            if (!(wynik2.has(x))) {
                throw new Error("Assertion error line 46: assert wynik2.has(x);");
            }
        }
    }
    Main.main = function (args) {
        Main.test1();
        Main.test2();
        Main.test3();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
