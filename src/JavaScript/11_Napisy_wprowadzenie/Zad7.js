var Main = (function() {
    function Main() {}
    Main.zamienV1 = function(napis) {
        if (napis.length === 0) {
            return "";
        }
        var wynik = ""; {
            var tablica = (napis).split('');
            for (var i = 0; i < tablica.length; i++) {
                var numer = tablica[i]; {
                    wynik += numer.charCodeAt(0) + ", ";
                }
            }
        }
        return wynik.substring(0, wynik.length - 2);
    };
    Main.test1 = function() {
        var napis = "pacZka!";
        var wynik = "112, 97, 99, 90, 107, 97, 33";

        if (!(Main.zamienV1(napis) === wynik)) {
            throw new Error("Assertion error;");
        };
    };
    Main.test2 = function() {
        var napis = "";
        var wynik = "";
        if (!(Main.zamienV1(napis) === wynik)) {
            throw new Error("Assertion error;");
        };
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
