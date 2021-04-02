var Main = (function() {
    function Main() {}
    Main.liczby = function(n) {
        var wynik = "";
        for (var i = 1; i <= n; i++) {
            {
                wynik += String(i).toString();
            };
        }
        return wynik;
    };
    Main.test1 = function() {
        var n = 5;
        var wynik = "12345";
        if (!(wynik === Main.liczby(n))) {
            throw new Error("Assertion error line 13: assert wynik.equals(liczby(n));");
        };
    };
    Main.test2 = function() {
        var n = -1;
        var wynik = "";
        if (!(wynik === Main.liczby(n))) {
            throw new Error("Assertion error line 19: assert wynik.equals(liczby(n));");
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
